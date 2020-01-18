import json
import sys
from trip_planner import find_carbon_paths

def main(*args):
    input_data = args[1].json()
    start_city,end_city,car_mpg, = \
        input_data["start"],input_data["end"],input_data["mode"]["car"]["mpg"] 
    max_cost,max_time,depart_date = \
        input_data["maxPrice"],input_data["maxTime"],input_data["date"]
    # find_carbon_paths will return a list of path objects to return as a json
    # files to the front end.
    return_list = []
    final_list = find_carbon_paths(start_city,end_city,car_mpg,max_cost,\
        max_time,depart_date)
    for i in range(5):
        print(len(final_list))
        if(len(final_list) <= i):
            break
        return_list.append(final_list[i].make_dict())

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
        }
    ]
    total_carbon:
    total_dollars:
    total_time: 
}
"""
