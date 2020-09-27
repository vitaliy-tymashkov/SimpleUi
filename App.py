from flask import Flask, render_template
from datetime import datetime
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route("/")
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    currentTimeStampString = 'Started at: ' + timestampStr

    print(currentTimeStampString)

    f = open("logfile.txt", "wt")
    f.write(currentTimeStampString)
    f.close()

    app.run(host="0.0.0.0", port=57777, debug=True)