"""
Calculates the total carbon cost (C), monetary cost ($), and time cost (t) 
as a triple for the trip from a source city to a destination city for all ground
travel options.
"""
import json
import requests
import googlemaps as maps
from datetime import datetime as dt


# Constants used for querying Google Maps and Trip to Carbon APIs
MAPS_BASE_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
CARBON_BASE_URL = 'https://api.triptocarbon.xyz/v1/footprint?country=usa&activity='
CARBON_CAR_URL_EXT = '&fuelType=motorGasoline&mode=petrolCar'
CARBON_BUS_URL_EXT = '&fuelType=diesel&mode=bus'
CARBON_TRAIN_URL_EXT = '&mode=transitRail'

# Google Maps API Key. TODO: Move this
API_KEY = 'AIzaSyCK4gZqTHsd4Fi7_enR4aaDuyFGwmi3Je4' 

# Constants for calculating costs of travel
PETROL_PRICE_PER_GAL_USD = 2.83
BUS_PRICE_PER_MILE_USD = 0.10
TRAIN_PRICE_PER_MILE_USD = 0.50



"""
Entry point for calculating the total cost of the ground trip from city_a to 
city_b.

Parameters:
city_a: The full name of the source city
city_b: The full name of the destination city
mpg: a decimal number representing the miles per gallon that the user specifies

Return:
a list of triples, one for each of the ground options: car, bus, and train in 
that order. The triple is in the order (C, $, t)
"""
def total_ground_cost(city_a, city_b, mpg):
    list_of_costs = []
    # Car Costs
    miles_by_car, hours_by_car = get_distance_and_time_by_car(city_a, city_b)
    gallons_used = miles_by_car // mpg
    if(gallons_used == 0):
        list_of_costs.append((0, 0, 0)) # negligible cost
    else:
        response = requests.get(CARBON_BASE_URL + str(gallons_used) + '&activityType=fuel' + CARBON_CAR_URL_EXT)
        list_of_costs.append( (response.json()['carbonFootprint'], \
                gallons_used * PETROL_PRICE_PER_GAL_USD, \
                hours_by_car) )

    # Bus Costs
    miles_by_bus, hours_by_bus = get_distance_and_time_by_bus(city_a, city_b)
    if (miles_by_bus == 0):
        list_of_costs.append((0, 0, 0))  # negligible cost
    else:
        response = requests.get(CARBON_BASE_URL + str(miles_by_bus) + '&activityType=miles' + CARBON_BUS_URL_EXT)
        list_of_costs.append( (response.json()['carbonFootprint'], \
                miles_by_bus * BUS_PRICE_PER_MILE_USD, \
                hours_by_bus) )

    # Train Costs
    miles_by_train, hours_by_train = get_distance_and_time_by_train(city_a, city_b)
    if(miles_by_train == 0):
        list_of_costs.append((0, 0, 0))  # negligible cost
    else:
        response = requests.get(CARBON_BASE_URL + str(miles_by_train) + '&activityType=miles' + CARBON_TRAIN_URL_EXT)
        list_of_costs.append( (response.json()['carbonFootprint'], \
                miles_by_train * TRAIN_PRICE_PER_MILE_USD, \
                hours_by_train) )

    return list_of_costs


"""
Returns the number of miles to drive by car from city_a to city_b as well as a decimal
for the number of hours to get there by using the Google Maps Distance Matrix API

Parameters: 
city_a: The full name of the source city
city_b: The full name of the destination city

Return:
a tuple that gives the number of miles from city_a to city_b by driving a car
and the time in number of hours to drive that distance
"""
def get_distance_and_time_by_car(city_a, city_b):
    response = requests.get(MAPS_BASE_URL + \
        '&mode=driving' + \
        '&origins=' + city_a + \
        '&destinations=' + city_b + \
        '&key=' + API_KEY).json()
    try:
        num_miles = response['rows'][0]['elements'][0]['distance']['text'][:-3]
        time_secs = int(response['rows'][0]['elements'][0]['duration']['value'])
        return (int(float(num_miles)), (time_secs / 3600) )
    except KeyError:
        return (-1, -1)


"""
Returns the number of miles to take a bus from city_a to city_b as well as a decimal
for the number of hours to get there by using the Google Maps Distance Matrix API

Parameters: 
city_a: The full name of the source city
city_b: The full name of the destination city

Return:
a tuple that gives the number of miles from city_a to city_b by taking a car
and the time in number of hours to travel that distance
"""
def get_distance_and_time_by_bus(city_a, city_b):
    response = requests.get(MAPS_BASE_URL + \
        '&mode=transit&transit_mode=' + 'bus' + \
        '&origins=' + city_a + \
        '&destinations=' + city_b + \
        '&key=' + API_KEY).json()
    try:
        num_miles = response['rows'][0]['elements'][0]['distance']['text'][:-3]
        time_secs = int(response['rows'][0]['elements'][0]['duration']['value'])
        return (int(float(num_miles)), (time_secs / 3600) )
    except KeyError:
        return (-1, -1)


"""
Returns the number of miles to take a train from city_a to city_b as well as a decimal
for the number of hours to get there by using the Google Maps Distance Matrix API

Parameters: 
city_a: The full name of the source city
city_b: The full name of the destination city

Return:
a tuple that gives the number of miles from city_a to city_b by taking a train
and the time in number of hours to travel that distance
"""
def get_distance_and_time_by_train(city_a, city_b):
    response = requests.get(MAPS_BASE_URL + \
        '&mode=transit&transit_mode=' + 'train' + \
        '&origins=' + city_a + \
        '&destinations=' + city_b + \
        '&key=' + API_KEY).json()
    try:
        num_miles = response['rows'][0]['elements'][0]['distance']['text'][:-3]
        time_secs = int(response['rows'][0]['elements'][0]['duration']['value'])
        return (int(float(num_miles)), (time_secs / 3600) )
    except KeyError:
        return (-1, -1)