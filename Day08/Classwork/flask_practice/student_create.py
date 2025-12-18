import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "manager",
    database = "student",
    use_pure = True
)

rollno = int(input("Enter rollno : "))
name = input("Enter name : ")
email = input("Enter email : ")
course = input("Enter course : ")

query = f"insert into stu_info values({rollno}, '{name}', '{email}', '{course}');"


cursor = connection.cursor()

cursor.execute(query)
connection.commit()

cursor.close()
connection.close()