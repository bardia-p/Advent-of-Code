f = open("Day 3/input.txt", "r")

lines = f.readlines()

priorities = 0 

for line in lines:
    bag1 = set(line[0:len(line)//2])
    bag2 = set(line[len(line)//2:len(line)])

    toChange = list(bag1.intersection(bag2))[0]


    if ord(toChange) <= 90:
        priorities += ord(toChange) - 64 + 26
    else:
        priorities += ord(toChange) - 96

print(priorities)
f.close()