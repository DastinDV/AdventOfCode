file = open("input.txt", "r")
data = file.readlines()

signal = 1
cycle = 1
prevSignal = 1
commands = {"addx": 2, "noop": 1}
startCycle = 0
stepCycle = 40
targetCycle = stepCycle

spritePos = [0,0]
pointerPos = [0,0]

answer = []
board = [["."] * 42 for i in range(6)]
print(board)

#.........
#123456789
def isOverlap(spritePos, pointerPos):
    print(pointerPos, spritePos)
    if pointerPos[1] >= spritePos[1] and pointerPos[1] <= spritePos[1] + 2:
        return True
    return False

#2 4 5 7 9 11... 19 21 23
for line in data:
    line = line.strip("\n")
    vals = line.split()
    curcycle = commands[vals[0]]

    #print(pointerPos, spritePos)

    if vals[0] == "addx":
        while curcycle > 0:

            if isOverlap(spritePos, pointerPos):
                print("Overlap", pointerPos, spritePos, line, cycle)
                board[pointerPos[0]][pointerPos[1]] = "#"

            if cycle == targetCycle:
                answer.append(signal * targetCycle)
                targetCycle = targetCycle + stepCycle
                pointerPos[0] = pointerPos[0] + 1
                pointerPos[1] = -1
                spritePos = [pointerPos[0], 0]

            curcycle = curcycle - 1
            cycle = cycle + 1
            pointerPos[1] = pointerPos[1] + 1

        signal += int(vals[1])
        spritePos[1] = signal - 1


    if vals[0] == "noop":
        #for list in board:
            #res = [''.join(ele) for ele in board]
            #print(res)

        if isOverlap(spritePos, pointerPos):
            print("Overlap", pointerPos, spritePos, line)
            board[pointerPos[0]][pointerPos[1]] = "#"

        if cycle == targetCycle:
            answer.append(signal * targetCycle)
            targetCycle = targetCycle + stepCycle
            pointerPos[0] = pointerPos[0] + 1
            pointerPos[1] = -1
            spritePos = [pointerPos[0], 0]

        pointerPos[1] = pointerPos[1] + 1
        cycle = cycle + 1

    #spritePos[1] = signal - 1

#print(answer)
#print(sum(answer))
res = list(map(''.join, board))

for line in res:
    print(line)