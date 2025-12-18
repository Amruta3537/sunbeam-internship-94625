import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "manager",
    database = "student",
    use_pure = True
)

rollno = int(input("Enter rollno of a student to be deleted : "))

query = f"delete from stu_info where rollno = {rollno};"

cursor = connection.cursor()

cursor.execute(query)
connection.commit()

cursor.close()
connection.close()