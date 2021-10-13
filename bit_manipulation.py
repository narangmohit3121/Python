import random
from collections import OrderedDict


def find_subsets(items: list):
    for k in range(1 << len(items)):
        for i in range(len(items)):
            if k & 1 << i != 0:
                print(items[i], end=" ")

        print()


def generate_list(n: int):
    list_of_items = []
    for i in range(n):
        list_of_items.append(random.randint(0, 100))
    return list_of_items


def count_of_bits(num):
    count = 0
    while num > 0:
        num &= num - 1
        count += 1
    return count


# print(count_of_bits(8))


def find_min_cost(cost_array: list):
    costs = [float("Inf")]*(1 << len(cost_array))
    costs[0] = 0
    for k in range(1 << len(cost_array)):
        i = count_of_bits(k)
        for j in range(len(cost_array)):
            # AND operation of k and left shift of 1 to j positions - This will give us whether task is assigned at jth
            # position
            if (k & 1 << j) != 0:
                # AND operation of k and inversion of left shift of 1 to j positions - This will unset the bit at jth
                # position
                costs[k] = min(costs[k], costs[k & ~(1 << j)] + cost_array[i-1][j])
            # print(costs)

    print(costs)


def find_min_cost_with_assignments(cost_array: list):
    costs = {}
    costs[0] = {"min": 0, "path": []}
    for x in range(1, 1 << len(cost_array)):
        costs[x] = {"min": float("Inf"), "path": []}
    for k in range(1 << len(cost_array)):

        i = count_of_bits(k)
        for j in range(len(cost_array)):
            # AND operation of k and left shift of 1 to j positions - This will give us whether task is assigned at jth
            # position
            if (k & 1 << j) != 0:
                # AND operation of k and inversion of left shift of 1 to j positions - This will unset the bit at jth
                # position
                current_cost = costs[k & ~(1 << j)]["min"] + cost_array[i-1][j]
                # print("Current cost:", current_cost)
                if costs[k]["min"] > current_cost:
                    costs[k]["min"] = current_cost
                    costs[k]["path"] = list(costs[k & ~(1 << j)]["path"])
                    if(len(costs[k]["path"])) > 0 and (len(costs[k]["path"])) == i:
                        costs[k]["path"].pop()
                    costs[k]["path"].append((i, j + 1))

        # print(costs)

    print(costs)


cost_arr = [generate_list(5) for i in range(5)]
for current_task_costs in cost_arr:
    print(current_task_costs)

find_min_cost_with_assignments(cost_arr)

# print(min(float("Inf"), 1))