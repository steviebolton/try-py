# import pymysql.cursors
import pymysql
import os

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password=os.environ.get("DB_PASSWORD"),
                             db='Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row['Name'])
finally:
    connection.close()