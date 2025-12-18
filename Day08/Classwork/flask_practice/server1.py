from flask import Flask

server = Flask(__name__)

@server.get('/')
def homepage():
    return "This is homepage"

@server.get('/welcome')
def welcome():
    return "<html><body><h1>Welcome to Student Management System</h1></body></html>"

server.run()
