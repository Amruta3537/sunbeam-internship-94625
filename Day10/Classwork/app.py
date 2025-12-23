from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
import mysql.connector
import os
from passlib.hash import sha256_crypt
crypto = sha256_crypt

def getConnection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="edu",
        use_pure=True
    )

def executeQuery(sql, params):
    with getConnection() as con:
        with con.cursor(dictionary=True) as cur:
            cur.execute(sql, params)
            if cur.description:
                return cur.fetchall()
                # SELECT query yields list of dicts
            else:
                con.commit()
                return {"affectedRows": cur.rowcount}


def createResult(error, data):
    if data:
        return jsonify(status="success", data=data)
    else:
        return jsonify(status="error", error=error)

app = Flask(__name__)
jwt_secret = os.getenv("MY_JWT_SECRET")
app.config["JWT_SECRET_KEY"] = jwt_secret
jwt_mgr = JWTManager(app)

@jwt_mgr.invalid_token_loader
def invalid_token_handler(e):
    return createResult("Invalid JWT Token", None)

@jwt_mgr.unauthorized_loader
def unauthorized_handler(e):
    return createResult("JWT Token Absent", None)

# global error handlers are production feature.
# not executed when debug mode enabled.
@app.errorhandler(500)
def handle_exception(e):
    err = getattr(e, "original_exception")
    return createResult(error=repr(err), data=None)


@app.get("/students")
@jwt_required()
def getAllStudents():
    jwt_payload = get_jwt()
    print(jwt_payload)
    sql = "SELECT * FROM students"
    result = executeQuery(sql, None)
    return createResult(None, result)

@app.get("/students/<int:rollno>")
@jwt_required()
def getStudent(rollno):
    sql = "SELECT * FROM students WHERE rollno = %s"
    result = executeQuery(sql, (rollno,))
    return createResult(None, result)

@app.post("/students")
@jwt_required()
def addStudent():
    sql = "INSERT INTO students(name, email, course) VALUES(%s, %s, %s)"
    params = (
        request.json["name"],
        request.json["email"],
        request.json["course"]
    )
    result = executeQuery(sql, params)
    return createResult(None, result)

@app.put("/students/<int:rollno>")
@jwt_required()
def updateStudent(rollno):
    sql = "UPDATE students SET name=%s, email=%s, course=%s WHERE rollno=%s"
    params = (
        request.json["name"],
        request.json["email"],
        request.json["course"],
        rollno
    )
    result = executeQuery(sql, params)
    return createResult(None, result)

@app.delete("/students")
@jwt_required()
def deleteStudent():
    rollno = request.args.get("rollno")
    sql = "DELETE FROM students WHERE rollno=%s"
    result = executeQuery(sql, (rollno,))
    return createResult(None, result)

@app.post("/users/signup")
def signup():
    sql = "INSERT INTO users(name, email, password, mobile) VALUES(%s, %s, %s, %s)"
    encPassword = crypto.hash(request.json["password"])
    params = (
        request.json["name"],
        request.json["email"],
        encPassword,
        request.json["mobile"]
    )
    result = executeQuery(sql, params)
    return createResult(error=None, data=result)

@app.post("/users/signin")
def signin():
    sql = "SELECT * FROM users WHERE email = %s"
    result = executeQuery(sql, (request.json["email"],))
    success = False
    if len(result) > 0: # user is found
        rawPasswd = request.json["password"] # entered by user
        encPasswd = result[0]["password"] # retrieved from db
        success = crypto.verify(rawPasswd, encPasswd)
    if not success:
        return createResult("Invalid email or password", None)
    result[0]["password"] = "*****"
    jwt = create_access_token(identity=request.json["email"],
                              expires_delta=False)
    result[0]["token"] = jwt
    return createResult(None, result[0])

if __name__ == "__main__":
    app.run(debug=True)
