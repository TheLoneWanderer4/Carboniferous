class Trip:
    # Modes of transportation allowed
    PLANE = "plane"
    CAR = "car"
    BUS = "bus"
    TRAIN = "train"
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
        self.prev_airport_code = ""

    def __repr__(self):
        curr = "{" + str(self.carbon_cost) + "," + str(self.money_cost) + "," + str(self.time_cost) + "} "
        for city in self.cities:
            curr += (city.current_city + '(' + city.transport_mode + ')' + '->')
        return curr + 'ENDTRIP\n'

    def get_last_city(self):
        last_step = self.cities[-1]
        return last_step.current_city

    """
    builds trip into a dictionary for json object creation
    """
    def make_dict(self):
        dict = {}
        step_list = []
        total_carbon = 0
        total_dollars = 0
        total_time = 0
        for step in self.cities:
            step_dict = {}
            step_dict["current_city"] = step.current_city
            step_dict["transport"] = str(step.transport_mode)
            step_dict["carbon_cost"] = step.carbon_cost
            step_dict["dollar_cost"] = step.dollar_cost
            step_dict["time_cost"] = step.time_cost
            step_list.append(step_dict)

            total_carbon += step.carbon_cost
            total_dollars += step.dollar_cost
            total_time += step.time_cost


        dict["steps"] = step_list
        dict["total_carbon"] = total_carbon
        dict["total_dollars"] = total_dollars
        dict["total_time"] = total_time

        return dict

class TripStep:
    # Fields for a TripStep
    current_city = ""
    transport_mode = ""
    carbon_cost = 0.0
    dollar_cost = 0.0
    time_cost = 0.0

    def __init__(self, city, mode, carbon, money, time):
        self.current_city = city
        if mode == None:
            self.transport_mode = "none"
        else:
            self.transport_mode = mode
        self.carbon_cost = carbon
        self.dollar_cost = money
        self.time_cost = time
