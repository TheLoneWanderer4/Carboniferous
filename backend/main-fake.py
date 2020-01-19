import sys
import json

fake_step = {
    "current_city": "Tucson",
    "transport":"Plane",
    "carbon_cost" : 70,
    "dollar_cost" : 800,
    "time_cost" : 3,
    "link": "https://www.google.com/maps/embed/v1/directions?key=AIzaSyCK4gZqTHsd4Fi7_enR4aaDuyFGwmi3Je4&origin=tucson&destination=dallas&mode=driving"

}

data = {
    "steps" : [fake_step, fake_step, fake_step],
    "total_carbon" : 400,
    "total_dollars" : 1200,
    "total_time" : 5
}

fake_step2 = {
    "current_city": "Dallas",
    "transport":"Plane",
    "carbon_cost" : 70,
    "dollar_cost" : 800,
    "time_cost" : 3,
    "link": "https://www.google.com/maps/embed/v1/directions?key=AIzaSyCK4gZqTHsd4Fi7_enR4aaDuyFGwmi3Je4&origin=tucson&destination=dallas&mode=driving"


}

data2 = {
    "steps" : [fake_step2, fake_step2, fake_step2],
    "total_carbon" : 900,
    "total_dollars" : 100,
    "total_time" : 5
}

print(json.dumps(data))
print(json.dumps(data))
print(json.dumps(data))
print(json.dumps(data2))
print(json.dumps(data2))
