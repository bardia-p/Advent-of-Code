f = open("Day 1/input.txt", "r")

lines = f.readlines()

maxCal = 0 
currCal = 0 

for line in lines:
    goodLine = line.strip()

    if goodLine != "":
        currCal += int(goodLine)
    else:
        maxCal = max(maxCal, currCal)
        currCal = 0
print(maxCal)

f.close()

