file = open("input.txt", "r")
data = file.readlines()

sums = []

maxSum = 0
curSum = 0
for item in data:
    if item == "\n":
        maxSum = max(maxSum, curSum)
        sums.append(curSum)
        curSum = 0
    else:
        curSum = curSum + int(item)

sums.sort()
lenSum = len(sums)
print(sums)
answer = sums[lenSum-1] + sums[lenSum-2] + sums[lenSum-3]
print(answer)