orders = []
print_queue = []
with open('input.txt', 'r') as f:
    for line in f:
        if "|" in line:
            orders.append([int(page) for page in line[:-1].split("|")]) # get orders instructions
        elif "," in line:
            print_queue.append([int(page) for page in line[:-1].split(",")]) # get manuals to be printed


def is_ordered(update):
    for order in orders:
        if order[0] in update and order[1] in update: # check if both pages listed together in an instruction
            if update.index(order[0]) > update.index(order[1]): # invalid page order
                return 0
    return update[((len(next_print)-1)//2)] # returns middle page number

def order_update(update):
    unordered = 1
    while unordered > 0: # equals 0 after running through whole orders list and all pages are in order
        unordered = 1
        for order in orders:
            if order[0] in update and order[1] in update: # check if both pages listed together in an instruction
                if update.index(order[0]) > update.index(order[1]): # invalid page order
                    buffer = update.pop(update.index(order[1])) # remove first invalid page
                    update.insert(update.index(order[0])+1, buffer) # insert page at valid index
                    unordered += 1 # counter to run again to check if it's ordered
        unordered -= 1 # sets unordered to 0 if all instructions are followed, breaks loop
    return update[((len(next_print)-1)//2)] # returns middle page number


middle_pages1, middle_pages2 = 0, 0
for next_print in print_queue:
    middle = is_ordered(next_print)
    if middle == 0: # if unordered, order the manual
        middle_pages2 += order_update(next_print)
    else:
        middle_pages1 += middle

print(f"The sum of the middle pages for all ordered manuals is {middle_pages1}.")
print(f"The sum of the middle pages for all unordered manuals after ordering them is {middle_pages2}.")
