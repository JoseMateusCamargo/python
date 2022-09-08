import mysql.connector
from mysql.connector import Error

query = """SELECT ID, INVENTORY_ID FROM db_cadastro LIMIT 10;"""

try:

    config = {'user': 'root', 'password': '', 'host': '127.0.0.1', 'database': 'data_base_name',
              'raise_on_warnings': True}

    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

        cursor = connection.cursor()
        cursor.execute(query)

        for (id_, inventory) in cursor:
            print("{}, {}".format(id_, inventory))

        cursor.execute("select database();")
        record = cursor.fetchone()
        print("\nYou're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
