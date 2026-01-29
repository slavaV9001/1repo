class Address:
    def __init__(self, index, city, street, house, apartament):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartament = apartament

    def get_index(self):
        return self.index

    def get_city(self):
        return self.city

    def get_street(self):
        return self.street

    def get_house(self):
        return self.house

    def get_apartament(self):
        return self.apartament

    def __str__(self):
        return (f"{self.index}",
                f"{self.city},{self.street},{self.house},{self.apartament}")
