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


exits_to_forest = [locations.get(key) if 5 in val.values() else key for key, val in exits.items()]
exits_to_forest_2 = [locations.get(key) for key, val in exits.items() if 5 in val.values()]

print(exits_to_forest)

burgers = ["burgerOne", "burgerTwo", "burgerThree", "burgerFour"]

toppings = ["toppingOne", "toppingTwo", "toppingThree", "toppingFour"]

print([[(topping, burger) for topping in toppings] for burger in burgers])
