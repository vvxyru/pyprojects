def load_stop_codes() -> dict[str, str]:
    stops = {}

    with open("codes.txt", "r") as file:
        for line in file:
            key, value = line.strip().split(",", 1)
            stops[key] = value
    return stops

def load_bus_routes() -> dict[str, list[str]]:
    routes = {}

    with open("routes.txt", "r") as file:
        for line in file:
            split_line = line.strip().split(",")
            route_num = split_line[0]
            stops = split_line[1:]

            routes[route_num] = stops

    return routes

def find_routes(
        stops_dict: dict[str, str],
        routes_dict: dict[str, list[str]],
        starting_stop: str,
        destination_stop: str,
):
    # Convert stop names to codes (ex. D017 -> University)
    starting_code = ""
    destination_code = ""

    for stop_code, name in stops_dict.items():
        if name == starting_stop:
            starting_code = stop_code
        if name == destination_stop:
            destination_code = stop_code

    # Case 1: Direct route
    for bus_number, route_list in routes_dict.items():
        if starting_code in route_list and destination_code in route_list:
            return direct_route_message(bus_number, route_list, stops_dict)

    # Case 2: Route with a transfer
    return find_transfer_route(stops_dict, routes_dict, starting_code, destination_code)

def find_transfer_route(
        stops_dict: dict[str, str],
        routes_dict: dict[str, list[str]],
        starting_code: str,
        destination_code: str
) -> str:

    starting_routes = {}
    destination_routes = {}

    transfer_stop = ""
    transferA = ""
    transferB = ""
    
    # Routes containing start point
    for bus_number, route_list in routes_dict.items():
        if starting_code in route_list:
            starting_routes[bus_number] = route_list

    # Routes containing destination point
    for bus_number, route_list in routes_dict.items():
        if destination_code in route_list:
            destination_routes[bus_number] = route_list

    # Find transfer stop
    # This is so ugly im sorry
    for rA_num, rA_list in starting_routes.items():
        for stopA in rA_list:  # walk along starting route in order
            for rB_num, rB_list in destination_routes.items():
                if rA_num != rB_num and stopA in rB_list:
                    transfer_stop = stops_dict[stopA]
                    transferA = rA_num
                    transferB = rB_num
                    transfer_message = (
                        f"Take route {transferA} and get off at {transfer_stop}.\n"
                        f"Then take route {transferB} to your destination.\n"
                        f"\n"
                        f"Route {transferB}: {rB_list}"
                    )
                    return transfer_message
    return "No routes serving that start point and end point"

def direct_route_message(bus_number: str, route_list: list[str], stops_dict: dict[str, str]) -> str:
    direct_message = f"Direct route found: {bus_number}"

    for code in route_list:
        stop_name = stops_dict[code]
        direct_message += f" -> {stop_name}"

    return direct_message

def main() -> None:
    stops_dict = load_stop_codes()
    routes_dict = load_bus_routes()

    user_starting_name = input("Enter Starting Point: ").title()
    user_destination_name = input("Enter Destination: ").title()

    completed_route = find_routes(stops_dict, routes_dict, user_starting_name, user_destination_name)
    
    print(completed_route)

if __name__ == "__main__":
    main()


