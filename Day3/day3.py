## Advent of Code Day 3

with open("input.txt", "r") as f:
    coords = f.readlines()

xpos = 0
trees = 0

coords = list(map(lambda l: l.strip(), coords))

for line in coords:
    normalisedXPos = xpos % len(line)
    if line[normalisedXPos] == '#':
        trees += 1
    xpos += 3

print("Part 1 trees:", trees)

# Part 2
import math

def findTrees(x, y, coords):
    trees = 0
    xpos = 0
    coords = coords[::y]
    for line in coords:
        normalisedXPos = xpos % len(line)
        if line[normalisedXPos] == '#':
            trees += 1
        xpos += x
    return trees

results = []
results.append(findTrees(1, 1, coords))
results.append(findTrees(3, 1, coords))
results.append(findTrees(5, 1, coords))
results.append(findTrees(7, 1, coords))
results.append(findTrees(1, 2, coords))

print("The answers are:", results)
print("The final answer is", math.prod(results))