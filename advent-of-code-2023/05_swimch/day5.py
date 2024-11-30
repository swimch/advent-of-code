almanach = {}
with open('test.txt', 'r') as f:
    for line in f:
        if len(line) > 4 and line[4] == "s":
            seeds = line[7:-1].split(" ")
        elif line[0].isalpha():
            category_name = line[:-1].split(":")[0]
            almanach[category_name] = []
        elif line[0].isdigit():
            almanach[category_name].append(line[:-1].split(" "))


def search_destination(source_f, category_f):
    for count, map_f in enumerate(almanach[category_f]):
        difference = source_f - int(almanach[category_f][count][1])
        if 0 <= difference <= int(almanach[category_f][count][2]):
            destination = int(almanach[category_f][count][0]) + difference
            return destination
    destination = source_f
    return destination


locations = []
for seed in seeds:
    source = int(seed)
    for category in almanach:
        source = search_destination(source, category)
    locations.append(source)

print(f"the nearest location is: {min(locations)}")


def search_destination_2(source_pairs_f, category_f):
    destinations_f = []
    print(f"The source pairs are: {source_pairs_f}")
    check = True
    while source_pairs_f:
        if not check:
            destinations_f.append(source_pair_f)
            print("hehe4")
        source_pair_f = source_pairs_f.pop()
        print(f"After popping the remaining source pairs are: {source_pairs_f}")
        source_lower = int(source_pair_f[0])
        source_upper = int(source_pair_f[1])
        print(f"Source pair: {source_pair_f}")
        print(f"Source lower and upper: {source_lower}, {source_upper}")
        check = False
        for count, map_f in enumerate(almanach[category_f]):
            print(f"The destinations are: {destinations_f}")
            map_range = int(almanach[category_f][count][2]) - 1
            map_lower = int(almanach[category_f][count][1])
            map_upper = int(almanach[category_f][count][1]) + map_range
            print(f"Map range: {map_range}\nMap lower: {map_lower}\nMap upper: {map_upper}")
            destination_lower = int(almanach[category_f][count][0])
            destination_upper = int(almanach[category_f][count][0]) + map_range
            difference_lower = source_lower - map_lower
            difference_upper = source_upper - map_lower
            print(f"Destination upper: {destination_upper}\nDestination lower: {destination_lower}\nDifference lower: {difference_lower}\nDifference upper: {difference_upper}")
            # source completely in range
            if source_lower >= map_lower and source_upper <= map_upper:
                destinations_f.append([destination_lower + difference_lower, destination_lower + difference_upper])
                print("hehe")
                check = True
                break
            # range completely in source
            elif source_lower < map_lower and source_upper > map_upper:
                destinations_f.append([destination_lower, destination_upper])
                source_pairs_f.append([source_lower, map_lower - 1])
                source_pairs_f.append([map_upper + 1, source_upper])
                check = True
                break
            # source upper out of range
            elif source_lower <= map_upper < source_upper:
                destinations_f.append([source_lower + difference_lower, destination_upper])
                source_pairs_f.append([map_upper + 1, source_upper])
                print("hehe2")
                check = True
                break
            # source lower out of range
            elif source_lower < map_lower <= source_upper:
                destinations_f.append([destination_lower, source_upper + difference_upper])
                source_pairs_f.append([source_lower, map_lower - 1])
                print("hehe3")
                check = True
                break
        # else source completely out of range
    if not check:
        destinations_f.append(source_pair_f)
    return destinations_f


source_pairs = []
for i in range(0, len(seeds), 2):
    source_pairs.append([int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]) - 1])

for category in almanach:
    print(category)
    source_pairs = search_destination_2(source_pairs, category)
    print(f"source pairs after function (input for later): {source_pairs}")

destinations = []
for source in source_pairs:
    destinations.append(int(source[1]))
print(destinations)
print(min(destinations))
