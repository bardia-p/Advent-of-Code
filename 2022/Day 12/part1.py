from collections import deque

f = open("Day 12/input.txt", "r")

map = [list(line.strip()) for line in f.readlines()]

def findShortestPathToE(x,y):
    global map


    visited = set([x,y])

    paths = dict()
    q = deque()
    q.append((x,y))

    while len(q) != 0:
        p = q.popleft()

        i = p[0]
        j = p[1]

        visited.add((i,j))

        currKey = str(i) + " " + str(j)
        if map[i][j] == "E":
            break    
        
        if i - 1 >= 0 and compare(map[i][j], map[i-1][j]) and (i-1, j) not in visited:
            q.append((i-1, j))
            paths[str(i-1) + " " + str(j)] = currKey

        if i + 1 < len(map) and compare(map[i][j], map[i+1][j]) and (i+1, j) not in visited:
            q.append((i+1, j))
            paths[str(i+1) + " " + str(j)] = currKey


        if j - 1 >= 0 and compare(map[i][j], map[i][j-1]) and (i, j-1) not in visited:
            q.append((i, j-1))
            paths[str(i) + " " + str(j-1)] = currKey

        if j + 1 < len(map[0]) and compare(map[i][j], map[i][j+1]) and (i, j+1) not in visited:
            q.append((i, j+1))
            paths[str(i) + " " + str(j+1)] = currKey

    key = currKey

    c = 0
    points = []
    while key in paths:
        c += 1
        points.append(key)

        key = paths[key]


    print(points[::-1])

    return c

def compare(c1, c2):
    if c1 == "S" and c2 == "a":
        return True
    if c1 == "z" and c2 == "E":
        return True
    if c1 >= c2 and c2 != "E" and c2 !="S":
        return True
    if ord(c1) == ord(c2) - 1:
        return True
    
    return False

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "S":
            print(findShortestPathToE(i, j))
f.close()


