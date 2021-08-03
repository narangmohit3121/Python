import shelve
import pickle
locations = {0: "You are sitting in front of the computer",
             1: "You are on the road",
             2: "You are on the hill",
             3: "You are in front of the building",
             4: "You are in the valley",
             5: "You are in the forest"
             }

exits = {
         1: {"N": 5, "E": 3, "S": 4, "W": 2, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"S": 1, "W": 2, "Q": 0}
         }

directions = {'North': 'N',
              'South': 'S',
              'West': 'W',
              'East': 'E'
              }
currentLocation = 1

# while True:
#     print(locations.get(currentLocation))
#     print("Press q to quit")
#     directionChosen = input("Choose a direction to Continue: ")
#     print('The direction you have chosen is {0}'.format(directionChosen.upper()))
#
#     if directionChosen.upper() in exits.get(currentLocation):
#         currentLocation = exits.get(currentLocation).get(directionChosen.upper())
#     elif directionChosen == 'q' or directionChosen == 'Q':
#         break
#     else:
#         print("No path to that particular direction. Choose another direction")

with open('DirectionBinary', 'wb') as directionBinary:
    pickle.dump(locations, directionBinary)
    pickle.dump(exits, directionBinary)
    pickle.dump(directions, directionBinary)
