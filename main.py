def inventory_builder():
    import os
    if os.path.exists("Full_Inventory.csv"):
        os.remove("Full_Inventory.csv")
    # Chicago
    old_file = open(r"CHI_Inventory.csv", "r")
    new_file = open(r"Full_Inventory.csv", "a")
    for index, line in enumerate(old_file):
        if index != 0:
            new_file.write(construct_line(line, [1, 2, 4, 5, 6, 7, 8], 0))
    old_file.close()
    new_file.close()

    # New York
    old_file = open(r"NYC_Inventory.csv", "r")
    new_file = open(r"Full_Inventory.csv", "a")
    for index, line in enumerate(old_file):
        if "RETIRED" in line:
            break
        if index != 0:
            new_file.write(construct_line(line, [0, 1, 2, 4, 5, 6, 7], 1))
    old_file.close()
    new_file.close()

    # Washington DC
    old_file = open(r"WDC_inventory.csv", "r")
    new_file = open(r"Full_Inventory.csv", "a")
    for index, line in enumerate(old_file):
        if "RETIRED" in line:
            break
        if index != 0:
            new_file.write(construct_line(line, [0, 1, 3, 4, 5, 7, 8], 2))
    old_file.close()
    new_file.close()

    # Dallas
    old_file = open(r"DAL_Inventory.csv", "r")
    new_file = open(r"Full_Inventory.csv", "a")
    for index, line in enumerate(old_file):
        if "RETIRED" in line:
            break
        if index != 0:
            new_file.write(construct_line(line, [0, 1, 3, 4, 5, 7, 8], 3))
    old_file.close()
    new_file.close()

    # Atlanta
    old_file = open(r"ATL_Inventory.csv", "r")
    new_file = open(r"Full_Inventory.csv", "a")
    for index, line in enumerate(old_file):
        if "RETIRED" in line:
            break
        if index != 0:
            new_file.write(construct_line(line, [0, 1, 3, 4, 5, 7, 8], 4))
    old_file.close()
    new_file.close()

    # Raleigh
    old_file = open(r"RAL_Inventory.csv", "r")
    new_file = open(r"Full_Inventory.csv", "a")
    for index, line in enumerate(old_file):
        if "RETIRED" in line:
            break
        if index != 0:
            new_file.write(construct_line(line, [0, 1, 3, 4, 5, 7, 8], 5))
    old_file.close()
    new_file.close()


def normalize_names(line, start_index):
    comma_counter = 0
    found_space = False
    firstname = ""
    lastname = ""
    rest_of_line = ""
    for i in range(start_index, len(line)):
        character = line[i]
        if character == "\"":
            return line
        elif comma_counter > 0:
            rest_of_line = rest_of_line + character
        elif character == ",":
            comma_counter = comma_counter + 1
        elif character == " ":
            found_space = True
        elif not found_space:
            firstname = firstname + character
        elif found_space:
            lastname = lastname + character
    rv = "\"" + lastname + ", " + firstname + "\"" + "," + rest_of_line
    return rv


def construct_line(line, comma_locations, city_index):
    name_start_index = 0
    for i in range(0, len(line)):
        character = line[i]
        if character == "\"":
            name_start_index = i
            break
    line = normalize_names(line, name_start_index)

    comma_counter = 0
    username = ""
    tag = ""
    sn = ""
    model = ""
    eol = ""
    comments = ""
    for i in range(0, len(line)):
        character = line[i]
        if character == ",":
            comma_counter = comma_counter + 1
            if comma_counter == comma_locations[1]:
                username = username + character
            elif comma_counter > comma_locations[6]:
                break
        else:
            if comma_counter == comma_locations[0] or comma_counter == comma_locations[1]:
                username = username + character
            elif comma_counter == comma_locations[2]:
                tag = tag + character
            elif comma_counter == comma_locations[3]:
                sn = sn + character
            elif comma_counter == comma_locations[4]:
                model = model + character
            elif comma_counter == comma_locations[5]:
                eol = eol + character
            elif comma_counter == comma_locations[6]:
                comments = comments + character
    rv = username + "," + tag + "," + sn + "," + model + "," + eol + "," + comments + ",\n"

    city = ""
    if city_index == 0:
        city = "CHI,"
    elif city_index == 1:
        city = "NYC,"
    elif city_index == 2:
        city = "WDC,"
    elif city_index == 3:
        city = "DAL,"
    elif city_index == 4:
        city = "ATL,"
    elif city_index == 5:
        city = "RAL,"

    rv = city + rv

    return rv


if __name__ == '__main__':
    inventory_builder()

