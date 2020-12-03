## Advent of code Day 2

with open("input.txt", "r") as f:
    rawInput = f.readlines()

p1ValidPasswords = 0

for line in rawInput:
    splitLine = line.split(" ")
    minMax = splitLine[0].split("-")
    letter = splitLine[1].rstrip(":")
    password = splitLine[2].rstrip("\n")
    
    occurrences = password.count(letter)
    if (occurrences >= int(minMax[0])) and (occurrences <= int(minMax[1])):
        p1ValidPasswords += 1

print("Part 1 valid passwords:", p1ValidPasswords)

p2ValidPasswords = 0

for line in rawInput:
    splitLine = line.split(" ")
    positions = splitLine[0].split("-")
    positions = list(map(int, positions))
    
    letter = splitLine[1].rstrip(":")
    password = splitLine[2].rstrip("\n")
    
    if (password[positions[0]-1] == letter) ^ (password[positions[1]-1] == letter):
        p2ValidPasswords += 1

print ("Part 2 valid passwords:", p2ValidPasswords)