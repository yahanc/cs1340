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


class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a  battery size " +  str(self.battery_size) + "-kwh ")
