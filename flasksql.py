from flask import Flask, render_template
import pymysql
import os

app = Flask(__name__)



def do_select(sql):
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user=os.environ.get("C9_USER"),
                                 password=os.environ.get("DB_PASSWORD"),
                                 db='Chinook')

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
                
    finally:
        connection.close()




@app.route('/')
def get_artists():
    return render_template("index.html", artists=do_select("select * from Artist"))
    
@app.route('/artist/<id>')
def get_an_artist(id):
    sql = "select * from Artist where ArtistId = {0}".format(id)
    artist = do_select(sql)[0]
    sql = "select * from Album where ArtistId = {0}".format(id)
    albums = do_select(sql)
    return render_template("artist_details.html", artist=artist, albums=albums)

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)