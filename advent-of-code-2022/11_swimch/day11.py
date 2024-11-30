import re
import copy

f = open("input.txt", "r")
input = [line.strip() for line in f]
monkeys = {}

for index, line in enumerate(input):
    if line.startswith("Monkey"):
        monkeys[int(line.split()[1][:-1])] = {
            "items": [int(x) for x in re.split(": |, ", input[index+1])[1:]],
            "operation": input[index + 2][17:],
            "test": int(input[index + 3].split()[3]),
            "throw true": int(input[index + 4][-1:]),
            "throw false": int(input[index + 5][-1:]),            
            "inspections": 0
    }
teiler = [monkeys[x]["test"] for x in monkeys] #evt relevant für teil 2?

def uuhuuhaahaah(rounds, worry):
    gorillas = copy.deepcopy(monkeys)
    for i in range(rounds):
        for monkey in gorillas:
            gorilla = gorillas[monkey]
            for item in gorilla["items"]:
                old = item
                new = eval(gorilla["operation"])
                new = new//worry
                if new % gorilla["test"] == 0:
                    gorillas[gorilla["throw true"]]["items"].append(new)
                else:
                    gorillas[gorilla["throw false"]]["items"].append(new)
                gorilla["inspections"] += 1
            gorilla["items"] = []
    monkeybusiness = []
    for monkey in gorillas:
        monkeybusiness.append(gorillas[monkey]["inspections"])
    monkeybusiness.sort()
    print(monkeybusiness[-1]*monkeybusiness[-2])
    return
uuhuuhaahaah(20, 3)
uuhuuhaahaah(10000, 1) #falscher ansatz :( (funktion effizienter machen)
