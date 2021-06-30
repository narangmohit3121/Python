def find_largest_sum(arr:list):
    prev_negative_index = 0
    max_val = 0
    current_sum = 0
    for index, current_val in enumerate(arr):
        if (current_sum < 0) and (current_val) > 0:
            current_sum = 0
        if current_val < 0:
            prev_negative_index = index
        current_sum += current_val
        if current_sum > 0 and current_sum > max_val:
            max_val = current_sum

    return max_val


print(find_largest_sum([7, 5, -1, -2, -4, 5, -3, -7, -6, 5, -2, -1, 1, 3, 5, 5, -3, 8, -7, 2]))


def find_missing_element(arr1: list, arr2: list):
    sum1 = 0
    sum2 = 0

    for elem in arr1:
        sum1 += elem
    for elem in arr2:
        sum2 += elem

    return sum1 - sum2


def find_missing_element_with_dict(arr1: list, arr2: list):
    consolidated_dict:dict = {}

    for elem in arr1:
        print(consolidated_dict.get(elem))
        if consolidated_dict.get(elem) is None:
            consolidated_dict[elem] = 1
        else:
            count_of_elem = consolidated_dict[elem] + 1
            consolidated_dict[elem] = count_of_elem

    for elem in arr2:
        if consolidated_dict.get(elem) is None:
            consolidated_dict[elem] = 1
        else:
            count_of_elem = consolidated_dict[elem] + 1
            consolidated_dict[elem] = count_of_elem
    print(consolidated_dict.items())
    for (key, val) in consolidated_dict.items():
        if val % 2 != 0:
            return key


print(find_missing_element_with_dict([7, 5, -1, -2, -4, 5, -7, -6, 5, -2, -1, 1, 3, 5, 5, -3, 8, -7, 2],
                                     [7, 5, -1, -2, -4, 5, -3, -7, -6, 5, -2, -1, 1, 3, 5, 5, -3, 8, -7, 2]))

