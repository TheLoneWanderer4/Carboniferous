class Trip:

    PLANE = "plane"
    CAR = "car"
    BUS = "bus"
    TRAIN = "train"

    """
    total_costs is the triple tuple of costs (carbon, mooney, time)
    city is a tuple with the airport name and the mode of travel there
    """
    def __init__(self, city, total_costs):
        self.cities = [city]
        self.carbon_cost = total_costs[0]
        self.money_cost = total_costs[1]
        self.time_cost = total_costs[2]

    