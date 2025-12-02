f = open("Day 4/input.txt", "r")

lines = f.readlines()

numPairs = 0 

for line in lines:
    pairs = line.split(",")
    p1 = list(map(int, pairs[0].split("-")))
    p2 = list(map(int, pairs[1].split("-")))

    if p1[0] <= p2[0]:
        first = p1
        second = p2
    else:
        first = p2
        second = p1

    if first[1] >= second[0]:
        numPairs += 1

print(numPairs)

f.close()