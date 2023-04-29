class Place:

    def __init__(self, place_name, country, place_description, status, place_id = None):
        
        self.place_name = place_name
        self.country = country
        self.status = status
        self.place_description = place_description
        self.place_id = place_id
