f = open("Day 8/input.txt", "r")

trees = [list(map(int,list(line.strip()))) for line in f.readlines()]

def getScore(i, j):
    global trees

    if i == 0 or j == 0 or i == len(trees) - 1 or j == len(trees[0]) - 1:
        return 0

    score = 1

    for k in range(i-1, -1, -1):
        if trees[k][j] >= trees[i][j] or k == 0:
            score *= (i - k)
            break

    for k in range(j-1, -1, -1):
        if trees[i][k] >= trees[i][j] or k == 0:
            score *= (j - k)
            break

    for k in range(i+1, len(trees)):
        if trees[k][j] >= trees[i][j] or k == len(trees) - 1:
            score *= (k - i)
            break

    for k in range(j+1, len(trees[0])):
        if trees[i][k] >= trees[i][j] or k == len(trees) - 1:
            score *= (k - j)
            break

    return score

maxScore = 0

for i in range(len(trees)):
    for j in range(len(trees[0])):
        maxScore = max(maxScore, getScore(i, j))

print(maxScore)

f.close()