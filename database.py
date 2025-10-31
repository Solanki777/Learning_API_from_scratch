# 1️⃣ Flask

# You already know — it’s your main web framework that helps you make APIs and websites in Python.

# 2️⃣ SQLAlchemy

# This is a Python library that helps your Flask app talk to a database (like SQLite or MySQL) easily.
# Instead of writing long SQL commands manually (like SELECT * FROM students)

# 🌍 Step 2: What is an “environment”?

# Good question — this confuses many beginners, so let’s simplify it 💡

# Imagine your computer like a big school 🏫 — it has many students (projects).

# Each project might need different versions of Flask, Python libraries, etc.
# So we make a small classroom for each project — where only that project’s tools are installed.
# That small classroom is called a Virtual Environment.

# 💡 In simple terms:

# Without environment: all projects share the same installed packages — can cause version problems.

# With environment: each project has its own isolated set of libraries.
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
# SQLALchemy is databse handler library

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///student.db'
# Tells SQLAlchemy to use SQLite and store data in a file named students.db (in the same folder).
# Format: sqlite:///filename.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#This is a Flask-SQLAlchemy configuration setting — it tells SQLAlchemy whether it should track every change you make to the objects in your database.
db=SQLAlchemy(app)
# connects SQLAlchemy to youtr Flask app . from now on db is your database controller


# define the table(model0)
class Student(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    work=db.Column(db.String(200),nullable=True)


# it convert this table data into python dictionary which is useful when sending JSON
    def to_dict(self):
        return{"id":self.id,"name":self.name,"work":self.work}
    

# Think of Flask like a school 🏫
# Inside it, your app (app = Flask(__name__)) is like a specific classroom.

# Whenever Flask runs, it needs to know which classroom (app) it’s working in — this is called the application context.    
with app.app_context():
    db.create_all()

# Normally, Flask automatically creates this context when you run:
# python app.py
# (because app.run() starts the server).
# But when you are just running a Python file manually (like database.py), Flask doesn’t automatically know which app to use.
# So, to tell Flask:
# “Hey, use this app while you run these commands,”
# ⚙️ Step 2: What does db.create_all() do?

# Once Flask knows which app is active, db.create_all() tells SQLAlchemy:

# “Go ahead and create all the database tables that I have defined using db.Model.”



# to see the database download sqlite viewer extension


