import json
import requests
import googlemaps
import pprint
'''
This function takes in a city name, as a string, and returns a list of tuples,
with each tuple having the name of the airport and its IATA airport code
'''
def nearby_airports(city, key_vault):
    # Key tokens for api
    LUFT_MAIN_KEY = key_vault.luft_main_key()
    LUFT_PRIVATE_KEY = key_vault.luft_private_key()
    GKEY = key_vault.google_key()
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
        final_list.append((i["Names"]["Name"]["$"],i["AirportCode"]))
    return final_list

    

