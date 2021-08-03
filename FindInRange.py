data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
data.sort()
print(data)
minValue = 100
maxValue = 200

frontIndex = 0
backIndex = 0
for value in data:
    if(value >= minValue):
        break
    frontIndex += 1
print(data[frontIndex:])

for index in range(len(data)-1, -1, -1):
    if(data[index] <= maxValue):
        break
    backIndex -= 1
print(data[:backIndex])
print(data[frontIndex:backIndex])

