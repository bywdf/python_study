class Car():
   
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = str(self.year) + " " +self.make + " " + self.model
        return long_name


class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size = 70

    def describe_battery(self):
        print(f"this car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

            message = "this car can go approximately" + str(range)
            message += "miles on a full charge"
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()




mycar = ElectricCar('tesla', 'model s', 2016)
mycar.battery.get_range()
mycar.battery.describe_battery()
mycar.battery.get_range()
mycar.battery.describe_battery()