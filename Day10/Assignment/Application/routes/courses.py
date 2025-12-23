from flask import Flask, jsonify, request, Blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
import utils.db as db
from utils.util import createResult


coursesRouter = Blueprint("courses", __name__, url_prefix="/courses")


# Get All Courses
@coursesRouter.route("/all-courses", methods=["GET"])
@jwt_required()
def get_all_courses():
    start_date = request.args.get("startDate")
    end_date = request.args.get("endDate")

    query = "SELECT * FROM courses"
    values = []

    if start_date and end_date:
        query += " WHERE start_date >= %s AND end_date <= %s"
        values = [start_date, end_date]

    result = db.executeQuery(query, values)
    return createResult(error=None, data=result)


# Add Course
@coursesRouter.route("/add", methods=["POST"])
@jwt_required()
def add_course():
    data = request.json

    query = """
    INSERT INTO courses
    (course_name, description, fees, start_date, end_date, video_expire_days)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        data["course_name"],
        data["description"],
        data["fees"],
        data["start_date"],
        data["end_date"],
        data["video_expire_days"]
    )


    result = db.executeQuery(query,values)

    return createResult(None, result)


# Update Course
@coursesRouter.route("/update/<int:courseId>", methods=["PUT"])
@jwt_required()
def update_course(courseId):
    data = request.json

    query = """
    UPDATE courses SET
    course_name=%s,
    description=%s,
    fees=%s,
    start_date=%s,
    end_date=%s,
    video_expire_days=%s
    WHERE course_id=%s
    """

    values = (
        data["course_name"],
        data["description"],
        data["fees"],
        data["start_date"],
        data["end_date"],
        data["video_expire_days"],
        courseId
    )


    result = db.executeQuery(query,values)

    return createResult(None, result)


# Delete Course
@coursesRouter.route("/delete/<int:courseId>", methods=["DELETE"])
@jwt_required()
def delete_course(courseId):

    query = "DELETE FROM courses WHERE course_id=%s "

    values = (courseId, )

    result = db.executeQuery(query,values)

    return createResult(None, result)
