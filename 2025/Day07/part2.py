with open('input.txt', 'r') as file:
    lines = file.readlines()

map = []

for i, line in enumerate(lines):
    map.append(line.strip())
    if i == 0:
        start = (0, line.index('S'))

to_visit = [start]
num_splits = 0
visited = {start: 1}
while len(to_visit) > 0:
    curr = to_visit.pop(0)
    candidates = []
    if curr[0] + 1 < len(map):
        if map[curr[0]+1][curr[1]] == '.':
            candidates.append((curr[0]+1, curr[1]))
        elif map[curr[0]+1][curr[1]] == '^':
            if curr[1] - 1 >= 0:
                candidates.append((curr[0]+1, curr[1]-1))
            if curr[1] + 1 < len(map[0]):
                candidates.append((curr[0]+1, curr[1]+1))

    for option in candidates:
        if option not in visited:
            to_visit.append(option)
            visited[option] = visited[curr]
        else:
            visited[option] += visited[curr]


print(sum(visited[coord] for coord in visited if coord[0] == len(map) - 1))