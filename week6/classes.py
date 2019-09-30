class Car():
    """Description"""

    def __init__(self, make, model, year):

        self.car_make = make
        self.model = model
        self.year = year
        self.long_name = str(self.year) + " " + str(self.model)

    def get_description(self):
        # long_name = str(self.year) + " " + str(self.model)
        print(self.long_name)

# my_car = Car("bmw", "m3", 2019)
# my_car.get_description()

class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a  battery size " +  str(self.battery_size) + "-kwh ")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(70)

    def get_description(self):
        print("This is a electric car")


my_electric_car = ElectricCar("tesla", "model s", 2019)
my_electric_car.battery.describe_battery()