with open('input.txt', 'r') as file:
    lines = file.readlines()

points = dict()

for line in lines:
    cleaned = line.strip().split()
    points[cleaned[0][:-1]] = cleaned[1:]

def traverse(node, visited = dict()):
    if node == "out":
        return 1
    
    if node in visited:
        return visited[node]
    
    total = 0
    for c in points[node]:
        total += traverse(c, visited)

    visited[node] = total
    return total

print(traverse('you'))