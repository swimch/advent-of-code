input_data = []
hands = []
hands_j = []
with open('input.txt', 'r') as f:
    for line in f:
        input_data.append(line[:-1].split())

mapping_table = str.maketrans({'A': "14", 'K': '13', 'Q': '12', 'J': '11', 'T': '10'})
mapping_table_j = str.maketrans({'A': "14", 'K': '13', 'Q': '12', 'J': '0', 'T': '10'})
for line in input_data:
    hand = {
        "hand": [x for x in line[0]],
        "bid": int(line[1]),
        "rank": 0,
    }
    hand_j = {
        "hand": [x for x in line[0]],
        "bid": int(line[1]),
        "rank": 0,
    }
    for count, card in enumerate(line[0]):
        hand[str(count)] = int(card.translate(mapping_table))
        hand_j[str(count)] = int(card.translate(mapping_table_j))
    hands.append(hand)
    hands_j.append(hand_j)


def find_type(hand_f):
    type_counter = 0
    cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    # count occurrences in hand and add a value, sum gives us the type
    # high cards = 0, pair = 1, 2 pair = 2, 3 of a kind = 3, full house = 4, 4 of a kind = 5, 5 of a kind = 6
    for i in cards:
        if hand_f.count(i) == 2:
            type_counter += 1
        elif hand_f.count(i) == 3:
            type_counter += 3
        elif hand_f.count(i) == 4:
            type_counter += 5
        elif hand_f.count(i) == 5:
            type_counter += 6
    return type_counter


def find_type_j(hand_f):
    type_counter = 0
    cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    if "J" in hand_f:
        for j_card in cards:
            j_hand = [card_f.replace("J", j_card) for card_f in hand_f.copy()]
            # count occurrences in hand and add a value, sum gives us the type
            # high cards = 0, pair = 1, 2 pair = 2, 3 of a kind = 3, full house = 4, 4 of a kind = 5, 5 of a kind = 6
            type_counter_j = 0
            for i in cards:
                if j_hand.count(i) == 2:
                    type_counter_j += 1
                elif j_hand.count(i) == 3:
                    type_counter_j += 3
                elif j_hand.count(i) == 4:
                    type_counter_j += 5
                elif j_hand.count(i) == 5:
                    type_counter_j += 6
            type_counter = type_counter_j if type_counter < type_counter_j else type_counter
    else:
        type_counter = find_type(hand_f)
    return type_counter


for hand in hands:
    hand["type"] = find_type(hand["hand"])
sorted_hands = sorted(hands, key=lambda e: (e["type"], e["0"], e["1"], e["2"], e["3"], e["4"]))
winnings = 0
for count, hand in enumerate(sorted_hands):
    hand["rank"] = count + 1
    winnings += hand["rank"] * hand["bid"]
print(winnings)

for hand in hands_j:
    hand["type"] = find_type_j(hand["hand"])
sorted_hands_j = sorted(hands_j, key=lambda e: (e["type"], e["0"], e["1"], e["2"], e["3"], e["4"]))
winnings = 0
for count, hand in enumerate(sorted_hands_j):
    hand["rank"] = count + 1
    winnings += hand["rank"] * hand["bid"]
print(winnings)
# got 248696167, too low
