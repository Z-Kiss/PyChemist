import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv, find_dotenv


def get_connection_data():
    load_dotenv(find_dotenv("config.env"))

    return {
        'dbname': os.getenv('DATABASE_NAME'),
        'user': os.getenv('USER_NAME'),
        'host': os.getenv('HOST'),
        'password': os.getenv('USER_PASSWORD')
    }


def establish_connection(connection_data=None):
    """
    Create a database connection based on the :connection_data: parameter
    :connection_data: Connection string attributes
    :returns: psycopg2.connection
    """
    if connection_data is None:
        connection_data = get_connection_data()
    try:
        connect_str = "dbname={} user={} host={} password={}".format(connection_data['dbname'],
                                                                     connection_data['user'],
                                                                     connection_data['host'],
                                                                     connection_data['password'])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)
    else:
        print("Successfully Connected")
        return conn


establish_connection()
