file = open("input.txt", "r")
data = file.readlines()

def chunk(start, end, step, my_list, stacks):
    x = 0
    for i in range(0, 9):
        part = my_list[x:x + step].strip(' ')
        if len(part) != 0:
            stacks[i].append(my_list[x:x + step].strip(' '))
        x = x + step + 1

stacks = [[] for i in range(9)]

for item in data[0:8]:
    chunk(0, len(item), 3, item, stacks)

for item in stacks:
    item.reverse()

for item in data[10:]:
    commands = item.split(' ')
    fromI = int(commands[3]) - 1
    toI = int(commands[5]) - 1
    amount = int(commands[1])
    stacks[toI].extend(stacks[fromI][-amount:])
    stacks[fromI] = stacks[fromI][0: -amount]



answer = ''
for item in stacks:
    answer = answer + item.pop()

print(answer)