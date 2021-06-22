def find_factorial(number):
    if number <= 1:
        return 1
    else:
        return number*find_factorial(number - 1)


for index, num in enumerate(range(1, 20)):
    print("The factorial for {0} is {1}".format(index, find_factorial(num)))


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


test = print_word_combinations("aacd")
print(test)
print(len(test))