from shapely.geometry import Polygon, box

# --- Read input ---
with open("input.txt") as f:
    points = [tuple(map(int, line.strip().split(","))) for line in f]

polygon = Polygon(points)
reds = points

max_area = 0

for i in range(len(reds)):
    x1, y1 = reds[i]
    for j in range(i+1, len(reds)):
        x2, y2 = reds[j]
        rect = box(min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2))
        if polygon.contains(rect):
            area = (abs(x2-x1)+1)*(abs(y2-y1)+1)
            if area > max_area:
                max_area = area

print(max_area)