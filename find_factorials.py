import math


def find_fact(num):
    facts = {}
    current_divisor = 2
    max_divisor = num//2 + 1
    while (num > 1) and (current_divisor < max_divisor):

        if prime_check(current_divisor):
            current_fact_count = 0
            while num % current_divisor == 0:
                current_fact_count += 1
                num = num // current_divisor
                # print(num)
            if current_fact_count > 0:
                facts[current_divisor] = current_fact_count
        current_divisor += 1
    return facts


def prime_check(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        is_prime = True
        max_denominator = math.ceil(math.sqrt(num))
        # print(max_denominator)
        for i in range(2, max_denominator + 1):
            if num % i == 0:
                is_prime = False
                break
        return is_prime


# print(prime_check(21))
print(find_fact(21))
print(find_fact(24))
print(find_fact(12345))
print(find_fact(100000))