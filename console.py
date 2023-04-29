from models.country import Country
from models.place import Place

import repositories.country_repository as country_repo
import repositories.place_repository as place_repo

country_repo.delete_all()
place_repo.delete_all()

brazil = Country("Brazil", "South America")
country_repo.save(brazil)
croatia = Country("Croatia", "Europe")
country_repo.save(croatia)
canada = Country("Canada", "North America")
country_repo.save(canada)
japan = Country("Japan", "Asia")
country_repo.save(japan)

banff = Place ("Banff", canada, "the most stunning place in the world", "been there, done that")
place_repo.save(banff)
rio = Place("Rio de Janeiro", brazil, "carnival looks cool", "on the bucket list")
place_repo.save(rio)
plitvice_lakes = Place("Plitvice lakes", croatia, "looks so beautiful", "still to visit")
place_repo.save(plitvice_lakes)





