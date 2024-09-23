import sqlite3

conn = sqlite3.connect('database_2.db')
print("Opened database successfully...!!")

conn.execute('CREATE TABLE students_2 (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print('Table created Successfully')
conn.close()