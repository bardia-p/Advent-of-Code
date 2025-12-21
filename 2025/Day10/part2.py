import pulp

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
    buttons = machine['buttons']
    target = machine['joltage']
    num_buttons = len(buttons)
    num_counters = len(target)

    prob = pulp.LpProblem("MinButtonPresses", pulp.LpMinimize)

    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(num_buttons)]

    prob += pulp.lpSum(x)

    for c in range(num_counters):
        prob += pulp.lpSum(x[i] for i in range(num_buttons) if c in buttons[i]) == target[c]

    solver = pulp.PULP_CBC_CMD(msg=False)
    prob.solve(solver)

    if pulp.LpStatus[prob.status] == "Optimal":
        total += int(sum(var.value() for var in x))
    else:
        print("No solution found")

print(total)
