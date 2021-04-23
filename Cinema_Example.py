# name = input("Please input your name: ")
# age = input("Please input your age as an integer: ")
#
# while name.isalpha() is False:
#     name = input("This is an invalid name, please type again (for example Ed):  ")
#
# while age.isnumeric() is False:
#     age = input("This is an invalid age, please type your age as an integer (for example 20 "
#                 "if you're twenty year's old):  ")
#
# if int(age) < 12:
#     supervised = input("Are you alone?  ")
#     yes = ['yes', 'y', 'yep', 'yess', 'indeed', 'yeah']
#     no = ['no', 'nope', 'naa', 'n', 'noo']
#     while supervised.lower() not in yes and supervised.lower() not in no:
#         supervised = input("Please type yes or no:  ")
#     if supervised.lower() in yes:
#         print(f"Hello {name.capitalize()}, you can go and see any PG or U or 12A films "
#             f"provided that's fine with whoever is supervising you.")
#     else:
#         print(f"Sorry {name.capitalize()}, you are too young and cannot see any films :(")
# elif 12 <= int(age) < 15:
#     print(f"Thank you {name.capitalize()}, you can only see films rated up to 12A")
# elif 15 <= int(age) < 18:
#     print(f"Thank you {name.capitalize()}, you can only see films rated up to 15")
# else:
#     print(f"Congratulations {name.capitalize()}, you are officially an adult, good luck! "
#             f"But the good news is you can see whichever film you want!")
# print("Hope you have a lovely day!")

class Cinema:

    def __init__(self):
        self.films_pg = []
        self.films_12a = []
        self.films_15 = []
        self.films_18 = []

    def add_films_pg(self, new_films: list):
        self.films_pg += new_films
        return self.films_pg

    def rem_films_pg(self, deleted_films: list):
        for i in deleted_films:
            if i in self.films_pg:
                self.films_pg.remove(i)
        return self.films_pg

    def add_films_12a(self, new_films: list):
        self.films_12a += new_films
        return self.films_12a

    def rem_films_12a(self, deleted_films: list):
        for i in deleted_films:
            if i in self.films_pg:
                self.films_12a.remove(i)
        return self.films_12a

    def add_films_15(self, new_films: list):
        self.films_15 += new_films
        return self.films_15

    def rem_films_15(self, deleted_films: list):
        for i in deleted_films:
            if i in self.films_15:
                self.films_15.remove(i)
        return self.films_15

    def add_films_18(self, new_films: list):
        self.films_18 += new_films
        return self.films_18

    def rem_films_18(self, deleted_films: list):
        for i in deleted_films:
            if i in self.films_18:
                self.films_18.remove(i)
        return self.films_18


class Cinema_Location(Cinema):

    def __init__(self, number_of_screens):
        super().__init__()
        self._num_of_screens = {}
        for i in range(number_of_screens):
            self._num_of_screens["Screen " + str(i + 1)] = None

    def add_film_screen(self, screen_number, sel_film):
        self._num_of_screens[screen_number] = sel_film
        return self._num_of_screens

    def rem_film_screen(self, screen_number):
        self._num_of_screens[screen_number] = None
        return self._num_of_screens

loc_1 = Cinema_Location(10)
print(loc_1._num_of_screens)
print(loc_1.add_film_screen("Screen 4", "Jurassic Park"))