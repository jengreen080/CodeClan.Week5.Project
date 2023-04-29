from flask import render_template, request, redirect
from app import app
from models.country import *
from models.place import *
from console import *

@app.route("/")
def index():
    return render_template("home.jinja", title = "Home", place = places)