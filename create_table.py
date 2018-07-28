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
        cursor.execute("drop table if exists Friends")
        cursor.execute("CREATE TABLE Friends (name char(20), age int , DOB datetime)")
finally:
    connection.close()

