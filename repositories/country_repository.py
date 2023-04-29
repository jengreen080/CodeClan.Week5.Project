from db.run_sql import run_sql

from models.country import Country
# from models.place import Place

# import repositories.place_repository as place_repo
def save(country):
    sql = "INSERT INTO countries(country_name, continent) VALUES (%s, %s) RETURNING *"
    values = [country.country_name, country.continent]
    results = run_sql(sql, values)
    country_id = results[0]["country_id"]
    country.country_id = country_id
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)