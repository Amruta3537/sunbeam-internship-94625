from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

def getConnection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="manager",
        database="institute_management_db",
        use_pure=True
    )

def executeQuery():
    with getConnection() as con:
        with con.cursor(dictionary=True) as cur:
            cur.execute()
            if cur.description:
                return cur.fetchall()
                # SELECT query yields list of dicts
            else:
                con.commit()
                return {"affectedRows": cur.rowcount}
            

app = Flask(__name__)
CORS(app)


# Get All Courses
@app.route("/course/all-courses", methods=["GET"])
def get_all_courses():
    start_date = request.args.get("startDate")
    end_date = request.args.get("endDate")

    conn = getConnection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM courses"
    values = []

    if start_date and end_date:
        query += " WHERE start_date >= %s AND end_date <= %s"
        values = [start_date, end_date]

    cursor.execute(query, values)
    courses = cursor.fetchall()

    conn.close()
    return jsonify(courses)


# Add Course
@app.route("/course/add", methods=["POST"])
def add_course():
    data = request.json

    conn = getConnection()
    cursor = conn.cursor()

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

    cursor.execute(query, values)
    conn.commit()
    conn.close()

    return jsonify({"message": "Course added successfully"})


# Update Course
@app.route("/course/update/<int:courseId>", methods=["PUT"])
def update_course(courseId):
    data = request.json

    conn = getConnection()
    cursor = conn.cursor()

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

    cursor.execute(query, values)
    conn.commit()
    conn.close()

    return jsonify({"message": "Course updated successfully"})


# Delete Course
@app.route("/course/delete/<int:courseId>", methods=["DELETE"])
def delete_course(courseId):
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM courses WHERE course_id=%s", (courseId,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Course deleted successfully"})





if __name__ == "__main__":
    app.run(debug=True)


