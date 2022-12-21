from collections import deque
from math import lcm

file = open("input.txt", "r")
data = file.readlines()

class Monkey:
    def __init__(self):
        self.worry = 0
        self.startingItems = deque([])
        self.operation = ''
        self.operand = ''
        self.test = ''
        self.trowTo = [0,0]
        self.inspectedItems = 0

    def addStartingItem(self, item):
        self.startingItems.extend(item)

    def print(self):
        print(self.worry, self.startingItems, self.operation, self.operand, self.test, self.trowTo, self.inspectedItems)

monkeys = []

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

operToFunc = { "*" : multiply, "/" : divide, "+" : add, "-" : subtract}

monkeyI = -1
for i, line in enumerate(data):
    line = line.strip("\n")
    if i % 7 == 0:                  #новая обезьяна
        newMonkey = Monkey()
        monkeys.append(newMonkey)
        monkeyI = monkeyI + 1

    if i % 7 == 1:
        startingItems = line[line.find(":")+1:]
        monkeys[monkeyI].addStartingItem([item.strip(' ') for item in startingItems.split(',')])

    if i % 7 == 2:
        expression = line[line.find(":") + 1:]
        monkeys[monkeyI].operation = expression.split()[3]
        monkeys[monkeyI].operand = expression.split()[4]

    if i % 7 == 3:
        expression = line[line.find(":") + 1:]
        monkeys[monkeyI].test = int(expression.split()[2])

    if i % 7 == 4:
        expression = line[line.find(":") + 1:]
        monkeys[monkeyI].trowTo[0] = int(expression.split()[3])

    if i % 7 == 5:
        expression = line[line.find(":") + 1:]
        monkeys[monkeyI].trowTo[1] = int(expression.split()[3])

#for monkey in monkeys:
    #monkey.print()

roundCount = 10000

base = lcm(*(monkey.test for monkey in monkeys))
print(base)
for i in range(0, roundCount):
    #print(i)

    for monkey in monkeys:
        currentWorryLVL = 0
        while len(monkey.startingItems) != 0:
            item = monkey.startingItems[0]
            monkey.inspectedItems = monkey.inspectedItems + 1
            worryLVL = int(item)
            currentWorryLVL = worryLVL
            #print("Inspect item: ", currentWorryLVL)
            if monkey.operand == 'old':
                currentWorryLVL = operToFunc[monkey.operation](worryLVL, worryLVL) % base
            else:
                currentWorryLVL = operToFunc[monkey.operation](worryLVL, int(monkey.operand)) % base


            if currentWorryLVL % monkey.test == 0:
                monkeys[monkey.trowTo[0]].startingItems.append(currentWorryLVL)
            else:
                monkeys[monkey.trowTo[1]].startingItems.append(currentWorryLVL)
            monkey.startingItems.popleft()
    #for monkey in monkeys:
        #monkey.print()

for monkey in monkeys:
    monkey.print()