file = open("input.txt", "r")
data = file.readlines()

def isVisible(grid, i, j):
    North = True
    South = True
    West = True
    East = True

    row = i
    col = j

    Nc = 0
    Sc = 0
    Wc = 0
    Ec = 0
    while row > 0:
        row = row - 1
        Nc = Nc + 1
        if grid[row][col] >= grid[i][j]:
            North = False
            break
    row = i
    col = j
    while row + 1 < len(grid):
        row = row + 1
        Sc = Sc + 1
        if grid[row][col] >= grid[i][j]:
            South = False
            break
    row = i
    col = j
    while col > 0:
        col = col - 1
        Wc = Wc + 1
        if grid[row][col] >= grid[i][j]:
            West = False
            break
    row = i
    col = j
    while col + 1 < len(grid[0]):
        col = col + 1
        Ec = Ec + 1
        if grid[row][col] >= grid[i][j]:
            East = False
            break

    print(i, j, Nc * Sc * Wc * Ec)
    return Nc * Sc * Wc * Ec

grid = []
for line in data:
    line = line.strip("\n")
    grid.append([int(x) for x in list(line)])

answer = 0
maxSceneScore = 0
for i,row in enumerate(grid):
    for j, col in enumerate(grid[i]):
        maxSceneScore = max(maxSceneScore, isVisible(grid,i,j))

print(grid)
print(maxSceneScore)