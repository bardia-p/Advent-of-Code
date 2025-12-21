with open('input.txt', 'r') as file:
    lines = file.readlines()

points = dict()

for line in lines:
    cleaned = line.strip().split()
    points[cleaned[0][:-1]] = cleaned[1:]

def traverse(node, end, forbidden, visited):
    if node in forbidden:
        return 0
    
    if node == end:
        return 1
    
    if node in visited:
        return visited[node]
    
    total = 0
    for c in points[node]:
        total += traverse(c, end, forbidden, visited)

    visited[node] = total
    return total


total = 0
# dac then fft
total += traverse('svr', 'dac', {'fft', 'out'}, dict()) * traverse('dac', 'fft', {'svr', 'out'}, dict()) * traverse('fft', 'out', {'svr', 'dac'}, dict())
# fft then dac
total += traverse('svr', 'fft', {'dac', 'out'}, dict()) * traverse('fft', 'dac', {'svr', 'out'}, dict()) * traverse('dac', 'out', {'svr', 'fft'}, dict())

print(total)