import pymysql
import datetime
import os

connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password=os.environ.get("DB_PASSWORD"),
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        data = [("bob", 21, "1990-02-06 23:04:56"),
                ("jim", 56, "1955-05-09 13:12:45"),
                ("fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("insert into Friends values (%s,%s,%s)", data)
        connection.commit()
finally:
    connection.close()