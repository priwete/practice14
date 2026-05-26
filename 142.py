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
    def __init__(self, restaurant_name, cuisine_type, flavours, type, location, work_time):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
        self.location = location
        self.work_time = work_time
        self.typesofice = {"на палочке": [], "фруктовый лёд": []}
    def flavours_list(self):
        for i in self.flavours:
            print(i)
    def flavours_add(self, flavour):
        if flavour not in self.flavours:
            self.flavours.append(flavour)
    def flavours_remove(self, flavour):
        if flavour in self.flavours:
            self.flavours.remove(flavour)
    def flavours_check(self, flavour):
        if flavour in self.flavours:
            print("Сорт", flavour, "имеется")
        else:
            print("такого не продаём")
    def flavour_addbytype(self, type, flavours):
        if type in self.typesofice and flavours not in self.typesofice[type]:
            self.typesofice[type].append(flavours)
    def flavour_removebytype(self, type, flavours):
        if type in self.typesofice and flavours in self.typesofice[type]:
            self.typesofice[type].remove(flavours)
    def menu(self):
        for i in self.typesofice:
            print(i, self.typesofice[i])
Morozhenoe = IceCreamStand("Мороженка", "русская", ["шоколадное", "ванильное", "пломбир"], ["на палочке", "фруктовый лёд"], "санкт-петербург", "с 10:00 до 22:00")

Morozhenoe.flavours_add("клубничное")
Morozhenoe.flavours_check("ванильное")
Morozhenoe.flavours_remove("шоколадное")
Morozhenoe.flavours_list()
Morozhenoe.flavour_addbytype("на палочке", ["клубника", "банан", "шоколад"])
Morozhenoe.flavour_addbytype("фруктовый лёд", ["клубника", "банан", "шоколад"])
Morozhenoe.flavour_removebytype("на палочке", "банан")
Morozhenoe.menu()
