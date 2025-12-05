with open('input.txt', 'r') as file:
    lines = file.readlines()

total = 0
did_change = True

for i in range(len(lines)):
    lines[i] = lines[i].strip()

while (did_change):
    did_change = False
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '@':
                num_neighbours = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if k < 0 or k >= len(lines) or l < 0 or l >= len(lines[k]) or (k == i and l == j):
                            continue
                        if lines[k][l] == '@':
                            num_neighbours += 1

                if num_neighbours < 4:
                    total += 1
                    lines[i] = lines[i][:j] + '.' + lines[i][j+1:]
                    did_change = True

print(total)