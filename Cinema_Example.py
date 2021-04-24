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

from datetime import datetime

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
            self._num_of_screens["Screen " + str(i + 1)] = set()

    def add_film_screen(self, screen_number: int, sel_film: str):
        self._num_of_screens["Screen " + str(screen_number)].add(sel_film)
        return self._num_of_screens

    def rem_film_screen(self, screen_number: int, sel_film: str):
        temp_set = set()
        for i in self._num_of_screens.get("Screen " + str(screen_number)):
            if i.lower() != sel_film.lower():
                temp_set.add(i)
        self._num_of_screens["Screen " + str(screen_number)] = temp_set
        return self._num_of_screens

    def print_film_screen(self, screen_number: int):
        if self._num_of_screens.get("Screen " + str(screen_number)) == set():
            return "No films running at this screen!"
        else:
            return self._num_of_screens.get("Screen " + str(screen_number), "This screen doesn't exist")

loc_1 = Cinema_Location(5)

class Films_At_Time(Cinema_Location):

    def __init__(self, number_of_screens):
        super().__init__(number_of_screens)
        self._time_of_films = {}

    def add_film_time(self, sel_film: str, time: "e.g. 14:10"):
        new_date = datetime.strptime(time, "%H:%M")
        new_date = "{}:{}".format(new_date.hour, new_date.minute)
        if sel_film.title() not in self._time_of_films.keys():
            self._time_of_films[sel_film.title()] = {new_date}
        else:
            self._time_of_films[sel_film.title()].add(new_date)

loc_1_times = Films_At_Time(5)
loc_1_times.add_film_time("Deadpool", "14:10")
loc_1_times.add_film_time("Deadpool", "14:50")
loc_1_times.add_film_time("the lion the witch and the wardrobe", "13:50")
print(loc_1_times._time_of_films)