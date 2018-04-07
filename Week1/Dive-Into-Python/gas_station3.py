def gas_stations(distance, tank_size, stations):
    result = []
    current_tank_size = tank_size
    last_station = 0
    traveled_km = 0
    for station in stations + [distance]:
        station_dist = station - last_station
        if traveled_km == 0:
            if station_dist <= current_tank_size:
                current_tank_size -= station_dist
                traveled_km += station_dist
            else:
                result.append(last_station)
                current_tank_size = tank_size - station_dist
                traveled_km = 0
        else:
            if station_dist > current_tank_size:
                result.append(last_station)
                current_tank_size = tank_size - station_dist
                traveled_km = 0
            else:
                current_tank_size -= station_dist
                traveled_km += station_dist
        last_station = station
    return result


print(gas_stations(320, 90, [50, 80, 90, 160, 180, 270]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
