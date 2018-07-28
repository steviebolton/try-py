import pymysql
import os

connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password=os.environ.get("DB_PASSWORD"),
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        list_of_names = ['jim', 'bob']
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute("delete from Friends where name in ({0})".format(format_strings), list_of_names)
        connection.commit()
finally:
    connection.close()