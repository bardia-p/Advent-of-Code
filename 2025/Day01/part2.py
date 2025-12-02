with open('input.txt', 'r') as file:
    lines = file.readlines()

zero_count = 0
score = 50

for code in lines:
    cleaned_code = code.strip()
    amount = int(cleaned_code[1:])
    move = cleaned_code[0]

    if move == 'R':
        to_zero = 100 - score
        sign = 1
    else:
        to_zero = score
        sign = -1
        
    if to_zero == 0:
        to_zero = 100
    if amount >= to_zero:
        zero_count += 1 + abs(amount - to_zero) // 100
        
    score = (score + sign * amount) % 100

print(zero_count)