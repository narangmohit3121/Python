def find_factorial(number):
    if number <= 1:
        return 1
    else:
        return number*find_factorial(number - 1)


# for index, num in enumerate(range(1, 20)):
#     print("The factorial for {0} is {1}".format(index, find_factorial(num)))


dummy = "test_string"
# print(dummy[:2] + dummy[3:])


def print_word_combinations(word: str) -> str:
    word_combinations:set = set()
    if len(word) == 2:
        word_combinations.add(word)
        word_combinations.add(word[::-1])
    else:
        for index, current_char in enumerate(word):
            index_char = word[index]
            print(index, index_char)
            remaining_char = word[:index] + word[index + 1:]
            remaining_char_combo = print_word_combinations(remaining_char)
            for current_str in remaining_char_combo:
                word_combinations.add(index_char + current_str)

    return word_combinations


# test = print_word_combinations("aacd")
# print(test)
# print(len(test))


def print_string_combinations(list_of_words: list):
    string_combos = set()
    if len(list_of_words ) > 2:
        for index, word in enumerate(list_of_words):
            temp_list = list(list_of_words)
            current_word = temp_list.pop(index)
            temp_list_combos = print_string_combinations(temp_list)
            for current_combo in temp_list_combos:
                string_combos.add(current_word + current_combo)
                string_combos.add(current_combo)
    elif len(list_of_words) == 2:
        string_combos.add(list_of_words[0] + list_of_words[1])
        string_combos.add(list_of_words[1] + list_of_words[0])
    else:
        string_combos.add(list_of_words[0])

    return string_combos


def reverse_string_recursion(input):
    rev = ""
    if len(input) > 2:
        return reverse_string_recursion(input[1:]) + input[0]
    if len(input) == 2:
        return input[1] + input[0]


def get_fibonacci_num(input):
    if input > 1:
        return get_fibonacci_num(input - 1) + get_fibonacci_num(input - 2)
    else:
        return input


print(print_string_combinations(["Im", "Love", "Electronic"]))
print(reverse_string_recursion("Hello World! Welcome to the jungle"))

for index in range(20):
    print(f"fibonacci number for {index} is {get_fibonacci_num(index)} ")
