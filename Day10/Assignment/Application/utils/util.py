
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
import mysql.connector
import os
from flask_jwt_extended import (JWTManager)

from passlib.hash import sha256_crypt
crypto = sha256_crypt

def createResult(error, data):
    if data:
        return jsonify(status="success", data=data)
    else:
        return jsonify(status="error", error=error)
    

def enableJWT(app):
    jwt_secret = os.getenv("MY_JWT_SECRET")
    app.config["JWT_SECRET_KEY"] = jwt_secret
    jwt_mgr = JWTManager(app)

    @jwt_mgr.invalid_token_loader
    def invalid_token_handler(e):
        return createResult("Invalid JWT Token", None)

    @jwt_mgr.unauthorized_loader
    def unauthorized_handler(e):
        return createResult("JWT Token Absent", None)
