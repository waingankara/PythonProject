import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"homework.db"

    sql_create_homeworkUpload_table = """CREATE TABLE IF NOT EXISTS homeworkUpload (
                                    id integer PRIMARY KEY,
                                    standard text NOT NULL,
                                    division text NOT NULL,
                                    subject text NOT NULL,
                                    date_of_homework  text NOT NULL,
                                    teacher_name text NOT NULL,
                                    type_of_homework text NOT NULL,
                                    desc_of_homework text NOT NULL,
                                    upload_timestamp text NOT NULL
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:

        # create tasks table
        create_table(conn, sql_create_homeworkUpload_table)
    else:
        print("Error! cannot create the database connection.")


def create_homework(homework):
    database = r"homework.db"

    # create a database connection
    conn = create_connection(database)
    with conn:

        sql = ''' INSERT INTO homeworkUpload(standard,division,subject,date_of_homework,teacher_name,type_of_homework,desc_of_homework,upload_timestamp)
                  VALUES(?,?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, homework)
        return cur.lastrowid

def select_all_homeworks():
    database = r"homework.db"

    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT * FROM homeworkUpload")

    rows = cur.fetchall()

    return rows