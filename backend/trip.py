class Trip:

    """
    total_costs is the triple tuple of costs (carbon, money, time)
    cities is a list of TripSteps
    """

    def __init__(self, start):
        self.cities = []
        self.cities.append(TripStep(start, None, 0.0, 0.0, 0.0))
        self.cities = []
        self.carbon_cost = 0.0
        self.money_cost = 0.0
        self.time_cost = 0.0

    def __repr__(self):
        curr = "{" + str(self.carbon_cost) + "," + str(self.money_cost) + "," + str(self.time_cost) + "} "
        for city in self.cities:
            curr += (city.current_city + '(' + city.transport_mode + ')' + '->')
        return curr + 'ENDTRIP\n'

class TripStep:
    # Modes of transportation allowed
    PLANE = "plane"
    CAR = "car"
    BUS = "bus"
    TRAIN = "train"

    # Fields for a TripStep
    current_city = ""
    transport_mode = ""
    carbon_cost = 0.0
    dollar_cost = 0.0
    time_cost = 0.0

    def __init__(self, city, mode, carbon, money, time):
        self.current_city = city
        if mode == None:
            self.transport_mode = ""
        else:
            self.transport_mode = mode
        self.carbon_cost = carbon
        self.dollar_cost = money
        self.time_cost = time