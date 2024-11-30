input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])

spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits1 = []
digits2 = []
values1 = []
values2 = []
for line in input:
    for i in range(len(line)):
        #Für Teil 1 & 2
        if line[i].isdigit():
            digits1.append(line[i])
            digits2.append(line[i])
        #Nur für Teil 2
        else:
            for number in spelled:
                if line[i:(i+len(number))] == number:
                    digits2.append(str(spelled.index(number)+1))

    values1.append(int(digits1[0] + digits1[-1]))
    values2.append(int(digits2[0] + digits2[-1]))
    digits1 = []
    digits2 = []
print(sum(values1))
print(sum(values2))