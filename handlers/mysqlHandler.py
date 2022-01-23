import mysql.connector, json
from mysql.connector import Error, connect

try:

    with open("./config.json", "r") as jsonfile:
        config = json.load(jsonfile)

    connection = mysql.connector.connect(host = config["database"]["host"],
                                         database = config["database"]["database"],
                                         user = config["database"]["user"],
                                         password = config["database"]["password"])

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server Version: ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record[0])

except Error as e:
    print(f"(mysqlHandler.py) An exception has occurred {e}")


def defaultQuery(query, parameters):

    try:

        cursor.execute(query, parameters)

        if 'INSERT' in query:       # If it's an insert query
            connection.commit()
            return True

        elif 'UPDATE' in query:
            return True

        elif 'SELECT' in query:
            return cursor.fetchall()

        return

    except Exception as e:
        # Extend on error handeling
        print(f"(mysqlHandler.py) MySQL ERROR while trying to execute Query {query} with parameters {parameters} : {e}")
        return False