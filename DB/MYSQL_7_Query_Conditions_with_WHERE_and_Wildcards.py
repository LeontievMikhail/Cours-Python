import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="testdb"
)

mycursor=mydb.cursor()
# sql = "SELECT * FROM students WHERE age=22"
# sql = "SELECT * FROM students WHERE name='Anna'"
sql = "SELECT * FROM students WHERE name LIKE '%a%'"

mycursor.execute(sql)
myresult=mycursor.fetchall()
for result in myresult:
    print(result)

print("2 _________")

sql1 = "SELECT * FROM students WHERE name = %s"
mycursor.execute(sql1, ("Anna",))
myresult1=mycursor.fetchall()
for result1 in myresult1:
    print(result1)

