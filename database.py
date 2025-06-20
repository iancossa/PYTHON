import sqlite3

#Create a db file
db=sqlite3.connect("mydb.db")

cursorobj= db.cursor()#cursor object->Bridge between python code and db
#used to run  sqlite3 commands

cursorobj.execute('''
                    CREATE TABLE IF NOT EXISTS students
                    (id INTEGER PRIMARY  KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    grade   TEXT)''')#create table using pyhton on sqlite3

cursorobj.execute('''
INSERT INTO students(name,age,grade)
VALUES(?,?,?)
''',("Alice",20,"A"))

db.commit()
#insert multiple data

stu_data=[("Bob",19,"B"),("Charlie",21,"A+"),("David",22,"B+")]
cursorobj.executemany("""INSERT INTO students(name,age,grade)VALUES(?,?,?)""",stu_data)
db.commit()