import json
from trip_planner import find_carbon_paths

def main(input_json):
    input_data = input_json.json()
    start_city = input_data["start"]
    end_city = input_data["end"]

    # find_carbon_paths will return a list of path objects to return as a json
    # files to the front end.
    return_dict = {}
    final_list = find_carbon_paths(start_city,end_city)
    for i in range(5):
        print(len(final_list))
        if(len(final_list) <= i):
            break
        return_dict[i] = final_list[i].make_dict()

    print(return_dict)
    return json.dumps(return_dict)

"""
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
