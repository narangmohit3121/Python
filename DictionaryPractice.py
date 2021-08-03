directions = {'North': 'N',
              'South': 'S',
              'West': 'W',
              'East': 'E'
              }

for direction in directions.keys():
    print(direction)


def make_dictionary(**kwargs):
    return kwargs


print(make_dictionary(one='one', two='2', three=3))
