# pip install mysql-connector-python

import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "manager",
    database = "student",
    use_pure = True
)

query = "select * from stu_info;"

cursor = connection.cursor()

cursor.execute(query)

stu_info = cursor.fetchall()

for student in stu_info:
    print(student)


cursor.close()
connection.close()