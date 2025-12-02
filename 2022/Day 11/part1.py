class Monkey:
    def __init__(self,id):
        self.id = id
        self.items = []
        self.operation = None
        self.test = None
        self.true = -1
        self.false = -1
        self.count = 0

    def inspect(self, item):
        self.count += 1
        func = lambda x : eval(self.operation)
        return func(item) // 3

    def passToMonkey(self, item):
        func = lambda x : eval(self.test)
        return self.true if func(item) == 0 else self.false

    def print(self):
        print("Monkey: " + str(self.id))
        print("\tItems: " + str(self.items))
        print("\tOperation: " + str(self.operation))
        print("\tTest: " + str(self.test))
        print("\t\t if true: Go to Monkey " + str(self.true))
        print("\t\t if false: Go to Monkey " + str(self.false))
        print("\tTotal Items: " + str(self.count))


f = open("Day 11/input.txt", "r")

lines = f.readlines()

monkeys = []


for line in lines:
    if "Monkey" in line:
        info = line.strip().split(" ")
        id = int(info[1].strip(":"))
        monkeys.append(Monkey(id))
    elif "Starting" in line:
        info = line.strip().split(" ")
        for item in info[2:]:
            monkeys[-1].items.append(int(item.strip(",")))
    elif "Operation" in line:
        info = line.strip().split(" ")
        value = "x" if info[-1] == "old" else info[-1]
        op = info[-2]
        monkeys[-1].operation = "x" + op + value
    elif "Test" in line:
        info = line.strip().split(" ")
        toDivide = info[-1]
        monkeys[-1].test = "x" + "%" + toDivide
    elif "true" in line:
        info = line.strip().split(" ")
        destMonkey = int(info[-1])
        monkeys[-1].true = destMonkey
    elif "false" in line:
        info = line.strip().split(" ")
        destMonkey = int(info[-1])
        monkeys[-1].false = destMonkey

for i in range(20):
    for m in monkeys:
        while len(m.items) > 0:
            item = m.items.pop(0)
            newItem = m.inspect(item)
            newDest = m.passToMonkey(newItem)
            monkeys[newDest].items.append(newItem)


max = [0,0]
for m in monkeys:
    if m.count > max[0]:
        max[1] = max[0]
        max[0] = m.count
    elif m.count > max[1]:
        max[1] = m.count

print(max[0] * max[1])
f.close()

