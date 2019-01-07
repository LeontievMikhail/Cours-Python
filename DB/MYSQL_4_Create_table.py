import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="testdb"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS students (name VARCHAR(255), age INTEGER (10))")
mycursor.execute("SHOW TABLES")
for tables in mycursor:
    print(tables)


#IF NOT EXISTS