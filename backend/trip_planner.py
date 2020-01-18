from nearby_cities import nearby_airports
from total_ground_cost import total_ground_cost
from trip import Trip


def find_carbon_paths(source, destination, car_mpg):
    start_trips(source, destination, car_mpg)

def start_trips(source, destination, car_mpg):
    src_airports = nearby_airports(source)
    trips = []
    for airport in src_airports:
        ground_paths = total_ground_cost(source, airport, car_mpg)
        trips.append((airport, Trip.CAR), ground_paths[0])
        trips.append((airport, Trip.BUS), ground_paths[1])
        trips.append((airport, Trip.TRAIN), ground_paths[2])
