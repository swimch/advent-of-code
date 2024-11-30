def task(line, marker_lenght):
    marker = []
    for count, char in enumerate(line):
        if count < marker_lenght:
            marker += char
        else:
            if len(set(marker)) == len(marker):
                print(count)
                return()
            else:
                marker += char
                del marker[0]
    
with open("input.txt", "r") as f:
    for line in f:
            task(line, 4)
            task(line, 14)
                