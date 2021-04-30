# class AmazingDog:
#
#     # _is_alive = True -- The underscore at the start makes it hidden (BUT STILL CHANGEABLE)
#     # __is_alive = True  -- Double underscore at the start means it cannot be changed as long as it's in
#                         # the init method!
#
#     def __init__(self, animal_kind):
#         self.animal_kind = animal_kind
#         self.bark()   # This happens at the same time
#         self.__is_alive = True
#
#      def __repr__(self):                 Use this to represent the class (could use __str__ method)
#         return f"This is a dog"
#
#     def bark(self):
#         return "woof!"
#
#     def set_is_alive(self, alive_status):
#         self.__is_alive = alive_status
#
#     def get_is_alive(self):
#         return self.__is_alive

# Bob = AmazingDog()  -- Need to create an instance of the class
# Bob.animal_kind = "dolphin"
# print(Bob.animal_kind)
#
# Bob = AmazingDog("canine")
# Sue = AmazingDog("dolphin")
# print(Bob.animal_kind)
# print(Sue.animal_kind)
#
# Bob = AmazingDog("canine")
# Bob.set_is_alive(False)
# print(Bob.get_is_alive())

# FOUR PILLARS OF OOP

# Abstraction - User is kept unaware of the how the method actually works, just worried about the end result

# Encapsulation - Some parts of the class is kept hidden from the user (using __)

# Inheritance - Lets one object acquire the properties and methods from another object

# Polymorphism - "The condition of occuring in several different forms" (i.e. using 4 as default number of
#                                                                        legs for an animal)

#  __name__ = __main__ for the module your currently running i.e. __name__ of this module is classes
#                                                                   (if not on file)
# if you want to use a function/class from a different module remember above fact