from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import *
from models.place import *
from console import *
import repositories.country_repository as country_repo
import repositories.place_repository as place_repo

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries/")
def show_all_countries():
    list_of_countries = country_repo.select_all()
    return render_template("countries/countries_home.jinja", list_of_countries = list_of_countries)

@countries_blueprint.route("/places/new_country")
def new_country():
    countries = country_repo.select_all()
    return render_template("countries/new_country.jinja", countries = countries)

@countries_blueprint.route("/countries/", methods = ["POST"])
def submit_new_country():
    country_name = request.form['country_name']
    continent = request.form['continent']
    new_country = Country(country_name, continent)
    country_repo.save(new_country)
    return redirect("/countries/")

@countries_blueprint.route("/countries/<country_id>/delete", methods = ["POST"])
def delete_country(country_id):
    country_repo.delete(country_id)
    return redirect("/countries/")

# @countries_blueprint.route("/countries/<country_id>/edit", methods=['GET'])
# def edit_a_country(country_id):
#     place = place_repo.select_all()
#     country = country_repo.select(country_id)
#     return render_template('countries/edit.jinja', country = country, place = place)

# @countries_blueprint.route("/countries/<country_id>", methods=['POST'])
# def update_country(country_id):
#     country_name = request.form['country_name']
#     continent = request.form['continent']
#     country = Country(country_name, continent, country_id)
#     country_repo.update(country)
#     return redirect('/countries')