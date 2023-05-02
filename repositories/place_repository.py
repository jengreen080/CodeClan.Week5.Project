from db.run_sql import run_sql

from models.country import Country
from models.place import Place

import repositories.country_repository as country_repo

def save(place):
    sql = "INSERT INTO places(place_name, country_id, place_description, visited) VALUES (%s, %s, %s, %s) RETURNING place_id"
    values = [place.place_name, place.country.country_id, place.place_description, place.visited]
    results = run_sql(sql, values)
    place_id = results[0]["place_id"]
    place.place_id = place_id
    return place

def delete_all():
    sql = "DELETE FROM places"
    run_sql(sql)

def select_all():
    list_of_places = []

    sql = "SELECT * FROM places"
    results = run_sql(sql)
    
    for row in results:
        # country = Country(row["country_name"], row["continent"], row["country_id"])
        country = country_repo.select(row["country_id"])
        place = Place(row["place_name"], country, row["place_description"], row["visited"], row["place_id"])
        list_of_places.append(place)
    return list_of_places

def select(place_id):
    place = None
    sql = "SELECT * FROM places WHERE id = %s"
    values = [place_id]
    results = run_sql(sql, values)

    if results: 
        result = results[0]
        country = country_repo.select(result["country_id"])
        place = Place(result["place_id"], result["place_name"], country, result["place_description"], result["visited"], result["place_id"])
    return place

def delete(place_id):
    sql = "DELETE FROM places WHERE place_id = %s"
    values = [place_id]
    run_sql(sql, values)