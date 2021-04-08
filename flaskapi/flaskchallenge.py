#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask, redirect, url_for, render_template, request, session

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)
app.secret_key = "any random string"

@app.route("/", methods = ["POST", "GET"])
def hello_world():
    groups = [{"hostname": "hostA", "ip": "192.168.30.22", "fqdn": "hostA.localdomain"},{"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},{"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]
    if request.method == "POST":
        if request.form.get("hostname") and request.form.get("ip") and request.form.get("fqdn"):
            groups.append({"hostname": request.form.get("hostname"), "ip": request.form.get("ip"), "fqdn": request.form.get("fqdn")})
            return render_template("challenge.html", groups=groups)
    else:
           return render_template("challenge.html", groups=groups)

if __name__ == "__main__":
   app.run(host="localhost", port=2224) # runs the application
