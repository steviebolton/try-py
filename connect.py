import pymysql.cursors
import pymysql
import os


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password=os.environ.get("DB_PASSWORD"),
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()



