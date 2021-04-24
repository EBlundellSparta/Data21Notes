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
        self._time_of_film = {}
        for i in range(number_of_screens):
            self._num_of_screens["Screen " + str(i + 1)] = {}

    def add_film_screen(self, screen_number: int, time_set: str, sel_film: str):
        emp_set = set()
        if sel_film.title() in self._time_of_film.keys():
            for i in self._time_of_film[sel_film.title()]:
                emp_set.add(i)
                emp_set.add(time_set)
        else:
            emp_set.add(time_set)
        self._time_of_film[sel_film.title()] = emp_set
        self._num_of_screens["Screen " + str(screen_number)] = self._time_of_film
        return self._num_of_screens

    def rem_film_screen(self, screen_number: int, rem_time: str, sel_film: str,):
        emp_set = set()
        if sel_film.title() not in self._time_of_film.keys():
            print("This film is not on today!")
        else:
            for i in self._time_of_film[sel_film.title()]:
                if i != rem_time:
                    emp_set.add(i)
            if emp_set == set():
                for key, value in self._num_of_screens["Screen " + str(screen_number)]:
                    if key != sel_film.title():
                        emp_set_2 = set()
                        for i in value:
                            emp_set_2.add(i)
                        self._num_of_screens["Screen " + str(screen_number)] = {key: emp_set_2}
            else:
                self._time_of_film[sel_film.title()] = emp_set
        self._num_of_screens["Screen " + str(screen_number)] = self._time_of_film
        return self._num_of_screens

    def print_film_screen(self, screen_number: int):
        if self._num_of_screens.get("Screen " + str(screen_number)) == set():
            return "No films running at this screen!"
        else:
            return self._num_of_screens.get("Screen " + str(screen_number), "This screen doesn't exist")

loc_1 = Cinema_Location(5)
loc_1.add_film_screen(3, "14:10", "Deadpool")
loc_1.add_film_screen(3, "19:10", "Deadpool")
loc_1.add_film_screen(3, "13:10", "Lion King")
loc_1.add_film_screen(3, "14:05", "Lion King")
loc_1.add_film_screen(3, "19:10", "Lion King")
loc_1.rem_film_screen(3, "14:10", "Deadpool")
loc_1.rem_film_screen(3, "19:10", "Deadpool")
print(loc_1._num_of_screens)

# class Films_At_Time(Cinema_Location):
#
#     def __init__(self, number_of_screens):
#         super().__init__(number_of_screens)
#         self._time_of_films = {}
#
#     def add_film_time(self, sel_film: str, time: "e.g. 14:10"):
#         new_date = datetime.strptime(time, "%H:%M")
#         new_date = "{}:{}".format(new_date.hour, new_date.minute)
#         if sel_film.title() not in self._time_of_films.keys():
#             self._time_of_films[sel_film.title()] = {new_date}
#         else:
#             self._time_of_films[sel_film.title()].add(new_date)

