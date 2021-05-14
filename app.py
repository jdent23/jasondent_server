#!/usr/bin/env python3

from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def landing():
    return redirect("http://jasondent.net:30000")

@app.route("/admin")
def hello_world():
    print("Site pinged")
    return "Hello world"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
