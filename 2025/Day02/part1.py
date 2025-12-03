with open('input.txt', 'r') as file:
    lines = file.readlines()

total = 0
for r in lines[0].strip().split(','):
    start, end = map(int, r.split('-'))
    total += sum(
        val for val in range(start, end + 1)
        if (s := str(val)) and len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]
    )

print(total)