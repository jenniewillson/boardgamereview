from flask import render_template
from taskmanager import app, db


@app.routes("/")
def home():
    return render_template("base.html")