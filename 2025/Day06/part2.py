with open('input.txt', 'r') as file:
    lines = file.readlines()

new_digit = False
new_lines = ["" for _ in range(len(lines))]
new_lines[-1] = lines[-1]

for i in range(len(lines[0])):
    empty_column = all(lines[j][i] == " " or lines[j][i] == "\n" for j in range(len(lines)- 1))
    
    for j in range(len(new_lines) - 1):
        if empty_column or lines[j][i].isdigit():
            new_lines[j] += lines[j][i]
        else:
            new_lines[j] += "0"

operations = []
problems = [[] for _ in range(len(new_lines[0].strip().split()))]
for i in range(len(new_lines)):
    line = new_lines[i].strip()
    if i == len(new_lines) - 1:
        operations = line.split()
    else:
        for i, arg in enumerate(line.split()):
            problems[i].append(arg)

cols = [[] for _ in range(len(problems))]
for i, problem in enumerate(problems):
    new_cols = ["" for _ in range(len(problems[i]))]
    for arg in problem:
        for j, c in enumerate(arg):
            if c != "0":
                new_cols[j] += (c)
    cols[i] = list(filter(lambda x: x != '', new_cols))

result = 0
for i in range(len(cols)):
    result += eval(operations[i].join(cols[i]))

print(result)