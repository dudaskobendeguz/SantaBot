import csv
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


def open_csv_file(file_path):
    with open(file_path, mode='r') as file:
        return [line.split(';') for line in file.read().splitlines()]


def create_data_dictionary(data_list):
    categories = data_list[0]
    return [{categories[number]: detail[number] for number, category in enumerate(categories)} for detail in
            data_list[1:]]


@database_common.connection_handler
def drop_table(cursor, table_name):
    cursor.execute(sql.SQL("""
        DROP TABLE IF EXISTS {table}
    """).format(table=sql.Identifier(table_name)))


@database_common.connection_handler
def create_karmas_table(cursor):
    query = """
        CREATE TABLE IF NOT EXISTS karmas(
            id SERIAL PRIMARY KEY,
            action_type TEXT,
            action TEXT
        )
    """
    cursor.execute(query)


@database_common.connection_handler
def create_profiles_table(cursor):
    query = """
        CREATE TABLE IF NOT EXISTS profiles(
            id SERIAL PRIMARY KEY,
            name TEXT,
            actions VARCHAR,
            ideal_present_categories TEXT
        )
    """
    cursor.execute(query)


@database_common.connection_handler
def import_data_to_karmas_table(cursor, karmas):
    for karma in karmas:
        cursor.execute(sql.SQL("""
            INSERT INTO karmas(action_type, action) 
            VALUES({action_type}, {action}) 
        """).format(
            action_type=sql.Literal(karma['action type']),
            action=sql.Literal(karma['action'])
                                    ))


def create_database():
    drop_table('profiles')
    create_profiles_table()
    drop_table('karmas')
    create_karmas_table()
    profiles_data = open_csv_file(file_path='data/profiles.csv')
    profiles = create_data_dictionary(profiles_data)
    karmas_data = open_csv_file(file_path='data/karma.csv')
    karmas = create_data_dictionary(karmas_data)
    import_data_to_karmas_table(karmas)
    print(profiles)
    print(karmas)


if __name__ == "__main__":
    create_database()
