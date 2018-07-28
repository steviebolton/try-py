import pymysql
import os

connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password=os.environ.get("DB_PASSWORD"),
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        data = [
                (23, 'bob'),
                (24, 'jim'),
                (25, 'fred')
            ]
        rows = cursor.executemany("update Friends set age = %s where name = %s", data)
        connection.commit()
finally:
    connection.close()

