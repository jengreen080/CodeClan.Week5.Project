from db.run_sql import run_sql

from models.country import Country
# from models.place import Place

# import repositories.place_repository as place_repo
def save(country):
    sql = "INSERT INTO countries (country_name, continent) VALUES (%s, %s) RETURNING country_id"
    values = [country.country_name, country.continent]
    results = run_sql(sql, values)
    country_id = results[0]["country_id"]
    country.country_id = country_id
    return country


def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:

        country = Country(row["country_name"], row["continent"], row["country_id"])
        countries.append(country)
    return countries



def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def select(country_id):
    country = None
    sql = "SELECT * FROM countries WHERE country_id = %s"
    values = [country_id]
    results = run_sql(sql, values)
    
    # country = Country(country_name = results["country_name"], continent = results["continent"], country_id = results["country_id"])
    # print(sql,values, resl)
    # return country
    if results: 
        result = results[0]
        country = Country(result["country_name"], result["continent"], country_id)
    return country


# def save(country):
#     sql = "INSERT INTO countries(country_name, continent) VALUES (%s, %s) RETURNING *"
#     values = [country.country_name, country.continent]
#     results = run_sql(sql, values)
#     country_id = results[0]["country_id"]
#     country.country_id = country_id
#     return country



def delete(country_id):
    sql = "DELETE FROM countries WHERE country_id = %s"
    values = [country_id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET (country_name, continent) = (%s, %s) WHERE country_id = %s"
    values = [country.country_name, country.continent, country.country_id]
    run_sql(sql, values)
