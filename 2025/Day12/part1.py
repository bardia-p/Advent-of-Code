from functools import lru_cache

with open('input.txt', 'r') as file:
    lines = file.readlines()

shapes = []
regions = []
i = 0
while i < len(lines):
    cleaned = lines[i].strip()
    if 'x' in cleaned:
        split = cleaned.split()
        size = split[0][:-1].split('x')
        regions.append([int(size[0]), int(size[1]), list(map(int, split[1:]))])
        i += 1
    elif ':' in cleaned:
        shape = set()
        i += 1
        for y in range(3):
            for x in range(3):
                if lines[i + y][x] == "#":
                    shape.add((x, y))
        i += 3
        shapes.append(shape)
    else:
        i += 1

def normalize(cells):
    minx = min(x for x, y in cells)
    miny = min(y for x, y in cells)
    return frozenset((x - minx, y - miny) for x, y in cells)

def rotations_and_flips(cells):
    variants = set()
    pts = list(cells)

    for _ in range(4):
        pts = [(y, -x) for x, y in pts]
        for sx in (1, -1):
            flipped = [(sx * x, y) for x, y in pts]
            variants.add(normalize(flipped))

    return list(variants)

def shape_to_mask(cells, width):
    mask = 0
    for x, y in cells:
        mask |= 1 << (y * width + x)
    return mask

def can_pack(W, H, shapes, counts, shape_orients):
    instances = []
    for sid, c in enumerate(counts):
        instances.extend([sid] * c)

    if not instances:
        return True

    placements = {}
    areas = {}

    for sid in set(instances):
        plist = []
        area = len(shapes[sid])
        areas[sid] = area

        for orient in shape_orients[sid]:
            maxx = max(x for x, y in orient)
            maxy = max(y for x, y in orient)

            for dx in range(W - maxx):
                for dy in range(H - maxy):
                    mask = shape_to_mask(
                        ((x + dx, y + dy) for x, y in orient), W
                    )
                    plist.append(mask)

        if not plist:
            return False

        placements[sid] = plist

    instances.sort(key=lambda i: len(placements[i]))

    remaining_area = [0] * (len(instances) + 1)
    for i in range(len(instances) - 1, -1, -1):
        remaining_area[i] = remaining_area[i + 1] + areas[instances[i]]

    total_cells = W * H

    @lru_cache(None)
    def backtrack(i, used_mask):
        used = used_mask.bit_count()
        if remaining_area[i] > total_cells - used:
            return False

        if i == len(instances):
            return True

        sid = instances[i]
        for mask in placements[sid]:
            if used_mask & mask == 0:
                if backtrack(i + 1, used_mask | mask):
                    return True
        return False

    return backtrack(0, 0)

def solve(shapes, regions):
    shape_orients = [rotations_and_flips(s) for s in shapes]
    ans = 0

    for W, H, counts in regions:
        if can_pack(W, H, shapes, counts, shape_orients):
            ans += 1

    return ans

print(solve(shapes, regions))