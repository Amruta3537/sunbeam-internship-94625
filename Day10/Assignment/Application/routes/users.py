from utils.util import crypto
from flask import Blueprint, request, jsonify
from flask_jwt_extended import (create_access_token)
import os
import utils.db as db
from utils.util import createResult
from utils.util import crypto

usersRouter = Blueprint("users", __name__, url_prefix="/users")


@usersRouter.route("/signup", methods=["POST"])
def signup():
    data = request.json

    # fixed student password from env
    fixed_password = os.getenv("FIXED_STUDENT_PASSWORD", "student123")
    hashed_pwd = crypto.hash(fixed_password)

    query = """
        INSERT INTO users (email, password, role)
        VALUES (%s, %s, 'student')
    """

    value = (
        data["email"],
        hashed_pwd
    )

    db.executeQuery(query, value)

    return createResult(
        None,
        "Student user created successfully (default password: student123)"
    )


@usersRouter.route("/setup-admin", methods=["POST"])
def setup_admin():
    email = "admin@gmail.com"
    password = crypto.hash("admin123")

    query = "INSERT INTO users (email, password, role) VALUES (%s, %s, 'admin')"
    db.executeQuery(query, (email, password))

    return createResult(None, "Admin created")


@usersRouter.route('/login', methods=['POST'])
def login():
    query = "SELECT email, password, role FROM users WHERE email = %s"
    result = db.executeQuery(query, (request.json["email"],))

    if not result:
        return createResult("Invalid email or password", None)

    raw_password = request.json["password"]
    db_password = result[0]["password"]
    role = result[0]["role"]

    if not crypto.verify(raw_password, db_password):
        return createResult("Invalid email or password", None)

    token = create_access_token(
        identity=result[0]["email"],
        additional_claims={"role": role},
        expires_delta=False
    )

    return createResult(None, {
        "email": result[0]["email"],
        "role": role,
        "token": token
    })
