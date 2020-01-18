import requests


def total_air_cost(src, dest, date):
    flights = (requests.get("http://localhost:3030/flights",
                            params={"date": date, "origin": src, "destination": dest})).json()

    if len(flights) == 0:
        return [-1, -1, -1]

    footprint = float(requests.get("https://api.triptocarbon.xyz/v1/footprint",
                              params={"activity": flights[0].get("distance"), "activityType": "miles",
                                      "mode": "economyFlight", "country": "usa"}).json().get("carbonFootprint"))

    info = [footprint, get_time_from_flight(flights[0]), get_min_cost(flights)]
    return info


def get_time_from_flight(flight):
    return flight.get("duration").get("hours") + (flight.get("duration").get("minutes") / 60)


def get_min_cost(flights):
    min_cost = flights[0].get("cost")
    for flight in flights:
        if flight.get("cost") < min_cost:
            min_cost = flight.get("cost")
    return min_cost


# for testing
print(total_air_cost("ORD", "DFW", "2020-01-02"))
