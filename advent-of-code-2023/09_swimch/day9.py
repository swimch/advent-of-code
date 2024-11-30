input_data = []
with open('input.txt', 'r') as f:
    for line in f:
        input_data.append([int(x) for x in line[:-1].split()])

print(input_data)

def predictions(values): # calculate next values with all input lists
    next_sum = 0
    # loop backwards through list, starting with :-1, add corresponding value from list below for prediction
    return next_sum


def next_values(values):
    current_list = [values]
    if current_list.count(0) == len(current_list):
        all_zero = True

    next_list = []
    for i in range(current_list.len()+1):
        next_list.append(current_list[i+1]-current_list[i])
    # loop through entire list, when all in next list = 0 set true and calculate next values with predictions
    # else loop through next list
    all_zero = False
    while not all_zero:

    return predictions("alle listen")


next_values_sum = 0
for values_over_time in input_data:   # Loops through value over time lists
    next_values_sum += next_values(values_over_time)
