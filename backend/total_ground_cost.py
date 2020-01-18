"""
Calculates the total carbon cost (C), monetary cost ($), and time cost (t) 
as a triple for the trip from a source city to a destination city.
"""
import json
import requests
import googlemaps as maps
from datetime import datetime as dt


# Constants used for calling the Trip to Carbon API
CAR = "petrolCar"
BUS = "bus"
TRAIN = "transitRail"
LIST_FUEL_TYPES_USED = [CAR, BUS, TRAIN]

# The URL used to request the carbon costs from the Trip to Carbon API
MAPS_BASE_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
CARBON_BASE_URL = 'https://api.triptocarbon.xyz/v1/footprint?country=usa&activity='
CARBON_CAR_URL_EXT = '&fuelType=motorGasoline&mode=petrolCar'
CARBON_BUS_URL_EXT = '&fuelType=diesel&mode=bus'
CARBON_TRAIN_URL_EXT = '&mode=transitRail'

# Google Maps API Key. TODO: Move this
API_KEY = 'AIzaSyCK4gZqTHsd4Fi7_enR4aaDuyFGwmi3Je4' 

# Constants for calculating costs of travel
PETROL_PRICE_PER_GAL = 2.83
BUS_PRICE_PER_MILE_USD = 0.10


"""
Entry point for calculating the total cost of the ground trip from city_a to 
city_b.

Parameters:
city_a: The full name of the source city
city_b: The full name of the destination city
mpg: a decimal number representing the miles per gallon that the user specifies

Return:
a list of triples, one for each of the ground
options: car, bus, and train. The triple is in the order (C, $, t)
"""
def total_ground_cost(city_a, city_b, mpg):
    list_of_costs = []
    # Request Car cost
    miles_by_car, hours_by_car = get_distance_and_time_by_car(city_a, city_b)
    gallons_used = str(miles_by_car // mpg)
    response = requests.get(CARBON_BASE_URL + gallons_used + '&activityType=fuel' + CARBON_CAR_URL_EXT)
    list_of_costs.append( (response.json()['carbonFootprint'], \
            gallons_used * PETROL_PRICE_PER_GAL, \
            hours_by_car) )

    # Request Bus cost
    miles_by_bus, hours_by_bus = get_distance_and_time_by_bus(city_a, city_b)
    response = requests.get(CARBON_BASE_URL + miles_by_bus + '&activityType=miles' + CARBON_BUS_URL_EXT)
    list_of_costs.append( (response.json()['carbonFootprint'], \
            miles_by_bus * BUS_PRICE_PER_MILE_USD, \
            hours_by_bus) )

    # Request Train cost
    miles_by_train, hours_by_train = get_distance_and_time_by_train(city_a, city_b)
    response = requests.get(CARBON_BASE_URL + miles_by_train + '&activityType=miles' + CARBON_TRAIN_URL_EXT)
    list_of_costs.append( (response.json()['carbonFootprint'], \
            gallons_used * PETROL_PRICE_PER_GAL, \
            hours_by_car) )


"""
Returns the number of miles to drive by car from city_a to city_b as well as a decimal
for the number of hours to get there by using the Google Maps Distance Matrix API
"""
def get_distance_and_time_by_car(city_a, city_b):
    response = requests.get(MAPS_BASE_URL + \
        '&mode=driving' + \
        '&origins=' + city_a + \
        '&destinations=' + city_b + \
        '&key=' + API_KEY).json()
    try:
        print(response)
        num_miles = response['rows'][0]['elements'][0]['distance']['text'][:-3]
        time_secs = int(response['rows'][0]['elements'][0]['duration']['value'])
        return (int(num_miles), (time_secs / 3600) )
    except KeyError:
        return (-1, -1)

def get_distance_and_time_by_bus(city_a, city_b):
    response = requests.get(MAPS_BASE_URL + \
        '&mode=transit&transit_mode=' + 'bus' + \
        '&origins=' + city_a + \
        '&destinations=' + city_b + \
        '&key=' + API_KEY).json()
    try:
        print(response)
        num_miles = response['rows'][0]['elements'][0]['distance']['text'][:-3]
        time_secs = int(response['rows'][0]['elements'][0]['duration']['value'])
        return (int(num_miles), (time_secs / 3600) )
    except KeyError:
        return (-1, -1)

def get_distance_and_time_by_train(city_a, city_b):
    response = requests.get(MAPS_BASE_URL + \
        '&mode=transit&transit_mode=' + 'train' + \
        '&origins=' + city_a + \
        '&destinations=' + city_b + \
        '&key=' + API_KEY).json()
    try:
        print(response)
        num_miles = response['rows'][0]['elements'][0]['distance']['text'][:-3]
        time_secs = int(response['rows'][0]['elements'][0]['duration']['value'])
        return (int(num_miles), (time_secs / 3600) )
    except KeyError:
        return (-1, -1)

print(get_distance_and_time_by_car('Tucson', 'Tempe'))
    