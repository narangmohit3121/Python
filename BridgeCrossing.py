import time


def bridge_crossing(people):
    pairs = set()
    time_to_cross = {}
    for person1 in people:
        for person2 in people:
            if person1 != person2:
                # print(person1, person2)
                current_pair = sorted(person1 + person2)
                pairs.add("".join(current_pair))
    # print(pairs)
    for pair in pairs:
        # p1 = pair.split("")[0]
        # p2 = pair.split("")[1]
        pair_crossing_time = people[pair[0]] if people[pair[0]] > people[pair[1]] else people[pair[1]]
        time_to_cross[pair] = pair_crossing_time

    # people.update(time_to_cross)
    # print(people)
    return time_to_cross


i = 0


def find_path_combinations(people_list, pair_crossing_times, all_paths, is_done=False):
    global i
    if not is_done:
        extended_paths = []
        if len(all_paths) > 0:
            current_paths = all_paths
            done = True
            for current_path in current_paths:
                # print("Current_path", current_path)
                if len(set(people_list.keys()) - set(list(current_path[1]))) > 0:
                    path = current_path[0]
                    # print(path)
                    already_crossed = current_path[1]
                    # print(already_crossed)
                    possible_paths = []
                    for pair in pair_crossing_times:
                        already_crossed_string = "".join(already_crossed)
                        if pair[0] in already_crossed_string or pair[1] in already_crossed_string:
                            pass
                        else:
                            possible_paths.append(pair)
                    # print('possible paths', possible_paths)
                    if len(possible_paths) > 0:
                        done = False
                        for new_pair in possible_paths:
                            new_path = list(path)
                            new_path.append(new_pair)
                            # print('new path', new_path)
                            t1 = people_list[new_pair[0]]
                            t2 = people_list[new_pair[1]]
                            new_already_crossed = already_crossed + (new_pair[0] if t1 > t2 else new_pair[1])
                            extended_paths.append([new_path, new_already_crossed])
                        # print('extended paths', extended_paths)
                    else:
                        extended_paths.append(current_path)
                    # time.sleep(1)
            # if not done:
            i += 1
            print('extended paths', extended_paths)
            print(f'Entering recursion {i}')
            return find_path_combinations(people_list, pair_crossing_times, extended_paths, done)

        else:
            for current_pair in pair_crossing_times.keys():
                t1 = people_list[current_pair[0]]
                t2 = people_list[current_pair[1]]
                new_path = [current_pair]
                extended_paths.append([new_path, current_pair[0] if t1 > t2 else current_pair[1]])
            print(extended_paths)
            return find_path_combinations(people_list, pair_crossing_times, extended_paths)
    else:
        i += 1
        print(f'Closing {i}', all_paths)
        return all_paths
    # i += 1
    #
    # print(f'Exiting recursion {i}', all_paths)


people_to_cross = {
    'A': 1,
    'B': 2,
    'C': 5,
    'D': 10,
    'E': 12
}

bridge_crossing(people_to_cross)
paths = find_path_combinations(people_to_cross, bridge_crossing(people_to_cross), [])
print('all paths main', paths)
