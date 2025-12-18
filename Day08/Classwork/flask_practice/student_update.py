import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "manager",
    database = "student",
    use_pure = True
)

name = input("Enter name whose email to be updated : ")
email = input("Enter new email : ")

query = f"update stu_info SET email = '{email}' where name = '{name}';"

cursor = connection.cursor()

cursor.execute(query)
connection.commit()

cursor.close()
connection.close()