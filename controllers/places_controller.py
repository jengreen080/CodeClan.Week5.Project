from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import *
from models.place import *
from console import *
import repositories.country_repository as country_repo
import repositories.place_repository as place_repo

places_blueprint = Blueprint("places", __name__)

@places_blueprint.route("/places/")
def places():
    list_of_places = place_repo.select_all()
    return render_template("places/places_home.jinja", list_of_places = list_of_places)

@places_blueprint.route("/places/<place_id>/delete", methods = ["POST"])
def delete_place(place_id):
    place_repo.delete(place_id)
    return redirect("/places/")
    
@places_blueprint.route("/places/new_place")
def new_place():
    countries = country_repo.select_all()
    return render_template("places/new_place.jinja", countries = countries)

@places_blueprint.route("/places/", methods = ["POST"])
def submit_new_place():
    place_name = request.form['place_name']
    country = country_repo.select(request.form['country'])
    place_description = request.form['place_description']
    if request.form['status'] == "visited":
        status = True
    else:
        status = False
    new_place = Place(place_name, country, place_description, status)
    place_repo.save(new_place)
    return redirect("/places/")



@places_blueprint.route("/places/<place_id>/edit", methods=['GET'])
def edit_a_place(place_id):
    place = place_repo.select(place_id)
    country = country_repo.select_all()
    
    return render_template('/places/edit_place.jinja', country = country, place = place)


@places_blueprint.route("/places/<place_id>", methods=['POST'])
def update_place(place_id):
    name = request.form['place_name']
    country = country_repo.select(place_id)
    description = request.form['country_description']
    visited = request.form['visited']
    place = Place(place_name = name, country = country, description = description, visited = visited)
    country_repo.update(country)
    return redirect('/countries/')
