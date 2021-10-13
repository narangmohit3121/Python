def fibonacci():
    current, previous = 1, 1
    while True:
        yield current
        current, previous = current + previous, current
        # print("previous", previous)


fib = fibonacci()

# for i in range(1, 30):
#     print(next(fib))


def odd_numbers():
    odd_number = 1
    while True:
        yield odd_number
        odd_number += 2


odds = odd_numbers()
print(odds)
# for i in range(1, 30):
#     print(next(odds))


def define_pi():
    pi_val = 0
    odd_num = odd_numbers()
    while True:
        pi_val += 4/next(odd_num)
        yield pi_val

        pi_val -= 4/next(odd_num)
        yield pi_val


pi = define_pi()

# for i in range(100000):
#     print(next(pi))

