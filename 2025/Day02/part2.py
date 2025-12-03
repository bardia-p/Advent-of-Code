with open('input.txt', 'r') as file:
    lines = file.readlines()

total = 0
for r in lines[0].strip().split(','):
    start, end = map(int, r.split('-'))
    for val in range(start, end + 1):
        s = str(val)
        for m in range(1, len(s)//2 + 1):
            if len(s) == m * s.count(s[:m]):
                total += val
                break

print(total)