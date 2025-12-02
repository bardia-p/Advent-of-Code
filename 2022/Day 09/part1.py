f = open("Day 9/input.txt", "r")

lines = f.readlines()

visited = set()

visited.add((0,0))

head = (0,0)
tail = (0,0)

for line in lines:
    command = line.strip().split(" ")

    move = command[0]
    num = int(command[1])

    for i in range(num):
        if move == "R":
            head = (head[0], head[1] + 1)
        elif move == "L":
            head = (head[0], head[1] - 1)
        elif move == "U":
            head = (head[0] + 1, head[1])
        elif move == "D":
            head = (head[0] - 1, head[1])

        diffRow = head[0] - tail[0]
        diffCol = head[1] - tail[1]

        if diffRow == 2 and diffCol == 0:
            tail = (tail[0] + 1, tail[1])
        elif diffRow == -2 and diffCol == 0:
            tail = (tail[0] - 1, tail[1])
        elif diffCol == 2 and diffRow == 0:
            tail = (tail[0], tail[1] + 1)
        elif diffCol == -2 and diffRow == 0:
            tail = (tail[0], tail[1] - 1)
        elif (diffRow == 2 and diffCol == 1) or (diffRow == 1 and diffCol == 2):
            tail = (tail[0] + 1, tail[1] + 1)
        elif (diffRow == -2 and diffCol == 1) or (diffRow == -1 and diffCol == 2):
            tail = (tail[0] - 1, tail[1] + 1)
        elif (diffRow == 2 and diffCol == -1) or (diffRow == 1 and diffCol == -2):
            tail = (tail[0] + 1, tail[1] - 1)
        elif (diffRow == -2 and diffCol == -1) or (diffRow == -1 and diffCol == -2):
            tail = (tail[0] -1, tail[1] - 1)

        visited.add(tail)

print(len(visited))

f.close()