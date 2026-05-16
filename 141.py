from pydoc import describe

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
        print(self.rating)
    def open_restaurant(self):
        print(self.restaurant_name, " открыт!!!!")
    def update_rating(self):
        print(self.rating)
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
    def flavours_list(self):
        for i in self.flavours:
            print(i)
Morozhenoe = IceCreamStand("Мороженка", "русская", ["шоколадное", "ванильное", "пломбир"])
Morozhenoe.flavours_list()