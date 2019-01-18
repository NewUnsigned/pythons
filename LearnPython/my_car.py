from car import Car
from electric_car import ElectricCar

my_new_car = Car('auto', 'a4', 2016)
my_new_car.fill_gas_tank()
print(my_new_car.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
