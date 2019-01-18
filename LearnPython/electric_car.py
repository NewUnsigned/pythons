from car import Car


class Battery:

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has al " + str(self.battery_size) + "-KWH battery")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #     print("This car has al " + str(self.battery_size) + "-KWH battery")

    def fill_gas_tank(self):
        print('This car dose not need a gas tank!')
