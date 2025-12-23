
from flask import Blueprint, jsonify
import utils.db as db
from utils.util import createResult

activecoursesRouter = Blueprint("activecourses", __name__, url_prefix="/activecourses")

@activecoursesRouter.route('/all-active-courses', methods=['GET'])
def get_all_active_courses():
    """
    Get all active courses where current date is between start_date and end_date
    """
    query = """
        SELECT *
        FROM courses
        WHERE CURDATE() BETWEEN start_date AND end_date;
    """
    data = db.executeQuery(query, ())
    return createResult(None, data)