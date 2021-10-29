def chicago_inventory():
    import os
    if os.path.exists("Full_Inventory.csv"):
        os.remove("Full_Inventory.csv")
    old_file = open(r"CHI_Inventory.csv", "r")
    new_file = open(r"Full_Inventory.csv", "a")
    for index, line in enumerate(old_file):
        if index != 0:
            new_file.write(chicago_construct_line(line))
    old_file.close()
    new_file.close()


def chicago_construct_line(line):
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
            if comma_counter == 2:
                username = username + character
            elif comma_counter >= 9:
                break
        else:
            if comma_counter == 1 or comma_counter == 2:
                username = username + character
            elif comma_counter == 4:
                tag = tag + character
            elif comma_counter == 5:
                sn = sn + character
            elif comma_counter == 6:
                model = model + character
            elif comma_counter == 7:
                eol = eol + character
            elif comma_counter == 8:
                comments = comments + character
    rv = username + "," + tag + "," + sn + "," + model + "," + eol + "," + comments + ",\n"
    return rv


if __name__ == '__main__':
    chicago_inventory()

