from flask import Flask , request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/student')
def create_student():
    rollno = request.form.get('rollno')
    name = request.form.get('name')
    email = request.form.get('email')
    course = request.form.get('course')

    query = f"insert into stu_info values({rollno}, '{name}', '{email}', '{course}');"

    executeQuery(query=query)

    return "student is added successfully"

@server.get('/student')
def retrieve_students():
    query = "select * from stu_info;"    
    data = executeSelectQuery(query=query)

    return f"students : {data}"    

@server.put('/student')
def update_student():
    name = request.form.get('name')
    email = request.form.get('email')

    query = f"update stu_info SET email = '{email}' where name = '{name}';"

    executeQuery(query=query)

    return "email is updated successfully"

@server.delete('/student')
def delete_student():
    name = request.form.get('name')

    query = f"delete from stu_info where name = '{name}';"

    executeQuery(query=query)

    return "student is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)