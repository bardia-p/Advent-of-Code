f = open("Day 3/input.txt", "r")

lines = f.readlines()

priorities = 0 

i = 0

while i < len(lines):
    bag1 = set(lines[i].strip())
    bag2 = set(lines[i+1].strip())
    bag3 = set(lines[i+2].strip())

    toChange = list(bag1.intersection(bag2).intersection(bag3))[0]

    if ord(toChange) <= 90:
        priorities += ord(toChange) - 64 + 26
    else:
        priorities += ord(toChange) - 96
    
    i += 3

print(priorities)
f.close()