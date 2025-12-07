with open('input.txt', 'r') as file:
    lines = file.readlines()

operations = []
problems = [[] for _ in range(len(lines[0].strip().split()))]
for i in range(len(lines)):
    line = lines[i].strip()
    if i == len(lines) - 1:
        operations = line.split()
    else:
        for i, arg in enumerate(line.split()):
            problems[i].append(arg)

result = 0
for i in range(len(problems)):
    result += eval(operations[i].join(problems[i]))

print(result)