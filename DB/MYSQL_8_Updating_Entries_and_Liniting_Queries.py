import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="testdb"
)
# print(mydb)

mycursor=mydb.cursor()

sql="UPDATE students SET age = 113 WHERE name='Anna'"
mycursor.execute(sql)
mydb.commit()

# sql="SELECT * FROM students ORDER BY name DESC"
sql="SELECT * FROM students LIMIT 5 OFFSET 2"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for r in myresult:
    print(r)
