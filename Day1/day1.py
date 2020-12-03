## Advent of Code - Day 1, question 1

with open("input.txt", "r") as f:
    expensesStrings = f.readlines()

expenses = []
for line in expensesStrings:
    expenses.append(int(line[:-1]))
    
expensesAsc = sorted(expenses)
expensesDesc = sorted(expenses, reverse=True)

print("For part 1")
for item in expensesAsc:
    if 2020 - item in expensesAsc:
        print("Numbers are", item, "and", 2020 - item)
        print("Solution is", item * (2020 - item))
        break
    
print("For part 2")

for firstItem in expensesAsc:
    for secondItem in expensesDesc:
        #print(firstItem, secondItem, newNumber)
        if 2020 - firstItem - secondItem in expensesAsc:
            print("Numbers are", firstItem, secondItem, "and", 2020 - firstItem - secondItem)
            print("Solution is", firstItem * secondItem * (2020 - firstItem - secondItem))