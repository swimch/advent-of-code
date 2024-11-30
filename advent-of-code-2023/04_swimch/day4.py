import re

input_data = []
with open('input.txt', 'r') as f:
    for line in f:
        input_data.append(line[10:-1])

cards = {}
total_score = 0

for count, line in enumerate(input_data):
    numbers = line.split(" | ")
    winning = re.split("  | ",numbers[0])
    winning.remove("") if len(winning) > 10 else True
    have = re.split("  | ",numbers[1])
    have.remove("") if len(have) > 25 else True
    score = 0
    matches = -1
    for number in winning:
        if number in have:
            matches += 1
    score = 2**matches if matches != -1 else 0
    total_score += score
    card = {
        "winning": winning,
        "have": have,
        "score": score,
        "matches": matches + 1,
        "runs_remaining": 1
    }
    cards[(count+1)] = card
print(total_score)

runs_total = 0
for win_for_life in cards:
    while cards[win_for_life]["runs_remaining"] > 0:
        for i in range(1, cards[win_for_life]["matches"]+1):
            cards[win_for_life+i]["runs_remaining"] += 1
        runs_total += 1
        cards[win_for_life]["runs_remaining"] -= 1
print(runs_total)