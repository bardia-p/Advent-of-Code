import itertools

with open('input.txt', 'r') as file:
    lines = file.readlines()

machines = []

for line in lines:
    cleaned = line.strip().split()
    machine = dict()
    machine["goal"] = list(cleaned[0][1:-1])
    
    buttons = []
    for button in cleaned[1:-1]:
        buttons.append(list(map(int, button[1:-1].split(","))))

    machine["buttons"] = buttons
    machine["joltage"] = list(map(int, cleaned[-1][1:-1].split(",")))

    machines.append(machine)

total = 0

for machine in machines:
    num_buttons = 1
    found_combo = False
    while not found_combo:
        for combo in list(itertools.combinations(machine["buttons"], num_buttons)):
            state = ['.' for _ in machine["goal"]]
            for item in combo:
                for b in item:
                    state[b] = "." if state[b] == "#" else "#"
            
            if state == machine["goal"]:
                total += num_buttons
                found_combo = True
                break
        num_buttons += 1

print(total)