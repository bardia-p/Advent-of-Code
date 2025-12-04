with open('input.txt', 'r') as file:
    lines = file.readlines()

def make_biggest_number(digits, num_digits):
    if len(digits) == 0 or num_digits <= 0:
        return ""
    
    curr_max = max(digits)
    curr_idx = digits.index(curr_max)
    
    if num_digits - 1 <= len(digits) - curr_idx - 1:
        return str(curr_max) + make_biggest_number(digits[curr_idx+1:], num_digits - 1)
    else:
        left_overs = num_digits - (len(digits) - curr_idx)
        return make_biggest_number(digits[:curr_idx], left_overs) + str(curr_max) + make_biggest_number(digits[curr_idx+1:], num_digits - left_overs - 1) 
    
total = 0
for line in lines:
    digits = list(map(int, list(line.strip())))
    number = make_biggest_number(digits, 12)
    total += int(number)

print(total)
