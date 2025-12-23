from flask import Flask, jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
import utils.db as db
from utils.util import createResult
# from passlib.hash import sha256_crypt
# crypto = sha256_crypt

from passlib.hash import sha256_crypt
crypto = sha256_crypt



studentRouter = Blueprint("student", __name__, url_prefix="/student")


@studentRouter.route("/register-to-course", methods = ['POST'])
def reg_course() :
    data = request.json

    query = """insert into students(course_id, name, email, mobile_no)
       values(%s, %s, %s, %s)"""
    
    values = (
        data["course_id"],
        data["name"],
        data["email"],
        data["mobile_no"]
    )

    result = db.executeQuery(query , values)

    return createResult(None, result)


@studentRouter.route("/change-password", methods = ['PUT'], endpoint='change_password')
@jwt_required()
def change_pass() :
    data = request.json
    email = get_jwt_identity()

    new_password = data.get("newPassword")
    confirm_password = data.get("confirmPassword")

    if not new_password or not confirm_password:
        return createResult("Password fields cannot be empty", None)

    if new_password != confirm_password:
        return createResult("New password and confirm password do not match", None)

    encrypted_password = crypto.hash(new_password)

    query = "UPDATE users SET password = %s WHERE email = %s"
    result = db.executeQuery(query, (encrypted_password, email))

    if result["affectedRows"] == 0:
        return createResult("Password update failed", None)

    return createResult(None, "Password changed successfully")
   


@studentRouter.route("/my-courses", methods = ['GET'])
@jwt_required()
def get_my_courses():
    
    email = get_jwt_identity()


    query = """
        SELECT c.course_id, c.course_name
        FROM courses c
        JOIN students sc ON c.course_id = sc.course_id
        WHERE sc.email = %s
    """
    courses = db.executeQuery(query, (email,))

    return createResult(None, courses)


@studentRouter.route("/my_courses_with_videos", methods = ['GET'])
@jwt_required()
def get_my_courses_with_videos():
    email = get_jwt_identity()

    query = """
        SELECT 
            c.course_id,
            c.course_name,
            v.video_id,
            v.title,
            v.youtube_url
        FROM students sc
        JOIN courses c ON sc.course_id = c.course_id
        LEFT JOIN videos v ON c.course_id = v.course_id
        WHERE sc.email = %s
         
    """
    result = db.executeQuery(query, (email,))

    return createResult(None, result)
