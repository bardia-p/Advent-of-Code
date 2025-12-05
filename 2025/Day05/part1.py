with open('input.txt', 'r') as file:
    lines = file.readlines()

intervals = []
count = 0
for line in lines:
    if "-" in line:
        s,e = line.strip().split("-")
        intervals.append((int(s), int(e)))
    elif line == "\n":
        intervals.sort(key= lambda x: x[0])
        merged_intervals = []
        for interval in intervals:
            if len(merged_intervals) == 0 or interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1] = (min(merged_intervals[-1][0], interval[0]), max(merged_intervals[-1][1], interval[1]))
    else:
        to_find = int(line.strip())
        for interval in merged_intervals[::-1]:
            if to_find > interval[1]:
                break
            elif to_find >= interval[0] and to_find <= interval[1]:
                count += 1
                break

print(count)