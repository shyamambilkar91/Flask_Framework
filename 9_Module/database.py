import sqlite3

conn = sqlite3.connect('database1.db')
print("Open Database Successfully...!!")

conn.execute('CREATE TABLE students_1 (f_name TEXT, l_name TEXT, address TEXT, city TEXT, contact TEXT, pincode TEXT )')
print("Table created Successfully...!!")
conn.close()