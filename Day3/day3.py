## Advent of Code Day 3

with open("input.txt", "r") as f:
    coords = f.readlines()

xpos = 0
trees = 0

coords = map(lambda l: l.strip(), coords)

for line in coords:
    normalisedXPos = xpos % len(line)
    if line[normalisedXPos] == '#':
        trees += 1
    print(xpos, normalisedXPos, line[normalisedXPos])
    xpos += 3

print("Trees:", trees)