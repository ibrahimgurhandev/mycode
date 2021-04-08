#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask, redirect, url_for

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_world():
   return "Hello World"


@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hello {guesty} Guest"
    #V2 FORMATTER - return "Hello {} Guest".format(guesty)
    #OLD FORMATTER - return "Hello %s as Guest" % guesty

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/user/<name>")
def hello_user(name):
    ## if you go to hello_user with a value of admin
    if name =="admin":
        # return a 302 response to redirect to /admin
        return redirect(url_for("hello_admin"))
    else:
        # return a 302 response to redirect to /guest/<guesty>
        return redirect(url_for("hello_guest",guesty = name))

if __name__ == "__main__":
   app.run(host="localhost", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
