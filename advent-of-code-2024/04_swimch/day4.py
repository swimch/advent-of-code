input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])


def direction_search(pos, direction, char_ind):
    next_char = "XMAS"[char_ind]
    x, y = (pos[0] + direction[0], pos[1] + direction[1]) # next position in defined direction
    if 0 <= x < len(input) and 0 <= y < len(input[0]): # to stay in index
        if input[x][y] == next_char:
            if next_char == "S": # Stop condition for recursion
                return 1
            else:
                return direction_search((x,y), direction, char_ind + 1) # Recursion! :)
    return 0


xmas, xmas2 = 0, 0
for i, row in enumerate(input):
    for j, char in enumerate(row):
        if char == "X":
            for k in range(-1, 2): # checking all directions with k and l
                for l in range(-1, 2):
                    xmas += direction_search((i, j), (k, l), 1)
        if char == "A" and 0 < i < len(input)-1 and 0 < j < len(input[0])-1:
            ul = input[i - 1][j - 1]  # upper left
            ur = input[i - 1][j + 1]  # upper right
            bl = input[i + 1][j - 1]  # bottom left
            br = input[i + 1][j + 1]  # bottom right
            if (((ul == "M" and br == "S") or (ul == "S" and br == "M")) and
                    ((ur == "M" and bl == "S") or (ur == "S" and bl == "M"))):
                xmas2 += 1

print(f"There are {xmas} XMAS in the crossword.")
print(f"There are {xmas2} X-MAS in the crossword.")


