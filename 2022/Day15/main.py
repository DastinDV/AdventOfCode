file = open("input.txt", "r")
data = file.readlines()

def calculateManhatten(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1]-beacon[1])


def parseData(sensors, beacons):
    for line in data:
        left = [x.strip(",") for x in line[0:line.find(":")].split()]
        right = [x.strip(",") for x in line[line.find(":") + 2:].split()]
        sensor = [int(left[2][left[2].find("=") + 1:]), int(left[3][left[2].find("=") + 1:])]
        beacon = [int(right[4][right[4].find("=") + 1:]), int(right[5][right[5].find("=") + 1:])]
        sensors.append(sensor)
        beacons.append(beacon)

def getRangesForTarget(target):
    ranges = []
    for sensor, beacon in zip(sensors, beacons):

        distance = calculateManhatten(sensor, beacon)

        #print("points", sensor, beacon, distance)
        if sensor[1] >= target:                      # сенсор ниже линии
            if sensor[1] - distance > target:       # не достает до линии
                continue
            spread = distance - (sensor[1] - target)
            pointSpread = [sensor[0], target]
            leftBorder = [pointSpread[0] - spread, pointSpread[1]]
            rightBorder = [pointSpread[0] + spread, pointSpread[1]]
            ranges.append([leftBorder[0], rightBorder[0]])
        elif sensor[1] <= target:                    # сенсор выше линии
            if sensor[1] + distance < target:       # не достает до линии
                continue
            spread = distance - (target - sensor[1])
            pointSpread = [sensor[0], target]
            leftBorder = [pointSpread[0] - spread, pointSpread[1]]
            rightBorder = [pointSpread[0] + spread, pointSpread[1]]
            ranges.append([leftBorder[0], rightBorder[0]])

    ranges.sort()
    return ranges



sensors = []
beacons = []
parseData(sensors,beacons)
print(sensors, beacons)

for i in range (0, 4000001):
    #print(i)
    ranges = getRangesForTarget(i)
    #print(i, ranges)

    prevRange = ranges[0]
    leftBorder = prevRange[0]
    rightBorder = prevRange[1]
    for k in range(1, len(ranges)):
        #print(ranges[i])
        if ranges[k][0] <= rightBorder+1:      #пересечение
            if ranges[k][1] >= rightBorder:
                rightBorder = ranges[k][1]
        else:                                  #разрыв
            print("RAZRIV", i, rightBorder)
            print((rightBorder+1)*4000000 + i)
            break
    else:
        continue
    break

#print(ranges)
#print(answer)