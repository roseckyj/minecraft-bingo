import errno
import json
import os
import random


def getFilename(x, y):
    return ["d", "b", "c", "a", "e"][y] + str(x + 1) + str(y + 1)

with open('items.json') as json_file:
    raw = json.load(json_file)

    data = {}
    categories = []

    print("Select categories of items:")
    
    for category in raw.keys():
        selected = True
        reply = input(" - " + category + " (" + ("Y/n" if selected else "y/N")  + "): ")
        if (reply != ""):
            if (reply.lower().startswith("y")):
                selected = True
            else:
                selected = False

        if selected:
            data = {**data, **raw[category]}
            categories.append(category)
    
    print()
    print("Generating datapack with following categories:")
    print(" " + (", ".join(categories)))

    keys = list()
    for i in data.keys():
        keys.append(i)

    random.shuffle(keys)

    i = 0

    for x in range(5):
        for y in range(5):
            filename = "data/bingo/advancements/" + getFilename(x, y) + ".json"
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
                                "text": "''' + data[keys[i]] + '''"
                            },
                            "description": {
                                "text": "Obtain ''' + data[keys[i]] + '''",
                                "color": "white"
                            },
                            "icon": {
                                "item": "''' + keys[i] + '''"
                            },
                            "frame": "''' + ("challenge" if x == y or x + y == 4 else "task") + '''",
                            "show_toast": true,
                            "announce_to_chat": true,
                            "hidden": false
                        },
                        "criteria": {
                            "''' + keys[i].split(":")[1] + '''": {
                                "trigger": "minecraft:inventory_changed",
                                "conditions": {
                                    "items": [
                                        {
                                            "item": "''' + keys[i] + '''"
                                        }
                                    ]
                                }
                            }
                        },
                        "rewards": {
                            "function": "bingo:check"
                        },
                        "parent": "''' + ('bingo:root' if (x == 0) else 'bingo:' + getFilename(x - 1, y)) + '''"
                    }
                ''')
            i += 1

    print()
    print("Done, you can now start playing.")
    print("Each player has to dig one dirt in order to start the game.")
    print("You can then view your BINGO by pressing L")
    print()
