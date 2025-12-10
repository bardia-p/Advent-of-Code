import math

with open('input.txt', 'r') as file:
    lines = file.readlines()

points = []
for line in lines:
    points.append(tuple(map(int, line.strip().split(','))))

ranges = []

for i in range(len(points)):
    ranges.append([points[i], points[(i+1) % len(points)]])

interior = set(points)
for i in range(len(points)):
    x1, y1 = points[i]
    x2, y2 = points[(i+1) % len(points)]
    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            interior.add((x1,y))
    else:
        for x in range(min(x1,x2), max(x1,x2)+1):
            interior.add((x,y1))

ys = sorted(set(y for _,y in points))
for y in range(min(ys), max(ys)+1):
    xs = []
    for i in range(len(points)):
        (x1, y1) = points[i]
        (x2, y2) = points[(i+1) % len(points)]
        if y1 == y2: continue
        if min(y1,y2) <= y < max(y1,y2):
            x = x1 + (y - y1) * (x2 - x1)/(y2 - y1)
            xs.append(x)
    xs.sort()
    for a, b in zip(xs[0::2], xs[1::2]):
        for x in range(math.ceil(a), math.floor(b)+1):
            interior.add((x,y))

points.sort(key=lambda x: (x[0], x[1]))

max_area = 0
for i in range(len(points)):
    p1 = points[i]
    for j in range(i+1, len(points)):
        p2 = points[j]
        
        if (p2[0], p1[1]) not in interior or (p1[0], p2[1]) not in interior:
            continue
            
        # bottom left - top right
        if (p2[0] >= p1[0] and p2[1] <= p1[1]):
            max_area = max(max_area, (p2[0] - p1[0] + 1) * (p1[1] - p2[1] + 1))

        # top left - bottom right
        elif (p2[0] >= p1[0] and p2[1] >= p1[1]):
            max_area = max(max_area, (p2[0] - p1[0] + 1) * (p2[1] - p1[1] + 1))


print(max_area)
