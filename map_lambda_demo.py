numbers = (1, 2, 3, 4)


def double(x):
    return 2*x


result = map(double, numbers)
result_via_lambda = map(lambda a: 2*a, numbers)

print(list(result))
print(list(result_via_lambda))
