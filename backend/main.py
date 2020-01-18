import json
from trip_planner import find_carbon_paths
'''
More probably needs to be added to this
'''
def main(input_json):
    input_data = input_json.json()
    start_city = input_data["start"]
    end_city = input_data["end"]

    # DO STUFF HERE

    # find_carbon_paths will return a list of path objects to return as a json
    # files to the front end.
    return_dict = {}
    final_list = find_carbon_paths(start_city,end_city)
    for i in range(0,5):
        return_dict["Trip "+ (i+1)] = final_list[i].__dict__
    return json.dumps(return_dict)
