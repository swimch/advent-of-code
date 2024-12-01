input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])

location1, location2 = [], []

for line in input:
    location1.append(line.split()[0])
    location2.append(line.split()[1])

location1.sort()
location2.sort()

difference = 0
for i in range(len(location1)):
    difference += abs(int(location1[i]) - int(location2[i]))

similarity = 0
for location in location1:
    similarity += location2.count(location) * int(location)

print(difference)
print(similarity)