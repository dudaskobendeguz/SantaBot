import csv

import database_common


def open_csv_file_into_dict(file_path):
    with open(file_path, mode='r') as file:
        return [dictionary for dictionary in csv.DictReader(file)]


def open_csv_file(file_path):
    with open(file_path, mode='r') as file:
        return [line.split(';') for line in file.read().splitlines()]


def create_profiles_dictionary(profiles_list):

    def get_categories(categories_list):
        category_list = []
        for category in categories_list:
            if 'ideal' in category:
                category = category.split(' ', maxsplit=1)
                category_list += category
            else:
                category_list.append(category)
        return category_list

    categories = get_categories(profiles_list[0])

    profiles = []
    for profile in profiles_list[1:]:
        profile += profile[-1].split(',')
        profile.pop(2)
        profiles.append({categories[number]: profile[number] for number, category in enumerate(categories)})

    return profiles


def get_karma(karmas_list):
    action_types = karmas_list[0]
    karmas = []
    for karma in karmas_list[1:]:
        karmas.append({action_types[number]: karma[number] for number, action_type in enumerate(action_types)})
    return karmas


@database_common.connection_handler
def create_karmas_table(cursor):
    query = """
        CREATE TABLE IF NOT EXISTS karmas(
            id INTEGER PRIMARY KEY,
            action_type TEXT,
            action TEXT
        )
    """
    cursor.execute(query)


@database_common.connection_handler
def create_profiles_table(cursor):
    query = """
        CREATE TABLE IF NOT EXISTS profiles(
            id INTEGER PRIMARY KEY,
            name TEXT,
            actions VARCHAR,
            ideal TEXT,
            present_categories TEXT
        )
    """
    cursor.execute(query)


def create_database():
    profiles_data = open_csv_file(file_path='data/profiles.csv')
    profiles = create_profiles_dictionary(profiles_data)
    karmas_data = open_csv_file(file_path='data/karma.csv')
    karmas = get_karma(karmas_data)
    print(profiles)
    print(karmas)
    create_profiles_table()
    create_karmas_table()


if __name__ == "__main__":
    create_database()

