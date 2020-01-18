import sys
'''
Given a starting and ending city, and the mode of transportation (train,bus,car,plane) this
function will print the url for the embedded map. 
Will return ValueError if the mode of transport is not one of the four
'''
def map_links(args):
    start, destination, mode = args[1], args[2],args[3]
    # This horribly named dictionary is to translate our internal names of transportation to 
    # what the google api uses. 
    mode_to_gmode = {"train": "transport", "bus":"transport","car":"driving", "plane": "flying"}
    if mode not in mode_to_gmode:
        raise ValueError("none is not a proper mode of transport")
    GKEY = "AIzaSyCK4gZqTHsd4Fi7_enR4aaDuyFGwmi3Je4"
    link = "https://www.google.com/maps/embed/v1/directions?key=" + GKEY + \
        "&origin=" + start + "&destination=" + destination + "&mode=" + mode_to_gmode[mode]
    print(link)
map_links(sys.argv)