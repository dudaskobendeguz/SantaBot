from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common
import server


@database_common.connection_handler
def get_people(cursor):
    query = """
            SELECT * FROM gift_list;
    """

    cursor.execute(query)
    return cursor.fetchall()