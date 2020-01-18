from nearby_cities import nearby_airports
from total_ground_cost import total_ground_cost
from total_air_cost import total_air_cost
from trip import Trip, TripStep


def find_carbon_paths(source, destination, car_mpg):
    start_trips(source, destination, car_mpg)

def start_trips(source, destination, car_mpg):
    src_airports = nearby_airports(source)
    print("Airports: ", src_airports)
    trips = []
    for airport in src_airports:
        ground_paths = total_ground_cost(source, airport, car_mpg)

        car_trip = Trip(source)
        car_costs = ground_paths[0]
        car_trip.cities.append(TripStep(airport, TripStep.CAR, car_costs[0], car_costs[1], car_costs[2]))
        trips.append(car_trip)
        
        bus_trip = Trip(source)
        bus_costs = ground_paths[1]
        bus_trip.cities.append(TripStep(airport, TripStep.BUS, bus_costs[0], bus_costs[1], bus_costs[2]))
        trips.append(bus_trip)

        train_trip = Trip(source)
        train_costs = ground_paths[1]
        train_trip.cities.append(TripStep(airport, TripStep.TRAIN, train_costs[0], train_costs[1], train_costs[2]))
        trips.append(train_trip)
        
    

find_carbon_paths("Tucson", "Denver", 35)
