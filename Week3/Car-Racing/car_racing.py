import random

class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __int__(self):
        return self.max_speed

    def __eq__(self, other):
        if self.max_speed == other.max_speed:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.max_speed > other.max_speed:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.car, self.model)

    def __repr__(self):
        return '{} {}'.format(self.car, self.model)


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return '{}'.format(self.name)


class Race:
    def __init__(self, drivers_list, crash_chance):
        self.drivers_list = drivers_list
        self.crash_chance = crash_chance

    def racing(self, drivers_list, crash_chance):
        score = {}
        if crash_chance == 0:
            sorted_drivers = sorted([(d, d.car.max_speed) for d in self.drivers_list], key=lambda x: x[1], reverse=True)
            top_3_drivers = sorted_drivers[:]
            points = [8, 6, 4]
            zero_points = [0 for i in range(len(sorted_drivers) - points)]
            total_points = points + zero_points
            drivers_points = zip(top_3_drivers, total_points)
            score = {driver[0][0]: driver[1] for driver in drivers_points}
            # score.update(for driver in sorted_drivers )
        elif crash_chance == 1:
            pass
        # for driver in drivers_points:
        #     score.update({driver[0][0]: driver[1]})
        return score

    def result(self):
        score = self.racing(self.drivers_list, self.crash_chance)
        return score


class Championship:
    pass
