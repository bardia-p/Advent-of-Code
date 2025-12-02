f = open("Day 6/input.txt", "r")

i = 0
visited = []
while True:
    c = f.read(1)
    if not c:
        break
    i += 1
    visited.append(c)
    if len(visited) == 14:
        if len(set(visited)) == 14:
            break
        visited.pop(0)

print(i)