file = open("input.txt", "r")
data = file.readlines()

grid = []
for i in range(0,600):
    newRow = ["."] * 1000
    grid.append(newRow)

def addStoneLine(grid, start, finish):
    s = [int(x) for x in start.split(',')]
    f = [int(x) for x in finish.split(',')]
    #print(s,f)
    grid[s[1]][s[0]] = '#'
    if s[0] == f[0]:
        while s[1] < f[1]:
            grid[s[1]][s[0]] = '#'
            s[1] = s[1] + 1

        while s[1] > f[1]:
            grid[s[1]][s[0]] = '#'
            s[1] = s[1] - 1
    elif s[1] == f[1]:
        while s[0] < f[0]:
            grid[s[1]][s[0]] = '#'
            s[0] = s[0] + 1

        while s[0] > f[0]:
            grid[s[1]][s[0]] = '#'
            s[0] = s[0] - 1

    grid[f[1]][f[0]] = "#"

def couldMoveDown(grid, cur):
    return grid[cur[0]+1][cur[1]] not in ['#', 'o']

def couldMoveLeftDown(grid, cur):
    return grid[cur[0] + 1][cur[1] - 1] not in ['#', 'o']

def couldMoveRightDown(grid, cur):
    return grid[cur[0] + 1][cur[1] + 1] not in ['#', 'o']

def step(direction, cur):
    cur[0] = cur[0] + direction[0]
    cur[1] = cur[1] + direction[1]

def moveSand(spawnPoint):

    cur = spawnPoint.copy()
    while True:
        if cur[0] >= len(grid) - 1:
            return -1
        if couldMoveDown(grid, cur):
            step([1, 0], cur)
        elif couldMoveLeftDown(grid, cur):
            step([1, -1], cur)
        elif couldMoveRightDown(grid, cur):
            step([1, 1], cur)
        else:
            grid[cur[0]][cur[1]] = 'o'
            if cur == spawnPoint:
                return -1
            break


for coord in data:
    coord = coord.strip("\n")
    parsed = coord.split(" -> ")
    for i in range(0, len(parsed) - 1):
        addStoneLine(grid, parsed[i], parsed[i+1])


counter = 0

for i in range(0,1000):
    grid[162][i] = "#"

while moveSand([0,500]) != -1:
    counter = counter + 1

#print(counter)
for line in grid:
    str = ''
    print(str.join(line))

print(counter + 1)

