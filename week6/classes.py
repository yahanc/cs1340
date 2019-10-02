from car import Car, Battery

# my_car = Car("bmw", "m3", 2019)
# my_car.get_description()

#
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(70)
        self.__some_variable = 10

    def get_description(self):
        print("This is a electric car")


my_electric_car = ElectricCar("tesla", "model s", 2019)
my_electric_car.battery.describe_battery()
print(my_electric_car._ElectricCar__some_variable)
