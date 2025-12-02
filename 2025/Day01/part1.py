with open('input.txt', 'r') as file:
    lines = file.readlines()

zero_count =0
score = 50

for code in lines:
    cleaned_code = code.strip()
    amount = int(cleaned_code[1:])
    move = cleaned_code[0]
    score = (score + amount if move == 'R' else score - amount) % 100

    if score == 0:
        zero_count += 1
print(zero_count)