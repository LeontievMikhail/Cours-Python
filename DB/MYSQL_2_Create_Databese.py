import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
# print(mydb)

mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE testdb")

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)
