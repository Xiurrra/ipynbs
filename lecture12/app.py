#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import flask
import sqlite3

app = flask.Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
        <body>
        This is my first flask app
        </body>
    </html>"""
@app.route("/form")
def form():
    return flask.render_template("form.html")

@app.route("/hello/<name>")
def hello(name):
    g = globals()
    a = "abc"
    return flask.render_template("hello.html", g=g, a=a)

@app.route("/result", methods=['POST'])
def result():
    return f"""
    <html>
        <body>
            hello, {flask.request.form['fname']}
        </body>
    </html>"""
