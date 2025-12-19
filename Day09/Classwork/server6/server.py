from flask import Flask, request

from createCustomResponse import createCustomResponse
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@app.route('/student', methods=['GET', 'POST', 'PUT', 'DELETE'])
def student_ops():
    if request.method == 'POST':
        rollno = request.get_json().get('rollno')
        name = request.get_json().get('name')
        email = request.get_json().get('email')
        course = request.get_json().get('course')

        query = f"insert into stu_info values({rollno}, '{name}', '{email}', '{course}');"

        executeQuery(query=query)
        msg = "student is added successfully"

    elif request.method == 'GET':
        query = "select * from stu_info;"    
        data = executeSelectQuery(query=query)

        msg =  f"students : {data}"

    elif request.method == 'PUT':
        name = request.get_json().get('name')
        email = request.get_json().get('email')

        query = f"update stu_info SET email = '{email}' where name = '{name}';"

        executeQuery(query=query)
        msg = "student is updated successfully"
        
    elif request.method == 'DELETE':
        name = request.get_json().get('name')

        query = f"delete from stu_info where name = '{name}';"

        executeQuery(query=query)
        msg = "student is deleted successfully"

    return createCustomResponse(msg, error=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)    