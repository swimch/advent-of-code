input = [int(stone) for stone in open("input.txt", "r").readline().split()]

def stone_change(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        return [int(str(stone)[:len(str(stone)) // 2]), int(str(stone)[len(str(stone)) // 2:])]
    return [stone * 2024]


def part2(stones, blinks):
    # only have to find the change once per number, can apply this to all identical stones
    # order is irrelevant
    stones = {stone: 1 for stone in stones} # assumes that every stone is unique at the start
    for i in range(blinks):
        # save new stones to new dictionary so stones doesn't change while iterating through it
        new_stones = {}
        for stone in stones:
            for new_stone in stone_change(stone):
                if new_stone in new_stones:
                    new_stones[new_stone] += stones[stone]
                else:
                    new_stones[new_stone] = stones[stone]
        stones = new_stones
    return sum([count for count in stones.values()])

print(f"There are {part2(input, 25)} stones after blinking 25 times")
print(f"There are {part2(input, 75)} stones after blinking 75 times")
