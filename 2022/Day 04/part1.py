f = open("Day 4/input.txt", "r")

lines = f.readlines()

numPairs = 0 

for line in lines:
    pairs = line.split(",")
    p1 = list(map(int, pairs[0].split("-")))
    p2 = list(map(int, pairs[1].split("-")))

    if (p1[0] >= p2[0] and p1[1] <= p2[1]) or (p2[0] >= p1[0] and p2[1] <= p1[1]):
        numPairs += 1

print(numPairs)

f.close()