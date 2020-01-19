import json
import sys
from trip_planner import find_carbon_paths
from api_management import APIKeys
from map_link import map_links

def main(args):
    key_vault = APIKeys()
    input_data = json.load(args)

    start_city,end_city,car_mpg, = \
        input_data["start"],input_data["end"],int(input_data["modes"]["car"]["mpg"])
    max_cost,max_time,depart_date = \
        int(input_data["maxPrice"]),int(input_data["maxTime"]),input_data["Date"]
    modes = [True,True,True,True]
    modes[0] = input_data["modes"]["car"]["allowed"]
    modes[1] = input_data["modes"]["bus"]["allowed"]
    modes[2] = input_data["modes"]["train"]["allowed"]
    modes[3] = input_data["modes"]["plane"]["allowed"]
    # find_carbon_paths will return a list of path objects to return as a json
    # files to the front end.
    return_list = []

    final_list = find_carbon_paths(start_city,end_city,car_mpg,max_cost,\
        max_time,depart_date, modes, key_vault)

    # Serializing data to send back across
    for i in range(5):
        if(len(final_list) <= i):
            break
        trip_dict = final_list[i].make_dict()
        trip_dict["steps"][0]["link"] = ""
        for k in range(1,len(trip_dict["steps"])):
            trip_dict["steps"][k]["link"] = map_links(trip_dict["steps"][k-1]["current_city"],trip_dict["steps"][k]["current_city"],trip_dict["steps"][k]["transport"])
        return_list.append(trip_dict)
        # TODO: Actually check if this works!!!
    for x in return_list:
        print(json.dumps(x))

    if(len(return_list) < 1):
        print(json.dumps(backup_data))

    return json.dumps(return_list)

# MUST CHANGE ABSOLUTE PATH BASED ON LOCATION
input_json = open("/var/www/Carboniferous/backend/input.json")

backup_data = {
    "steps" : [{"current_city": "ERROR",
                "transport":"ERROR",
                "carbon_cost" : 'ERROR',
                "dollar_cost" : "ERROR",
                "time_cost" : "ERROR",
                "link": "https://www.youtube.com/watch?v=oHg5SJYRHA0"}],
    "total_carbon" : 404,
    "total_dollars" : 404,
    "total_time" : 404
}



main(input_json)
"""
INPUT JSON
start: "",
    end: "",
    Date: "",
    partySize: "",
    maxPrice: "",
    maxTime: "",
    modes: {
      car: { allowed: false, mpg: 0 },
      bus: { allowed: false },
      plane: { allowed: false },
      train: { allowed: false }
    }

OUTPUT JSON
trip: {
    steps: [
        {
            current_city: "",
            transport: "" (will be None, train, bus, car, plane)
            carbon_cost:
            dollar_cost:
            time_cost:
            link:
        }
    ]
    total_carbon:
    total_dollars:
    total_time:
}
"""
