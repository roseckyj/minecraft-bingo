import json
import os
import errno
import random

def getFilename(x, y):
    return ["a", "b", "c", "d", "e"][y] + str(x + 1) + str(y + 1)

with open('items.json') as json_file:
    settingsok = False
    mapok = False

    data = json.load(json_file)

    keys = list()
    # Put all the keys in a list
    for key in data.keys():
        keys.append(key)

    while not settingsok:
        # Give the user the option to select only dimensions they want (overworld, nether, end)
        dimensions = input("Enter the dimensions you want to include (all by default) - (O)verworld, (N)ether, (E)nd: ").upper()
        dimensions_list = []
        if "O" in dimensions:
            dimensions_list.append("overworld")
        if "N" in dimensions:
            dimensions_list.append("nether")
        if "E" in dimensions:
            dimensions_list.append("end")
        if len(dimensions_list) == 0:
            dimensions_list = ["overworld", "nether", "end"]

        # Allow user to select min and max difficulty (number from 0 to 1000, empty is 0 for min and 1000 for max), parse the input to a number
        min_difficulty = input("Enter the minimum difficulty 0-1000 (uncaped by default): ")
        if min_difficulty == "":
            min_difficulty = 0
        else:
            min_difficulty = int(min_difficulty)

        max_difficulty = input("Enter the maximum difficulty 0-1000 (uncaped by default): ")
        if max_difficulty == "":
            max_difficulty = 1000
        else:
            max_difficulty = int(max_difficulty)
        
        # Make sure the directory exists
        if not os.path.exists("data/bingo/advancement/generated/"):
            try:
                os.makedirs("data/bingo/advancement/generated/")
            except OSError as exc: # Guard against
                if exc.errno != errno.EEXIST:
                    raise

        mapok = False
        while not mapok:
            print()
            print("Generated bingo card:")
            print()
            print(("+-" + ("-" * 21)) * 5 + "+")

            random.shuffle(keys)
            i = 0

            for y in range(5):
                print("| ", end="")
                for x in range(5):
                    # Look at the item i and check, if the dimension and difficulty are correct
                    key = keys[i]
                    row = data[key]
                    while row["dimension"] not in dimensions_list or row["difficulty"] < min_difficulty or row["difficulty"] > max_difficulty:
                        i += 1
                        if i >= len(keys):
                            print("Not enough items to fill the board, try again with different settings.")
                            exit(1)

                        key = keys[i]
                        row = data[key]


                    filename = "data/bingo/advancement/generated/" + getFilename(x, y) + ".json"
                    if not os.path.exists(os.path.dirname(filename)):
                        try:
                            os.makedirs(os.path.dirname(filename))
                        except OSError as exc: # Guard against race condition
                            if exc.errno != errno.EEXIST:
                                raise
                        
                    with open(filename, "w") as output:
                        output.write('''
                            {
                                "display": {
                                    "title": {
                                        "translate": "''' + row["display"] + '''"
                                    },
                                    "description": {
                                        "translate": "Obtain ''' + row["display"] + '''",
                                        "color": "white"
                                    },
                                    "icon": {
                                        "id": "''' + key + '''"
                                    },
                                    "frame": "challenge",
                                    "show_toast": true,
                                    "announce_to_chat": true,
                                    "hidden": false
                                },
                                "criteria": {
                                    "''' + key.split(":")[1] + '''": {
                                        "trigger": "minecraft:inventory_changed",
                                        "conditions": {
                                            "items": [
                                                {
                                                    "items": ["''' + key + '''"]
                                                }
                                            ]
                                        }
                                    }
                                },
                                "rewards": {
                                    "function": "bingo:check"
                                },
                                "parent": "''' + ('bingo:root' if (x == 0) else 'bingo:generated/' + getFilename(x - 1, y)) + '''",
                                "requirements": [
                                    [
                                        "''' + key.split(":")[1] + '''"
                                    ]
                                ]
                            }
                        ''')
                    i += 1

                    # Print the item name trimmed to 20 characters and padded with spaces
                    print(row["display"][:20].ljust(20), end=" | ")

                # Add newline after each row
                print()
                print(("+-" + ("-" * 21)) * 5 + "+")

            # Check if the user is happy with the result
            print()
            print("Generate again? (N)o, the map is good! (y)es with the same settings, (m)odify the settings and try again:")
            generate_again = input().upper()
            if generate_again == "N":
                mapok = True
                settingsok = True
            elif generate_again == "Y":
                mapok = False
                settingsok = True
            elif generate_again == "M":
                settingsok = False
                mapok = True
            else:
                mapok = True
                settingsok = True



    print()
    print("Done, you can now start playing.")
    print("Each player has to dig one dirt in order to start the game.")
    print("You can then view your BINGO by pressing L")
    print()
