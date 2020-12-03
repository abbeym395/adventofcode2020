## Advent of Code - Day 1, question 1

with open("input.txt", "r") as f:
    expensesStrings = f.readlines()

expenses = []
for line in expensesStrings:
    expenses.append(int(line[:-1]))
    
expensesAsc = sorted(expenses)
expensesDesc = sorted(expenses, reversed=True)

print("For part 1")
for item in expensesAsc:
    if 2020 - item in expensesAsc:
        print("Numbers are", item, "and", 2020 - item)
        print("Solution is", item * (2020 - item))
        break
    
print("For part 2")
print(expensesAsc)

firstItem = 0
secondItem = 0
