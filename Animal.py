class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("one breath in and one out")

    def eat(self):
        print("nom nom nom")

    def moving(self):
        print("forwards, backwards and side to side")

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True

    def use_venom(self):
        print("If I have venom, I'm going to use it")

    def moving(self):
        print("Slither like a snake")

    def __repr__(self):
        return f"This is a reptile"


Bob = Reptile()
