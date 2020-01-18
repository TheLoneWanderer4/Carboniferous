import json
import sys
from trip_planner import find_carbon_paths
from map_link import map_link
from api_management import APIKeys

def main(*args):
    key_vault = APIKeys()
    input_data = args[1].json()
    start_city,end_city,car_mpg, = \
        input_data["start"],input_data["end"],input_data["mode"]["car"]["mpg"] 
    max_cost,max_time,depart_date = \
        input_data["maxPrice"],input_data["maxTime"],input_data["date"]
    # find_carbon_paths will return a list of path objects to return as a json
    # files to the front end.
    return_list = []
    final_list = find_carbon_paths(start_city,end_city,car_mpg,max_cost,\
        max_time,depart_date, key_vault)
    for i in range(5):
        print(len(final_list))
        if(len(final_list) <= i):
            break
        return_list.append(final_list[i].make_dict())
        # TODO: Actually check if this works!!!
        previous_step = return_list[0]["trip"]["step"]
        previous_step["current_city"] =""
        for k in range(1,len(return_list[i]["trip"]["step"])):
            curr_step = return_list["trip"]["step"][i]
            curr_step["link"] = map_link(previous_step["current_city"],\
                curr_step["current_city"],curr_step[transport])
            previous_step = curr_step
    
    print(return_list) 
    return json.dumps(return_list)

main(sys.argv)
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
