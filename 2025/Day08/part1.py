import heapq
import math 

with open('input.txt', 'r') as file:
    lines = file.readlines()

distances_priority_queue = [] 

for i in range(len(lines)):
    lines[i] = tuple(map(int, lines[i].strip().split(',')))

for i in range(len(lines)):
    p1 = lines[i]
    for j in range(i+1, len(lines)):
        p2 = lines[j]
        distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
        heapq.heappush(distances_priority_queue, (distance, (p1, p2)))

teams = [[l] for l in lines]

for i in range(1000):
    distance, (p1, p2) = heapq.heappop(distances_priority_queue)
    for team in teams:
        if p1 in team:
            p1_team = team
        if p2 in team:
            p2_team = team

    if p1_team != p2_team:
        teams.remove(p1_team)
        teams.remove(p2_team)
        teams.append(p1_team + p2_team)

teams.sort(key=lambda x: len(x))
print(len(teams[-1]) * len(teams[-2]) * len(teams[-3]))
        
