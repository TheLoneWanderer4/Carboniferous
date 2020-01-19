import requests

# api locations
FLIGHT_DATA_API = "http://localhost:3030/flights"

# strings that are likely to be adjusted as parameters
FLIGHT_TYPE = "economyFlight"
COUNTRY = "usa"
COST = "cost"

KG_C_PER_MILE_BUS = 0.18

def total_air_cost(src, dest, date):
    flights = (requests.get(FLIGHT_DATA_API,
                            params={"date": date, "origin": src, "destination": dest})).json()

    if len(flights) == 0:
        print(src + " to " + dest)
        return [-1, -1, -1]

    footprint = flights[0].get("distance") * KG_C_PER_MILE_BUS

    info = [footprint, get_min_cost(flights), get_time_from_flight(flights[0])]
    return info


def get_time_from_flight(flight):
    return flight.get("duration").get("hours") + (flight.get("duration").get("minutes") / 60)


def get_min_cost(flights):
    min_cost = flights[0].get(COST)
    for flight in flights:
        if flight.get(COST) < min_cost:
            min_cost = flight.get(COST)
    return min_cost