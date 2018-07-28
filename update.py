import pymysql
import os

connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password=os.environ.get("DB_PASSWORD"),
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        cursor.execute("update Friends set age = 22 where name = 'bob'")
        connection.commit()
finally:
    connection.close()