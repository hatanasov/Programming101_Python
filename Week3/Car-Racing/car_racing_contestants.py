import json
from car_racing import Car
from car_racing import Driver
from car_racing import Race

def contestants(filename_json):
    with open(filename_json, 'r') as jf:
        loader = json.load(jf)
        contestant = [racer for data in loader.values() for racer in data]
    return contestant


def car_objects(contestants_data):
    cars_obj = []
    for data in contestants_data:
        car = data['car']
        model = data['model']
        max_speed = data['max_speed']
        cars_obj.append(Car(car, model, max_speed))
    return cars_obj


def drivers(contestants_data, cars):
    drivers = []
    for index in range(0, len(cars)):
        drivers.append(Driver(contestants_data[index]['name'], cars[index]))

    return drivers


contestants_data = contestants('cars.json')
cars = car_objects(contestants_data)
drivers = drivers(contestants_data, cars)
raceing_1 = Race(drivers, 0)
print(raceing_1.result())


#
# print(contestants_data)
# # print(sorted(drivers))
# print(cars)
# # for c in drivers:
# #     print(c.name, c.car.max_speed)
# for d in drivers:
#     print(d, d.car.max_speed)
#
#
