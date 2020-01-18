from nearby_cities import nearby_airports
from total_ground_cost import total_ground_cost
from total_air_cost import total_air_cost
from trip import Trip, TripStep
from copy import deepcopy


def find_carbon_paths(source, destination, car_mpg, max_cost, max_time, depart_time, key_vault):
    trips = start_ground_trips(source, destination, car_mpg, key_vault)
    print(trips[0], " last city: ", trips[0].get_last_city())
    find_flights(trips, destination, max_cost, max_time, depart_time, key_vault)

"""

"""
def start_ground_trips(source, destination, car_mpg, key_vault):
    src_airports = nearby_airports(source, key_vault)
    trips = []
    for airport, code in src_airports:
        ground_paths = total_ground_cost(source, airport, car_mpg, key_vault)

        car_trip = Trip(source)
        car_costs = ground_paths[0]
        car_trip.carbon_cost += float(car_costs[0])
        car_trip.money_cost += car_costs[1]
        car_trip.time_cost += car_costs[2]
        car_trip.cities.append(TripStep(airport, TripStep.CAR, car_costs[0], car_costs[1], car_costs[2]))
        car_trip.prev_airport_code = code
        if car_trip.carbon_cost >= 0:
            trips.append(car_trip)
        
        bus_trip = Trip(source)
        bus_costs = ground_paths[1]
        bus_trip.carbon_cost += float(bus_costs[0])
        bus_trip.money_cost += bus_costs[1]
        bus_trip.time_cost += bus_costs[2]
        bus_trip.cities.append(TripStep(airport, TripStep.BUS, bus_costs[0], bus_costs[1], bus_costs[2]))
        bus_trip.prev_airport_code = code
        if bus_trip.carbon_cost >= 0:
            trips.append(bus_trip)

        train_trip = Trip(source)
        train_costs = ground_paths[2]
        train_trip.carbon_cost += float(train_costs[0])
        train_trip.money_cost += train_costs[1]
        train_trip.time_cost += train_costs[2]
        train_trip.cities.append(TripStep(airport, TripStep.TRAIN, train_costs[0], train_costs[1], train_costs[2]))
        train_trip.prev_airport_code = code
        if train_trip.carbon_cost >= 0:
            trips.append(train_trip)

    return trips
    
def find_flights(curr_trips, destination, max_cost, max_time, depart_time, key_vault):
    end_cities = nearby_airports(destination, key_vault)
    print(curr_trips)
    updated_trips = []
    for trip in curr_trips:
        if trip.money_cost >= max_cost or trip.time_cost >= max_time:
            continue
        prev_code = trip.prev_airport_code
        if trip.get_last_city() != destination:
            for city in end_cities:
                airport_code = city[1]
                flight_cost = total_air_cost(prev_code, airport_code, depart_time)
                if flight_cost[0] >= 0:
                    curr_trip = deepcopy(trip)
                    flight_step = TripStep(city[1], TripStep.PLANE, flight_cost[0], flight_cost[1], flight_cost[2])
                    curr_trip.carbon_cost += flight_cost[0]
                    curr_trip.money_cost += flight_cost[1]
                    curr_trip.time_cost += flight_cost[2]
                    curr_trip.cities.append(flight_step)
                    updated_trips.append(curr_trip)
    return updated_trips

def finish_trips(curr_trips, destination, max_cost, max_time, car_mpg, key_vault):
    finished_trips = []
    for trip in curr_trips:
        prev_city = trip.get_last_city()
        if prev_city == destination:
            finished_trips.append(trip)
            continue
        ground_paths = total_ground_cost(prev_city, destination, car_mpg, key_vault)
        # By car
        car_costs = ground_paths[0]
        car_trip = deepcopy(trip)
        car_trip_step = TripStep(destination, TripStep.CAR, car_costs[0], car_costs[1], car_costs[2])
        car_trip.cities.append(car_trip_step)
        car_trip.carbon_cost += float(car_costs[0])
        car_trip.money_cost += car_costs[1]
        car_trip.time_cost += car_costs[2]
        if car_trip.money_cost <= max_cost and car_trip.time_cost <= max_time:
            finished_trips.append(car_trip)
        # By bus
        bus_costs = ground_paths[1]
        bus_trip = deepcopy(trip)
        bus_trip_step = TripStep(destination, TripStep.BUS, bus_costs[0], bus_costs[1], bus_costs[2])
        bus_trip.cities.append(bus_trip_step)
        bus_trip.carbon_cost += float(bus_costs[0])
        bus_trip.money_cost += bus_costs[1]
        bus_trip.time_cost += bus_costs[2]
        if bus_trip.money_cost <= max_cost and bus_trip.time_cost <= max_time:
            finished_trips.append(bus_trip)
        # By train
        train_costs = ground_paths[2]
        train_trip = deepcopy(trip)
        train_trip_step = TripStep(destination, TripStep.TRAIN, train_costs[0], train_costs[1], train_costs[2])
        train_trip.cities.append(train_trip_step)
        train_trip.carbon_cost += float(train_costs[0])
        train_trip.money_cost += train_costs[1]
        train_trip.time_cost += train_costs[2]
        if train_trip.money_cost <= max_cost and train_trip.time_cost <= max_time:
            finished_trips.append(train_trip)
    print(finished_trips)
    

from api_management import APIKeys
find_carbon_paths("Tucson", "Seattle", 35, 10000, 100, "2020-01-15", key_vault= APIKeys())
