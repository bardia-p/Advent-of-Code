f = open("Day 8/input.txt", "r")

trees = [list(map(int,list(line.strip()))) for line in f.readlines()]

def canSee(i, j):
    global trees

    left = True
    right = True
    top = True
    bottom = True
    

    for k in range(i-1, -1, -1):
        if trees[k][j] >= trees[i][j]:
            top = False
            break

    for k in range(j-1, -1, -1):
        if trees[i][k] >= trees[i][j]:
            left = False
            break

    for k in range(i+1, len(trees)):
        if trees[k][j] >= trees[i][j]:
            bottom = False
            break

    for k in range(j+1, len(trees[0])):
        if trees[i][k] >= trees[i][j]:
            right = False
            break

    return top or left or bottom or right

treeCounter = 0 


for i in range(len(trees)):
    for j in range(len(trees[0])):
        if canSee(i, j):
            treeCounter += 1


print(treeCounter)

f.close()