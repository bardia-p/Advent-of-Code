f = open("Day 5/input.txt", "r")

lines = f.readlines()

table = []

for line in lines:
    if "move" in line:
        row = line.split(" ")

        count = int(row[1])
        source = int(row[3]) - 1
        to = int(row[5]) - 1

        table[to] += table[source][-count:][::-1]
        del table[source][-count:]
    elif "[" in line:
        row = line.split(" ")

        spaceCounter = 0
        
        tableRow = []

        for col in row:
            if col == "" or col == "\n":
                spaceCounter += 1

                if spaceCounter == 4:
                    spaceCounter = 0
                    tableRow.append(" ")
            elif "[" in col:
                spaceCounter = 0
                tableRow.append(col[1])

        if len(table) == 0:
            table = [[] if i == " " else [i] for i in tableRow]
        else:
            for i in range(len(tableRow)):
                if tableRow[i] != " ":
                    table[i].insert(0, tableRow[i]) 
                           
finalWord = ""

for c in table:
    finalWord += c[-1]

print(finalWord)
