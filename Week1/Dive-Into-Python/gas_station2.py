'''Optimal variant'''


def gas_stations(distance, tank_size, stations):
    res = []
    curr_tank_size = tank_size
    last_station = 0
    for station in stations + [distance]:
        station_dist = station - last_station
        if station_dist <= curr_tank_size:
            curr_tank_size -= station_dist
        else:
            res.append(last_station)
            curr_tank_size = tank_size - station_dist
        last_station = station
    return res


print(gas_stations(320, 90, [50, 80, 90, 160, 180, 270]))
print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))

