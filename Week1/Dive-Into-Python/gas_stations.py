def get_stations_distance(list_of_distance, final_destination):
    """Get distances between stations"""
    stations_distance = []
    for index in range(0, len(list_of_distance) - 1):
        if index == 0:
            # distance from 0 to first station
            stations_distance.append(list_of_distance[index])
        distance = list_of_distance[index + 1] - list_of_distance[index]
        stations_distance.append(distance)

    # distance from last station to final destination
    stations_distance.append(final_destination - list_of_distance[-1])
    return stations_distance


def gas_stations(distance, tank_size, stations):
    station_distances = get_stations_distance(stations, distance)
    result = []
    index = 0
    traveled_km = 0
    while index < len(station_distances) - 1:
        first_station = station_distances[index]
        second_station = station_distances[index + 1]
        if traveled_km == 0:
            if first_station + second_station <= tank_size:
                # travel around the 'first station'
                traveled_km += first_station + second_station
            else:
                # refueling
                result.append(stations[index])
                traveled_km = 0
        else:
            if traveled_km + second_station > tank_size:
                # refueling
                result.append(stations[index])
                traveled_km = 0
            else:
                traveled_km += second_station

        index += 1

    return result


# print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
# print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
print(gas_stations(320, 90, [50, 80, 90, 160, 180, 270]))
