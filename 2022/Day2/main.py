file = open("input.txt", "r")
data = file.readlines()

print(data)
values = { "A X" : "3",
           "B X" : "0",
           "C X" : "6",
           "A Y" : "6",
           "B Y" : "3",
           "C Y" : "0",
           "A Z" : "0",
           "B Z" : "6",
           "C Z" : "3"
           }

chose = { "X" : "1",
          "Y" : "2",
          "Z" : "3"}

replace = { "A Y": "A X",
            "B Y": "B Y",
            "C Y": "C Z",

            "A X": "A Z",
            "B X": "B X",
            "C X": "C Y",

            "A Z": "A Y",
            "B Z": "B Z",
            "C Z": "C X",
            }

score = 0
for item in data:
    item = item.strip('\n')
    item = replace[item]
    score += int(values[item])
    score += int(chose[item[-1]])

print(score)

