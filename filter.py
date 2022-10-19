import json
import os
import errno
import random

sorted = []
unsorted = {}

with open('items.json') as items_file:
    items = json.load(items_file)

    for category in items.keys():
        sorted = sorted + list(items[category].keys())

with open('everything.json') as everything_file:
    everything = json.load(everything_file)

    for item in everything.keys():
        if item not in sorted:
            unsorted[item] = everything[item]

with open("unsorted.json", "w") as outfile:
    json.dump(unsorted, outfile)