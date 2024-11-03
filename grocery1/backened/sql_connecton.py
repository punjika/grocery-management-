# import mysql.connector
#
# __cnx = None
#
#
# def get_sql_connection():
#     global __cnx
#     if __cnx is None:
#         cnx = mysql.connector.connect(user='root', password='Mysql@123',
#                                       host='127.0.0.1',
#                                       database='grocerystore')
#
#     return __cnx

# Example implementation of get_sql_connection
import mysql.connector
from mysql.connector import Error


def get_sql_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='grocerystore',
            user='root',
            password='Mysql@123'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
