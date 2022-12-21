file = open("input.txt", "r")
data = file.readlines()

directions = {"R": [0, 1], "L": [0, -1], "U": [1, 0], "D": [-1, 0]}


def updateHead(grid, direction, headPos):
    #print(headPos[0],headPos[1])
    #grid[headPos[0]][headPos[1]] = 2
    headPos[0] = headPos[0] + directions[direction][0]
    headPos[1] = headPos[1] + directions[direction][1]


def isSameRow(headPos, tailPos):
    return headPos[0] == tailPos[0]


def isSameColumn(headPos, tailPos):
    return headPos[1] == tailPos[1]

def isNotTouchingAround(headPos, tailPos):
    answer = True
    if (headPos[0] == tailPos[0] - 1) and (headPos[1] == tailPos[1] - 1) or\
           (headPos[0] == tailPos[0] - 1) and (headPos[1] == tailPos[1] + 1) or\
           (headPos[0] == tailPos[0] + 1) and (headPos[1] == tailPos[1] - 1) or\
           (headPos[0] == tailPos[0] + 1) and (headPos[1] == tailPos[1] + 1):
           answer = False

    return answer


def updateTail(tailPos, prevHeadPos):
    print("UpdateTail")
    grid[tailPos[0]][tailPos[1]] = 1
    tailPos = prevHeadPos.copy()


grid = []
for i in range(0,200):
    grid.append([0] * 200)

headPos = [0, 0]
tailPos = [0, 0]
prevHeadPos = headPos

answer = 0
knots = [[0, 0], [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8], [0,-9], [-9,-9]]
print(knots)
#currentHead
for item in data:
    item = item.strip("\n")
    vals = item.split()
    for i in range(0, int(vals[1])):
        prevHeadPos = knots[0].copy()
        for k, knotPos in enumerate(knots):      # За головой двигаем оставшиеся узлы
            if k == 0:
                updateHead(grid, vals[0], knotPos)
            if k == len(knots) - 1:
                continue
            currentHead = knots[k].copy()
            tailPos = knots[k+1].copy()
            buf = tailPos.copy()
            print("Hi", currentHead, prevHeadPos, tailPos)

            if (isSameRow(currentHead, tailPos) and abs(currentHead[1] - tailPos[1]) == 2)\
                    or (isSameColumn(currentHead, tailPos) and abs(currentHead[0] - tailPos[0]) == 2):
                print("UPDATE TAIL")
                tailPos = prevHeadPos.copy()
            elif isSameRow(currentHead, tailPos) == False and isSameColumn(currentHead, tailPos) == False and\
                isNotTouchingAround(currentHead,tailPos) == True:
                print("UPDATE TAIL DIAGONAL")
                tailPos = prevHeadPos.copy()

            prevHeadPos = buf.copy()
            knots[k+1] = tailPos



        print('\n')

grid.reverse()

for line in grid:
    for el in line:
        if el == 1:
            answer = answer + 1

#print(grid)
print(answer)