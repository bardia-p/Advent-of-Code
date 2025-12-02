def update(tail, head):

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
    elif (diffRow == 2 and diffCol >= 1) or (diffRow >= 1 and diffCol == 2):
        tail = (tail[0] + 1, tail[1] + 1)
    elif (diffRow == -2 and diffCol >= 1) or (diffRow <= -1 and diffCol == 2):
        tail = (tail[0] - 1, tail[1] + 1)
    elif (diffRow == 2 and diffCol <= -1) or (diffRow >= 1 and diffCol == -2):
        tail = (tail[0] + 1, tail[1] - 1)
    elif (diffRow == -2 and diffCol <= -1) or (diffRow <= -1 and diffCol == -2):
        tail = (tail[0] -1, tail[1] - 1)

    return tail

f = open("Day 9/input.txt", "r")

lines = f.readlines()

rope = [(0,0) for i in range(10)]

visited = set()

visited.add((0,0))

for line in lines:
    command = line.strip().split(" ")

    move = command[0]
    num = int(command[1])

    for i in range(num):
        # move head
        if move == "R":
            rope[-1] = (rope[-1][0], rope[-1][1] + 1)
        elif move == "L":
            rope[-1] = (rope[-1][0], rope[-1][1] - 1)
        elif move == "U":
            rope[-1] = (rope[-1][0] + 1, rope[-1][1])
        elif move == "D":
            rope[-1] = (rope[-1][0] - 1, rope[-1][1])

        for i in range(len(rope) - 2, -1, -1):
            rope[i] = update(rope[i], rope[i+1])

        visited.add(rope[0])

print(len(visited))

f.close()