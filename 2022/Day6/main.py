file = open("input.txt", "r")
data = file.readlines()
data = str(data[0])
l = 0
r = 0
unique = dict({})
while r < len(data) and (r - l <= 13):
    if data[r] in unique:
        l = unique[data[r]]
        r = l+1
        unique.clear()


    unique[data[r]] = r
    print(unique)
    r = r + 1

print(l,r)
answer = data[l:r]
print(answer)
print(r)