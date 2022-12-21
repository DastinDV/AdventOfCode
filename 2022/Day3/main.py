file = open("input.txt", "r")
data = file.readlines()

scores = {}

s = 97
for i in range(1,27):
    scores[s] = i
    s = s + 1

s = 65
for i in range(27, 53):
    scores[s] = i
    s = s + 1

answer = 0
lists = [[] for _ in range(3)]
i = 0

for item in data:
    item = item.strip('\n')
    lists[i % 3].append(item)
    i = i + 1


for (f, s, t) in zip(lists[0], lists[1], lists[2]):
    res = list(set(f) & set(s) & set(t))
    answer += scores[ord(res[0])]

print(answer)