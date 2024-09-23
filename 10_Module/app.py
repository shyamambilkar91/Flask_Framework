from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    global msg
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect('database_2.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students_2(name, addr, city, pin) VALUES (?,?,?,?)", (nm, addr, city, pin))

                con.commit()
                msg = "Record Successfully added"
        except:
            con.rollback()
            msg = "Error in Insert Operation...!!"
        finally:
            return render_template('result.html', msg=msg)


@app.route('/list')
def list():
    con = sql.connect('database_2.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM students_2')

    rows = cur.fetchall()
    return render_template('list.html', rows = rows)


if __name__ == "__main__":
    app.run()
