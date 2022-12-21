from collections import deque

file = open("input.txt", "r")
data = file.readlines()

def dfs(grid,start,ei, ej):

    queue = deque([[start]])
    seen = set()

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x,y) in seen:
            continue
        seen.add((x, y))
        #print(x,y, len(queue))
        if x == ei and y == ej:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0])\
                    and ord(grid[x2][y2]) <= 1 + ord(grid[x][y]):
                queue.append(path + [(x2, y2)])
                #seen.add((x2, y2))



grid = []
sI = 0
sJ = 0
eI = 0
eJ = 0

for k, line in enumerate(data):
    line = line.strip("\n")
    lineSep = list(line)
    if lineSep.count('S'):
        sI = k
        sJ = lineSep.index('S')
        lineSep[sJ] = 'a'
    if lineSep.count('E'):
        eI = k
        eJ = lineSep.index('E')
        lineSep[eJ] = 'z'
    grid.append(lineSep)

print(tuple([sI, sJ]))
print(tuple([eI, eJ]))
minPath = 10000000
for i,line in enumerate(grid):
    for j,val in enumerate(grid[i]):
        if grid[i][j] == "a":
            path = dfs(grid, (i, j), eI, eJ)
            if path:
                pathlen = len(path) - 1
                print(pathlen)
                minPath = min(pathlen, minPath)

print(minPath)


#print(minPath)
