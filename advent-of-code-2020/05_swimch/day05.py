file = []
with open('input.txt', 'r') as f:
    for line in f:
        file.append(line[:-1])

seats = []
for i in range(1, 127):  # Part 2
    for j in range(8):
        seats.append((i, j))

seat_ids = []
for line in file:
    rows = [i for i in range(128)]
    columns = [i for i in range(8)]
    for instr in line[:-3]:
        if instr == "B":
            rows = rows[int(len(rows) / 2):]
        else:
            rows = rows[:int(len(rows) / 2)]
    for instr in line[-3:]:
        if instr == "L":
            columns = columns[:int(len(columns) / 2)]
        else:
            columns = columns[int(len(columns) / 2):]
    seat_ids.append(rows[0] * 8 + columns[0])
    if 0 < rows[0] < 127:  # Part 2
        seats.remove((rows[0], columns[0]))

### Part 1 ###
print(f"The highest seat id is: {sorted(seat_ids)[-1]}")

### Part 2 ###
for seat in seats:
    if (seat[0] * 8 + seat[1] + 1) in seat_ids and (seat[0] * 8 + seat[1] - 1) in seat_ids:
        print(f"My seat is in row {seat[0]}, column {seat[1]} and has the seat id {seat[0] * 8 + seat[1]}")
