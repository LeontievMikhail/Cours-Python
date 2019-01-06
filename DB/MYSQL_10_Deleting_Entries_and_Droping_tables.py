import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="testdb"
)

mycursor=mydb.cursor()
# sql = "DELETE FROM students WHERE name='Alex'"
# sql = "DELETE FROM students WHERE age=55"
# mycursor.execute(sql)
# mydb.commit()

sql = "DROP TABLE IF EXISTS students"
mycursor.execute(sql)
mydb.commit()