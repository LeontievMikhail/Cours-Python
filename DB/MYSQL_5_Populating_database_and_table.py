import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="testdb"
)

mycursor=mydb.cursor()

# sqlFormula="INSERT INTO students (name, age) VALUES (%s, %s)"
# student1=("Rachel", 22)
# student2=("Mikhail", 33)
#
# mycursor.execute(sqlFormula, student1)
# mycursor.execute(sqlFormula, student2)
#
# mydb.commit()

sqlFormula="INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("Bob", 12),
            ("Anna", 22),
            ("Alex", 33),
            ("Emma", 55)
            ]
mycursor.executemany(sqlFormula, students)

mydb.commit()



