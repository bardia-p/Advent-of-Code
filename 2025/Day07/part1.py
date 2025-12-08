with open('input.txt', 'r') as file:
    lines = file.readlines()

map = []

for i, line in enumerate(lines):
    map.append(line.strip())
    if i == 0:
        start = (0, line.index('S'))

to_visit = [start]
num_splits = 0
visited = set()
while len(to_visit) > 0:
    curr = to_visit.pop(0)
    if curr not in visited:
        if curr[1] < len(map[0]) and 0 <= curr[0] < len(map) - 1:
            if map[curr[0]+1][curr[1]] == '.':
                to_visit.append((curr[0]+1, curr[1]))
            elif map[curr[0]+1][curr[1]] == '^':
                num_splits += 1
                to_visit.append((curr[0]+1, curr[1] - 1))
                to_visit.append((curr[0]+1, curr[1] + 1))
        visited.add(curr)
print(num_splits)