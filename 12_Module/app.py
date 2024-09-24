from flask import Flask, request, flash, url_for, redirect,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://students_3.sqlite3'
app.config['SECRET_KEY'] = 'random string'

db = SQLAlchemy(app)

class student_3(db.Model):
    id = db.Column('student_id',db.Integer, primary_key = True)
    name = db.Column(db.string(100))
    city = db.Column(db.string(100))
    addr = db.Column(db.string(100))
    pin = db.Column(db.string(10))

def __init__(self, name, city, addr, pin):
    self.name = name
    self.city = city
    self.addr = addr
    self.pin = pin


@app.route('/')
def show_all():
    return render_template('show_all.html', students = student_3.query.all())


if __name__=="__main__":
    app.run()