class AmazingDog:

    # _is_alive = True -- The underscore at the start makes it hidden (BUT STILL CHANGEABLE)
    # __is_alive = True  -- Double underscore at the start means it cannot be changed as long as it's in
                        # the init method!

    def __init__(self, animal_kind):
        self.animal_kind = animal_kind
        self.bark()   # This happens at the same time
        self.__is_alive = True

    def bark(self):
        return "woof!"

    def set_is_alive(self, alive_status):
        self.__is_alive = alive_status

    def get_is_alive(self):
        return self.__is_alive

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

