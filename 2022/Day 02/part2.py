f = open("Day 2/input.txt", "r")

lines = f.readlines()

moves = {"A":1, "B":2, "C":3, "X":0, "Y":3, "Z":6}

points = 0 

for line in lines:
    currMove = line.strip().split()

    otherHand = currMove[0]
    result = moves[currMove[1]]

    if otherHand == "A":
        if result == 0:
            yourMove = "C"
        elif result == 3:
            yourMove = "A"
        else:
            yourMove = "B"

    elif otherHand == "B":
        if result == 0:
            yourMove = "A"
        elif result == 3:
            yourMove = "B"
        else:
            yourMove = "C"

    elif otherHand == "C":
        if result == 0:
            yourMove = "B"
        elif result == 3:
            yourMove = "C"
        else:
            yourMove = "A"


    yourHand = moves[yourMove]

    points += yourHand + result

print(points)

f.close()