# Create a car class. Give the vehicle a maximum speed, and keep track of the
# current speed of the vehicle. It doesn't make sense for the speed to be adjusted directly,
# so put an underscore in front of it and implement a speed getter as well as accelerate and brake
# setter methods that change the speed in a logical way

class Car:
    def __init__(self, current_speed: int = 0 , max_speed: int = 120):
        self.__curr_speed = int(current_speed)
        self.max_speed = int(max_speed)

    def current_speed(self):
        return self.__curr_speed

    def accelerate(self, speed_increase: int):
        new_speed = self.__curr_speed + speed_increase
        if new_speed > self.max_speed:
            self.__curr_speed = self.max_speed
            print("This cannot be true as above the max speed")
        else:
            self.__curr_speed = new_speed

    def brake(self, brake_set: int):
        n_speed = self.__curr_speed - int(brake_set)
        if n_speed <= 0:
            n_speed = 0
            self.__curr_speed = n_speed
            print("This cannot be true as below 0mph")
        else:
            self.__curr_speed = n_speed

example_1 = Car(50, 100)
print(example_1.current_speed())
example_1.accelerate(40)
print(example_1.current_speed())
example_1.brake(30)
print(example_1.current_speed())
example_1.accelerate(50)
print(example_1.current_speed())