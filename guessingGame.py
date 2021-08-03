import  random
a = "test"


def guess_answer(low: int, high: int, correct_answer: int) -> None:

    """
    This function tries to find the answer in a range by making a number of guesses
    :param low:The lower end of the range
    :param high: The higher end of the range
    :param correct_answer: The answer that must be guessed
    :return:
    """
    if isinstance(correct_answer,int):
        number_of_guesses = 0
        while True:
            # guess = random.randint(low, high)
            guess = (low + high)//2
            print('Current guess is {0}'.format(guess))
            if guess > correct_answer:
                print("Guess should be lower")
                high = guess - 1
            elif guess < correct_answer:
                print('Guess should be lower')
                low = guess + 1
            else:
                print("Correct answer guessed in {0} number of guesses".format(number_of_guesses))
                break;
            number_of_guesses += 1
    else:
        raise ValueError("The correct answer should be a number")
    return None


LOW = 1
HIGH = 1000

guess_answer(correct_answer=456, high=HIGH, low=LOW)
