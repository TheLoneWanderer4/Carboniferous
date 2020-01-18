class Trip:

    """
    total_costs is the triple tuple of costs (carbon, money, time)
    cities is a list of TripSteps
    """
    def __init__(self, cities, total_costs):
        self.cities = cities
        self.carbon_cost = total_costs[0]
        self.money_cost = total_costs[1]
        self.time_cost = total_costs[2]

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
    time_Cost = 0.0