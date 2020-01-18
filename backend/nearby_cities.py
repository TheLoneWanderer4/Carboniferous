import json
import requests
import googlemaps
import pprint
'''
This function takes in a city name, as a string, and returns the names of the five 
nearest airports
'''
def nearby_airports(city):
    # Key tokens for api
    LUFT_MAIN_KEY = "5xwbffdd35p2kbkmbawv6wjr"
    LUFT_PRIVATE_KEY = "Jez3gpttWg"
    GKEY = "AIzaSyCK4gZqTHsd4Fi7_enR4aaDuyFGwmi3Je4"
    # change this later
    gmaps = googlemaps.Client(key=GKEY)

    # GETTING THE LAT AND LNG FOR THE GIVEN CITY
    city_link = requests.get(\
        "https://maps.googleapis.com/maps/api/geocode/json?address="\
        + city + "&key=" + GKEY)
    city_data = city_link.json()
    # approximate latitude and longitude for the given city
    city_lat = city_data["results"][0]["geometry"]["location"]["lat"]
    city_lng = city_data["results"][0]["geometry"]["location"]["lng"]

    # get the token for the airport api
    get_token_data = {"client_id": LUFT_MAIN_KEY, "client_secret":LUFT_PRIVATE_KEY, \
        "grant_type": "client_credentials"}
    api_token = (requests.post("https://api.lufthansa.com/v1/oauth/token",\
         data = get_token_data)).json()["access_token"]  
    headers = {"Authorization": "Bearer " + api_token}
    # gets the json return of the 5 nearest airports 
    airports_json = (requests.get("https://api.lufthansa.com/v1/references/airports/nearest/"\
        + str(city_lat)+ ","+str(city_lng)+ "?lang=en",headers=headers)).json()
    final_list = []
    for i in airports_json["NearestAirportResource"]["Airports"]["Airport"]:
        final_list.append(i["Names"]["Name"]["$"])
    return final_list



    

