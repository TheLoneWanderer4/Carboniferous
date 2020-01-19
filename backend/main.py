import json
import sys
from trip_planner import find_carbon_paths
from api_management import APIKeys
from map_link import map_links

def main(args):
    key_vault = APIKeys()
    input_data = json.loads(args)
    start_city,end_city,car_mpg, = \
        input_data["start"],input_data["end"],int(input_data["modes"]["car"]["mpg"]) 
    max_cost,max_time,depart_date = \
        int(input_data["maxPrice"]),int(input_data["maxTime"]),input_data["Date"]
    # find_carbon_paths will return a list of path objects to return as a json
    # files to the front end.
    return_list = []
    final_list = find_carbon_paths(start_city,end_city,car_mpg,max_cost,\
        max_time,depart_date, key_vault)
    # Serializing data to send back across
    for i in range(5):
        print(final_list[i].make_dict())
        if(len(final_list) <= i):
            break
        trip_dict = final_list[i].make_dict()
        trip_dict["steps"][0]["link"] = ""
        for k in range(1,len(trip_dict["steps"])):
            trip_dict["steps"][k]["link"] = map_links(trip_dict["steps"][k-1]["current_city"],trip_dict["steps"][k]["current_city"],trip_dict["steps"][k]["transport"])
        print(trip_dict)
        return_list.append(trip_dict)
        # TODO: Actually check if this works!!!
    print(return_list)
    return json.dumps(return_list)


input_json = """{
"start": "Tucson",
"end": "Seattle",
"Date": "2020-01-19",
"partySize": "22",
"maxPrice": "500",
"maxTime": "12",
"modes":{
"car": {"allowed": true, "mpg": "30"},
"bus": {"allowed": true},
"plane": {"allowed": true},
"train": {"allowed": true}
}
}"""
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
        }
    ]
    total_carbon:
    total_dollars:
    total_time: 
}
"""
