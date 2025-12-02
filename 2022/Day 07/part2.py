class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dir:
    def __init__ (self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = dict()
        self.size = 0

    def addDir(self, dir):
        self.dirs[dir.name] = dir

    def addFile(self, file):
        self.files.append(file)

def getSize(node):
    if node.size > 0:
        return node.size

    res = 0

    for file in node.files:
        res += file.size

    for dir in node.dirs.values():
        res += getSize(dir)

    node.size = res
    return res

def findSmallestDir(node, toDelete):
    if node.size >= toDelete:
        res = node.size
    else:
        res = 70000000

    for dir in node.dirs.values():
        res = min(res, findSmallestDir(dir, toDelete))

    return res

f = open("Day 7/input.txt", "r")

lines = f.readlines()

root = Dir("/", None)
root.parent = root
currDir = root 


for line in lines:
    command = line.strip().split(" ")

    if "$" in line:
        if command[1] == "cd":
            name = command[2]
            if name == "..":
                currDir = currDir.parent
            elif name == "/":
                currDir = root
            else:
                currDir = currDir.dirs[name]
    else:
        if command[0] == "dir":
            name = command[1]
            if name not in currDir.dirs:
                newDir = Dir(name, currDir)
                currDir.addDir(newDir)
        else:
            size = int(command[0])
            name = command[1]

            currDir.addFile(File(name, size))

freeSpace = 70000000 - getSize(root)

if freeSpace < 30000000:
    toDelete = 30000000 - freeSpace

    print(findSmallestDir(root, toDelete))

f.close()

