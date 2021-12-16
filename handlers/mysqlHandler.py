import mysql.connector
from mysql.connector import Error, connect

try:

    connection = mysql.connector.connect(host = 'localhost',
                                         database = 'marketwatcher',
                                         user = 'root',
                                         password = '')

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server Version: ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record[0])

except Error as e:
    print(f"An exception has occurred {e}")


def defaultQuery(query, parameters):

    try:

        if 'INSERT' in query:       # If it's an insert query
            
            cursor.execute(query, parameters)
            connection.commit()
            return True

        else:                       # Most probably a select query
            
            cursor.execute(query, parameters)
            return cursor.fetchall()

    except Exception as e:
        # Extend on error handeling
        print(f"MySQL ERROR {e}")
        return False