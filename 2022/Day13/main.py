from itertools import zip_longest
from functools import cmp_to_key

file = open("input.txt", "r")
data = file.readlines()


def parseLine(line, i):
    result = []
    while i < len(line):
        if line[i] == ",":
            i = i + 1
            continue

        if line[i] == '[':
            innerList = parseLine(line, i + 1)
            result.append(innerList[0])
            i = innerList[1]
            continue

        if line[i] == ']':
            return tuple((result, i+1))

        num = ''
        while line[i].isdigit():
            num += line[i]
            i = i+1

        #print(num)
        result.append(int(num))
        #print(result)
        #i = i + 1

    return result

def compareLists(list1, list2):
    print(list1, "==", list2)

    for l, r in zip_longest(list1, list2):
        print(l,r)
        match l, r:
            case int(), int():
                if l < r: return -1
                if l > r: return 1
            case None, _:
                return -1
            case _, None:
                return 1
            case list(), list():
                val = compareLists(l, r)
                if val != 0: return val
            case int(), list():
                val = compareLists([l], r)
                if val != 0: return val
            case list(), int():
                val = compareLists(l, [r])
                if val != 0: return val

    return 0


#def compare(list1, list2):
    #l = 0
    #r = 0
    #if type(list1[l]) == list and type(list2[l]) == list:
        #return compareLists(list1, list2)



parsedLists = []
for line in data:
    line = line.strip("\n")
    if len(line) == 0:
        continue

    result = parseLine(line, 0)
    parsedLists.append(result)
    #print(result)

answer = 0
k = 0
for i, el in enumerate(parsedLists):
    if i % 2 == 0:
        left = parsedLists[i]
    if i % 2 == 1:
        k = k + 1
        right = parsedLists[i]
        if compareLists(left[0], right[0]) == -1:
            print("TRUE", k)
            answer += k
    #print("FALSE")
    print()

parsedLists.append([[2]])
parsedLists.append([[6]])

print(parsedLists)
parsedLists.sort(key=cmp_to_key(lambda l, r: next(compareLists(l, r))), reverse=True)
#print(parsedLists)

print(answer)