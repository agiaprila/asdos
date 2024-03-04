from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dataasdos'

mysql =MySQL(app)

@app.route("/")
def home ():
    return render_template ('home.html')

@app.route("/data")
def data ():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM asdos")
        dataa = cur.fetchall()
        cur.close()
        return render_template ('data.html', asdos=dataa)

@app.route("/profileMc")
def profileMc ():
    return render_template ('profileMc.html')


if __name__ == "__main__" :
    app.run(debug=True, port=5001)