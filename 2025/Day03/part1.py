with open('input.txt', 'r') as file:
    lines = file.readlines()

total = 0
for line in lines:
    digits = list(map(int, list(line.strip())))
    index = digits.index(max(digits))
    if index == len(digits) -1:
        index = digits.index(max(digits[:len(digits)-1]))

    highest = digits[index]
    second_highest = max(digits[index+1:])


    total += highest * 10 + second_highest

print(total)

