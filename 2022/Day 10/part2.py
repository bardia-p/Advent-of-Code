def draw(cycles, x):
    global crt
    row = (cycles -1) // 40
    col = (cycles - 1) % 40

    if x - 1 <= col <= x + 1:
        crt[row][col] = "#"


f = open("Day 10/input.txt", "r")

lines = f.readlines()

crt = [["." for i in range(40)] for j in range(6)]

x = 1
totalSignal = 0
signalCount = 20
cycles = 0

for line in lines:
    inst = line.strip().split(" ")

    if inst[0] == "noop":
        cycles += 1
        draw(cycles, x)
    elif inst[0] == "addx":
        for i in range(2):
            cycles += 1
            draw(cycles, x)
        x += int(inst[1])

    if signalCount > 220:
        break

for i in range(6):
    print("".join(crt[i]))