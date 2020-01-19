import sys
'''
Given a starting and ending city, and the mode of transportation (train,bus,car,plane) this
function will print the url for the embedded map. 
Will return ValueError if the mode of transport is not one of the four
'''
def map_links(start,destination,mode):
    # This horribly named dictionary is to translate our internal names of transportation to 
    # what the google api uses. 
    mode_to_gmode = {"train": "transit", "bus":"transit","car":"driving", "plane": "flying"}
    if mode not in mode_to_gmode:
        raise ValueError("none is not a proper mode of transport")
    link = "https://www.google.com/maps/dir/?api=1" + \
        "&origin=" + start + "&destination=" + destination + "&travelmode=" + mode_to_gmode[mode]
    return link
