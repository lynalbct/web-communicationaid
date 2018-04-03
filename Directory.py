from flask import Flask,render_template,request,redirect,url_for
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect("dbname='proj18' user='postgres' password='coycoy6197' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM teacher""")
    rows = cur.fetchall()
    return render_template('directory.html', rows=rows)

if __name__ == '__main__':
    app.run()
