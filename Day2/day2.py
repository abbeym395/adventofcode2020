## Advent of code Day 2

with open("input.txt", "r") as f:
    rawInput = f.readlines()

validPasswords = 0

for line in rawInput:
    splitLine = line.split(" ")
    minMax = splitLine[0].split("-")
    letter = splitLine[1].rstrip(":")
    password = splitLine[2].rstrip("\n")
    
    occurrences = password.count(letter)
    if (occurrences >= int(minMax[0])) and (occurrences <= int(minMax[1])):
        validPasswords += 1

print("Valid passwords:", validPasswords)