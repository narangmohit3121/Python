import pickle

with open('DirectionBinary', 'rb') as directionBin:
    locations = pickle.load(directionBin)
    for key in locations.keys():
        print(key)
    # print(locations)
    exits = pickle.load(directionBin)
    print(exits)
    for currentLocation in exits:
        availableExits = exits.get(currentLocation)
        for direction in availableExits:
            print(availableExits.get(direction), end='::')

