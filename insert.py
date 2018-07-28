import pymysql
import datetime
import os

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password=os.environ.get("DB_PASSWORD"),
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        data = ("bob", 21, "1990-02-06 23:04:56")
        cursor.execute("insert into Friends values (%s,%s,%s)", data)
        connection.commit()
finally:
    connection.close()