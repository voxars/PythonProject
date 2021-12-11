import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask import Flask,render_template,session,url_for,request
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect


app = Flask(__name__)
DATABASE = "./main.db"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# https://sites.uclouvain.be/P2SINF/flask/tutorial/database.html

#  Database Connection

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


# Database Disconnection

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()  

# Create table
def init_db():
    db = get_db()

    with current_app.open_resource('bdd.sql') as f:
        db.executescript(f.read().decode('utf8'))
    print('db create')    

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.cli.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Database initialized.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app

# ROUTE
#Init ROUTE
@app.route("/")
def index():
    return render_template('index.html')





# ROUTE   
@app.route('/post-login', methods=['post'])
def login():
    if request.method == 'POST':
         username = request.form['username']
         password = request.form['password']
         print('Username:',username, 'password',password)
         hashpassword = checkLogin(username, password)
         if check_password_hash(hashpassword,password):
             # todo redirect to create book 
             session['username'] = request.form['username']
             return redirect('/list')
         else:
             session.pop('username', None)
             return 'Accès non autorisé'
    else:
         return render_template('index.html')



@app.route('/notConnected')
def notConnect():
    return render_template("notconnected.html")

@app.route('/list')
def list():
     if 'username' in session:
         rows = query_db('select * from book')
         return render_template("ListBooks.html",rows = rows)
     return redirect('/notConnected')


@app.route('/createBook')
def createBook():
    
   click.echo('Book.')

   return render_template("CreateBook.html")




def checkLogin(username, password):
    user = query_db('select * from user where username = ?',
                [username], one=True)
    if user is None:
        return 'No such user'
    else:
        return user['password']


def addBook(title,author,quantity,kind):
     cur = get_db().execute('INSERT INTO Book (title, author, quantity, kind) VALUES ( ?, ?, ?, ? )', [title,author,quantity,kind])
     get_db().commit()





    
        