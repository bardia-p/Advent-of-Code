with open('input.txt', 'r') as file:
    lines = file.readlines()

points = []
for line in lines:
    points.append(tuple(map(int, line.strip().split(','))))

points.sort(key=lambda x: (x[0], x[1]))

max_area = 0
for i in range(len(points)):
    p1 = points[i]
    for j in range(i+1, len(points)):
        p2 = points[j]
        if (p2[0] >= p1[0] and p2[1] <= p1[1]):
            max_area = max(max_area, (p2[0] - p1[0] + 1) * (p1[1] - p2[1] + 1))
        elif (p2[0] >= p1[0] and p2[1] >= p1[1]):
            max_area = max(max_area, (p2[0] - p1[0] + 1) * (p2[1] - p1[1] + 1))


print(max_area)
