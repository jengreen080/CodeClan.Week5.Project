from flask import render_template, request, redirect
from flask import Blueprint
from models.country import *
from models.place import *
from console import *
import repositories.country_repository as country_repo
import repositories.place_repository as place_repo

travel_blueprint = Blueprint("travel", __name__)

@travel_blueprint.route("/home/")
def places():
    list_of_places = place_repo.select_all()
    return render_template("home.jinja", list_of_places = list_of_places)

@travel_blueprint.route("/home/<place_id>/delete", methods = ["POST"])
def delete_place(place_id):
    place_repo.delete(place_id)
    return redirect("/home/")
    


# @travel_blueprint.route("/my_bucket_list/<id>", methods = ["GET"])
# def show_bucket_list(place_id):
#     bucket_list = place_repo.select(place_id)
#     return render_template("my_bucket_list.jinja", places_to_display = bucket_list)
