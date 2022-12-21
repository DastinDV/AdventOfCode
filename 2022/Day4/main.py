file = open("input.txt", "r")
data = file.readlines()

count = 0
for item in data:
    item = item.strip("\n")
    result = item.split(",")
    range1 = [int(x) for x in result[0].split("-")]
    range2 = [int(x) for x in result[1].split("-")]
    print(range1, range2)
    if ((range2[0] >= range1[0] and range2[0] <= range1[1]) or (range2[1] >= range1[0] and range2[1] <= range1[1])) or \
       ((range1[0] >= range2[0] and range1[0] <= range2[1]) or (range1[1] >= range2[0] and range1[1] <= range2[1])) :
        print("yes")
        count = count + 1

print(count)