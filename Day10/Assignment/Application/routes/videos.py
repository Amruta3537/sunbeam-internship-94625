# from flask import Flask, jsonify, request, Blueprint
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
# import utils.db as db
# from utils.util import createResult


# videosRouter = Blueprint("videos", __name__, url_prefix="/videos")


# @videosRouter.route("/video/all-videos", methods=["GET"])
# @jwt_required
# def get_all_videos():
#     course_id = request.args.get("course_id")

#     if course_id:
#         query = "SELECT * FROM videos WHERE course_id = %s"
#         values = []
#         result = db.executeQuery(query, (course_id,))
#     else:
#         query = "SELECT * FROM videos"
#         result = db.executeQuery(query, values)

#     return createResult(error=None, data=result)
    



# @videosRouter.route("/video/add/", methods=["POST"])
# @jwt_required
# def add_video():
#     data = request.json

#     query = """
#     INSERT INTO videos (course_id, title, youtube_url, description)
#     VALUES (%s, %s, %s, %s)
#     """

#     values = (
#         data["course_id"],
#         data["title"],
#         data["youtube_url"],
#         data["description"]
#     )
#     result = db.executeQuery(query,values)


#     return createResult(error=None, data=result)
    


# @videosRouter.route("/video/update/<int:video_id>", methods=["PUT"])
# @jwt_required
# def update_video(video_id):
#     data = request.json

#     query = """
#     UPDATE videos
#     SET course_id=%s, title=%s, youtube_url=%s, description=%s
#     WHERE video_id=%s
#     """

#     values= (
#         data["course_id"],
#         data["title"],
#         data["youtube_url"],
#         data["description"],
#         video_id
#     )

#     result = db.executeQuery(query,values)
#     return createResult(error=None, data=result)

    
# @videosRouter.route("/video/delete/<int:video_id>", methods=["DELETE"])
# def delete_video(video_id):

#     query = "DELETE FROM videos WHERE video_id = %s"

#     values = (video_id,)

#     result = db.executeQuery(query,values)

#     return createResult(error=None, data=result)



from flask import Flask, jsonify, request, Blueprint
# functools import is not needed if you use the endpoint argument in the route
# from functools import wraps 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
import utils.db as db
from utils.util import createResult


videosRouter = Blueprint("videos", __name__, url_prefix="/videos")


@videosRouter.route("/all-videos", methods=["GET"], endpoint="get_all_videos")
@jwt_required()
def get_all_videos():
    course_id = request.args.get("course_id")

    if course_id:
        query = "SELECT * FROM videos WHERE course_id = %s"
        result = db.executeQuery(query, (course_id,))
    else:
        query = "SELECT * FROM videos"
        result = db.executeQuery(query,())

    return createResult(error=None, data=result)

    


@videosRouter.route("/add", methods=["POST"], endpoint='add_video')
@jwt_required()
def add_video():
    data = request.json

    query = """
    INSERT INTO videos (course_id, title, youtube_url, description)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        data["course_id"],
        data["title"],
        data["youtube_url"],
        data["description"]
    )
    result = db.executeQuery(query,values)


    return createResult(error=None, data=result)
    


@videosRouter.route("/update/<int:video_id>", methods=["PUT"], endpoint='update_video')
@jwt_required()
def update_video(video_id):
    data = request.json

    query = """
    UPDATE videos
    SET course_id=%s, title=%s, youtube_url=%s, description=%s
    WHERE video_id=%s
    """

    values= (
        data["course_id"],
        data["title"],
        data["youtube_url"],
        data["description"],
        video_id
    )

    result = db.executeQuery(query,values)
    return createResult(error=None, data=result)

    
@videosRouter.route("/delete/<int:video_id>", methods=["DELETE"], endpoint='delete_video')
@jwt_required() # Added jwt_required here assuming it was intended
def delete_video(video_id):

    query = "DELETE FROM videos WHERE video_id = %s"

    values = (video_id,)

    result = db.executeQuery(query,values)

    return createResult(error=None, data=result)
