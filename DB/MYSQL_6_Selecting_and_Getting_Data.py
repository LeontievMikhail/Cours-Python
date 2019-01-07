import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="testdb"
)

# print(mydb)

mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM students")
myresult=mycursor.fetchall()
# myresult=mycursor.fetchone()

for row in myresult:
    print(row)

