# --> I chose option number 2 for this lab since it looked more simple lol

# Will store a list of properties, each turned into a dictionary
# Each property in the list has the form of:
# property = {
#   str: str,   (location_name)
#   str: int,   (rooms)
#   str: float, (area)
#   str: int    (owner_id)
# }
# I chose to store it this way since each property has information which are
# spanned across multiple types, this way I can also access specific info
# for each property listing easier
property_list: list[dict[str, str | int | float]] = []

# List to store all the information of all the firms, similar way to
# the properties list where each firm is a dictionary:
# firm =  {
#   str: int, (owner_id)
#   str: str, (name)
#   str: int, (date_est)
# }
firm_list: list[dict[str, str | int]] = []

# List of all the locations from 'price_index.txt', but this time its
# just a dictionary of all the items instead of a list
location_list: dict[str, float] = {}

def get_property_info() -> None:

    # This function transforms all the properties in the list to a list of
    # dictionaries, which I can access individual to work on later
    with open("properties.txt", "r") as file:

        # This will become a list including all the lines inside the properties
        # file, then I just loop through them all excluding the first line as
        # the first line is just a header explaining the data
        lines = file.readlines()

        for line in lines[1:]:  # Skips the header line here (first in list)
            location, rooms, area, firm_id = line.strip().split(",")

            property_info = {
                "location": location,
                "rooms": int(rooms),
                "area": float(area),
                "owner_id": int(firm_id)
            }

            property_list.append(property_info)


def get_firm_info() -> None:
    # I'm just going to select the same company that was used in the sample,
    # but I included functionality to get all the firms just in case

    with open("ownership.txt", "r") as file:
        lines = file.readlines()

        for line in lines[1:]:
            firm_id, name, date_est = line.strip().split(",")
            
            firm_info = {
                "owner_id": int(firm_id),
                "name": name,
                "date_est": int(date_est),
            }

            firm_list.append(firm_info)


def get_location_info() -> None:
    # Probably could've just hard coded all the locations into a dictionary,
    # but I guess this is here just incase there are any new locations added
    global location_list

    with open("price_index.txt", "r") as file:
        lines = file.readlines()

        for line in lines[1:]:
            location, average_price = line.strip().split(",")

            # Making all of the values float to make life simple
            location_list[location] = float(average_price)

    # Sorts the dictionary by name (required by lab)
    # Didn't need to search up how to do this (I'm lying)
    location_list = dict(sorted(location_list.items()))


def get_firm_id(firm_name: str) -> int:
    global firm_list

    for firm in firm_list:
        if firm["name"] == firm_name:
            return int(firm["owner_id"])
    return -1   # Default value, should never return though


def get_firm_date(firm_name: str) -> int:
    global firm_list

    for firm in firm_list:
        if firm["name"] == firm_name:
            # Annoying IDE warning, had to put 'int()'
            return int(firm["date_est"])
    return -1   # Default value, should never return though


def get_property_count(firm_name: str, location_name: str) -> int:
    global property_list
    property_count = 0

    firm_id = get_firm_id(firm_name)
    
    # I'm using 'place' because 'property' is a keyword lol
    for place in property_list:
        if place["owner_id"] == firm_id and place["location"] == location_name:
            property_count+= 1
    return property_count


def get_total_area(firm_name: str, location_name: str) -> float:
    global property_list
    total_area = 0.0

    firm_id = get_firm_id(firm_name)
    
    # I'm using 'place' because 'property' is a keyword lol
    for place in property_list:
        if place["owner_id"] == firm_id and place["location"] == location_name:
            total_area += float(place["area"])
    return total_area


def get_area_value(firm_name: str, location_name: str) -> float:
    global property_list
    global location_list
    total_price = 0.0

    firm_id = get_firm_id(firm_name)
    
    for place in property_list:
        if place["owner_id"] == firm_id and place["location"] == location_name:
            location_area = float(place["area"])
            location_price_per_sqft = float(location_list[location_name])

            total_price += location_area * location_price_per_sqft
    return total_price


def get_total_properties(firm_name: str) -> int:
    global property_list
    total_properties = 0

    firm_id = get_firm_id(firm_name)
    
    for place in property_list:
        if place["owner_id"] == firm_id:
            total_properties+= 1
    return total_properties


def get_networth(firm_name: str) -> float:
    global location_list
    global property_list

    overall_networth = 0.0

    for location in location_list:
        overall_networth += get_area_value(firm_name, location)

    return float(overall_networth)


def location_asset_summary(firm_name: str, location_name: str) -> None:
    global property_list
    global location_list

    total_locations = get_property_count(firm_name, location_name)
    total_area = get_total_area(firm_name, location_name)
    total_value = get_area_value(firm_name, location_name)

    print(f"\n{location_name}:")

    # Right aligns with a specific amount of places
    print(f"\tProperties owned: {total_locations:>13}")

    # Adds commas, 2 decimal points
    print(f"\tArea (sqft): {total_area:>18,.2f}")

    print(f"\tNet Value: $ {total_value:>18,.2f}")


def print_title(firm_name: str) -> None:
    owner_title = f"<< {firm_name} >>"
    print(f"{owner_title:^40}")

    owner_date = f"ESTD: {get_firm_date(firm_name)}"
    print(f"{owner_date:^40}")


def main() -> None:
    # Storing owners name into a variable (required by lab)
    firm = "Nest Properties"

    # Probably shouldn't have made these global variables, but whatever
    get_property_info()
    get_firm_info()
    get_location_info()

    print_title(firm)

    # Get the summary of all properties in each location for the firm
    for location in location_list:
        location_asset_summary(firm, location)


    # Getting the last bit of the summary
    total_properties = get_total_properties(firm)
    total_networth = get_networth(firm)

    print(f"\nTotal properties owned: {total_properties:>15}")
    print(f"Net worth of Firm: $ {total_networth:>18,.2f}")


if __name__ == "__main__":
    main()

