file = open("input.txt", "r")
data = file.readlines()

class Folder:
    def __init__(self):
        self.name = ''
        self.filesSize = 0
        self.nameToChild = dict({})
        self.parent = None

    name = ''
    filesSize = 0
    nameToChild = dict({})
    parent = None

    def setName(self, name):
        self.name = name

    def addFolder(self, name, newFolder):
        if self.nameToChild.get(name) == None:
            self.nameToChild[name] = Folder()

        self.nameToChild[words[1]] = newFolder

    def addFileSize(self, fileSize):
        self.filesSize += fileSize

    def getFileSize(self):
        return self.filesSize

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def getFolder(self, name):
        return self.nameToChild.get(name)


root = Folder()
root.name = '/'
root.filesSize = 0

currentFolder = root
currentCommand = ''

for line in data:
    line = line.strip("\n")
    words = line.split(' ')
    if words[0] == "$":             #command started
        currentCommand = words[1]
        if currentCommand == "ls":
            continue

    if currentCommand == "ls":
        if words[0] == "dir":
            newFolder = Folder()
            newFolder.setName(words[1])
            newFolder.setParent(currentFolder)
            currentFolder.addFolder(words[1], newFolder)
        else:
            currentFolder.addFileSize(int(words[0]))
    if currentCommand == "cd":
        if words[2] == "..":
            currentFolder = currentFolder.getParent()
        elif words[2] != "/":
            currentFolder = currentFolder.getFolder(words[2])


currentFolder = root

answer = []
allFolders = []
updateSpace = 30000000
allSpace = 70000000

def PrintTree(currentFolder,counter, answer, allFolders):
    print((" " * counter) + "Folder size ", currentFolder.getFileSize())
    print((" " * counter) + "Folder name ", currentFolder.name)
    currentFolderSize = currentFolder.getFileSize()
    for item in currentFolder.nameToChild.items():
        currentFolderSize += PrintTree(item[1], counter + 2, answer, allFolders)
    print((" " * counter) + "Current folder size ", currentFolderSize)

    if currentFolderSize <= 100000:
        answer.append(currentFolderSize)

    allFolders.append(currentFolderSize)
    return currentFolderSize;

filledSpace = PrintTree(currentFolder, 0, answer, allFolders)
freeSpace = allSpace - filledSpace
needToRemoveSpace = updateSpace - freeSpace

print("FilledSpace: ", filledSpace)
print("FreeSpace: ", freeSpace)
print("UpdateSpace: ", needToRemoveSpace)
print(allFolders)

minDiff = needToRemoveSpace
minVal = 0

for item in allFolders:
    if item >= needToRemoveSpace and item - needToRemoveSpace < minDiff:
        print(minDiff)
        minDiff = item - needToRemoveSpace
        minVal = item

sumAnswer = sum(answer)
print("PartOne: ", sumAnswer)
print("PartTwo: ", minVal)



