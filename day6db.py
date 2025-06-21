import sqlite3

db=sqlite3.connect("school.db")#create db file

cursor=db.cursor()#create a cursor object to execute sql commands
cursor.execute('''CREATE TABLE IF NOT EXISTS 
               students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER,
               grade TEXT)''')


db.commit()
#inserting data(create)
cursor.execute("""
INSERT INTO students(name,age,grade)
VALUES(?,?,?)
""",("Alice","20","A"))
db.commit()
#Fetch all rows
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)
#fetchone()=Fetches first row,fetchmany(n)=Fetch next row,fetchall()=Fetches all remaining

#Updating data
cursor.execute("""
UPDATE students
SET grade =?
WHERE name=?                            
""",("A+","Bob"))

db.commit()
cursor.execute("""
DELETE FROM students
WHERE name = ?               
""",("Charlie",))
db.commit()

#OR 1=1 -> attackers will set this command(SQL Injection)
'''
true for every entry, giving directly access to sql commands is dangerous
->?",("Alice",)
->"OR 1=1 is a py str
'''