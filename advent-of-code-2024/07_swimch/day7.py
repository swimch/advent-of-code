calibrations = []
with open('test.txt', 'r') as f:
    for line in f:
        target, values = line.split(":")
        calibrations.append((int(target), [int(num) for num in values.split()])) # add target and numbers as tuple

def check_possible(equation): # recursive, returns results for all possible operations
    if len(equation) == 1: # exit condition
        return [equation[0]]
    else: # else return all possibilities
        previous = check_possible(equation[:-1]) # iterate backwards to read left to right in calculation
        return ([equation[-1] + prev for prev in previous] +
                [equation[-1] * prev for prev in previous])


result1 = 0
for calibration in calibrations:
    if calibration[0] in check_possible(calibration[1]): # check if target gets reached by at least one term
        result1 += calibration[0] # if calibration is possible, add target for AOC solution
print(result1) # 1399219271639


def check_possible2(equation): # recursive, returns results for all possible operations
    if len(equation) == 1: # exit condition
        return [equation[0]]
    else: # else return all possibilities
        previous = check_possible(equation[:-1]) # iterate backwards to read left to right in calculation
        return ([equation[-1] + prev for prev in previous] +
                [equation[-1] * prev for prev in previous] +
                [int(str(prev) + str(equation[-1])) for prev in previous])
                # Sometimes concatenations don't get added to list, e.g. 7290: 6 8 6 15 (6*8||6*15 missing)

result2 = 0
for calibration in calibrations:
    if calibration[0] in check_possible2(calibration[1]): # check if target gets reached by at least one term
        result2 += calibration[0] # if calibration is possible, add target for AOC solution
print(result2) # 11387 for test case
