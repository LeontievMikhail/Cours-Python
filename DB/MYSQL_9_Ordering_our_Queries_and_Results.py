import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="testdb"
)
print(mydb)

mycursor=mydb.cursor()

sql="SELECT * FROM students ORDER BY name"
# sql="SELECT * FROM students ORDER BY age"
# sql="SELECT * FROM students ORDER BY age DESC"

mycursor.execute(sql)

myresult=mycursor.fetchall()
for r in myresult:
    print(r)