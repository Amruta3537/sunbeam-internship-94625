from flask import Flask, request, jsonify

import os
from flask_cors import CORS
from routes.users import usersRouter
from routes.activecourses import activecoursesRouter 
from routes.student import studentRouter
from routes.courses import coursesRouter
from routes.videos import videosRouter
from utils.util import createResult, enableJWT

app = Flask(__name__)
enableJWT(app)

@app.errorhandler(500)
def handle_exception(e):
    err = getattr(e, "original_exception")
    return createResult(error=repr(err), data=None)

app.register_blueprint(usersRouter)
app.register_blueprint(activecoursesRouter)
app.register_blueprint(studentRouter)
app.register_blueprint(coursesRouter)
app.register_blueprint(videosRouter)


CORS(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)