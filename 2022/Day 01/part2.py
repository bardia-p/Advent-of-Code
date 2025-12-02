f = open("Day 1/input.txt", "r")

lines = f.readlines()

cals = []
currCal = 0 

for line in lines:
    goodLine = line.strip()

    if goodLine != "":
        currCal += int(goodLine)
    else:
        cals.append(currCal)
        currCal = 0

cals.sort()

print(sum(cals[-3::]))
f.close()