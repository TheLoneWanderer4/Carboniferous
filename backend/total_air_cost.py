import requests

# api locations
FLIGHT_DATA_API = "http://localhost:3030/flights"
CARBON_FOOTPRINT_API = "https://api.triptocarbon.xyz/v1/footprint"

# strings that are likely to be adjusted as parameters
FLIGHT_TYPE = "economyFlight"
COUNTRY = "usa"
COST = "cost"


def total_air_cost(src, dest, date):
    flights = (requests.get(FLIGHT_DATA_API,
                            params={"date": date, "origin": src, "destination": dest})).json()

    if len(flights) == 0:
        return [-1, -1, -1]

    footprint = float(requests.get(CARBON_FOOTPRINT_API,
                              params={"activity": flights[0].get("distance"), "activityType": "miles",
                                      "mode": FLIGHT_TYPE, "country": COUNTRY}).json().get("carbonFootprint"))

    info = [footprint, get_time_from_flight(flights[0]), get_min_cost(flights)]
    return info


def get_time_from_flight(flight):
    return flight.get("duration").get("hours") + (flight.get("duration").get("minutes") / 60)


def get_min_cost(flights):
    min_cost = flights[0].get(COST)
    for flight in flights:
        if flight.get(COST) < min_cost:
            min_cost = flight.get(COST)
    return min_cost


# for testing
print(total_air_cost("ORD", "DFW", "2020-01-02"))
