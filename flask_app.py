
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('signup.html')

@app.route('/signup' , methods=['POST'])
def signup():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("INSERT INTO user(username, password) VALUES (?,?)",
                    (request.form['un'],request.form['pw']))
    con.commit()
    return 'user added'
@app.route('/create')
def create():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE user(
        username VARCHAR(20) NOT NULL PRIMARY KEY,
        password VARCHAR(20) NOT NULL)
        """)
    return 'tbl created'

@app.route('/login', methods=['POST'])
def login():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Users WHERE Username=? AND Password=?",
                    (request.form['un'],request.form['pw']))
    match = len(cur.fetchall())
    if match == 0:
        return "Wrong username and password"
    else:
        return "Welcome " + request.form['un']
  
@app.route('/insert')
def insert():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("""INSERT INTO user(username, password)
                    VALUES ("bob" , "123")
        """)
    con.commit()
    return 'insert!'

@app.route('/select')
def select():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    return str(rows)
