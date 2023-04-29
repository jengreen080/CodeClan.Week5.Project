from db.run_sql import run_sql

from models.country import Country
from models.place import Place

# import repositories.country_repository as country_repo

def save(place):
    sql = "INSERT INTO places(place_name, country, place_description, status) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [place.place_name, place.country.country_id, place.place_description, place.status]
    results = run_sql(sql, values)
    place_id = results[0]["place_id"]
    place.place_id = place_id
    return place

def delete_all():
    sql = "DELETE FROM places"
    run_sql(sql)