f = open("Day 10/input.txt", "r")

lines = f.readlines()

x = 1
totalSignal = 0
signalCount = 20
cycles = 0

for line in lines:
    inst = line.strip().split(" ")

    if inst[0] == "noop":
        cycles += 1
        if cycles == signalCount:
            totalSignal += cycles * x
            signalCount += 40
    elif inst[0] == "addx":
        for i in range(2):
            cycles += 1
            if cycles == signalCount:
                totalSignal += cycles * x
                signalCount += 40
        x += int(inst[1])

    if signalCount > 220:
        break

print(totalSignal)
