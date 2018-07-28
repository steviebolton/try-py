import pymysql
import os

connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password=os.environ.get("DB_PASSWORD"),
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        rows = cursor.execute("delete from Friends where name = %s", 'bob')
        connection.commit()
finally:
    connection.close()