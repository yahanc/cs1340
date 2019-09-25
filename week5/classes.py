class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age, weight):

        """Initialize name and age attributes """
        self.name = name
        self.age = age
        self.weight = weight

    def sit(self):
        """Simulating a dog sitting"""
        # print(self.weight)
        print(self.name + " is sitting now")

    def roll_over(self):
        print(self.name + " is rolled over")


# my_dog = Dog("shadow", 6, 100)
# my_dog.sit()
# my_dog.roll_over()
#
# # print(my_dog.name, my_dog.age)
#
# your_dog = Dog("lucy", 3, 60)
# your_dog.sit()
# your_dog.roll_over()


class Car():
    """A simple attempt model a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        print(long_name)

    def get_odometer_reading(self):
        return self.odometer_reading

    def update_odometer_reading(self, mileage):
        if mileage < self.odometer_reading:
            print("mileage can not be less than the original value")
        elif mileage < 0:
            print("mileage can not be less than 0")
        else:
            self.odometer_reading = mileage

my_car = Car("bmw", "m3", 2016)
my_car.get_descriptive_name()

print(my_car.get_odometer_reading())
my_car.update_odometer_reading(1000)
print(my_car.get_odometer_reading())

my_car.update_odometer_reading(-500)
