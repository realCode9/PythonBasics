#FOR loop

# it can iterate from one point to other point

ageList = [20, 34, 23, 45, 55]

# Print age of each person from age List
for age in ageList:
    print(age)

# Calculate sum of first five natural numbers using for loop    1+2+3+4+5 = 15

addition = 0
# this range (i, j) will iterate from i to j-1 to do operation
for i in range(1, 6):
    addition= addition + i

print(addition)

print("********Skipping with 2 numbers ********")
for j   in range(2, 10, 2):
    print(j)

# Print sum of even numbers between 0 - 50
evenSum = 0
for s in range(0, 52, 2):
    print(s)
    evenSum = evenSum + s

print(evenSum)

print("*************Skipping first parameter of range***********")
for m in range(10):
    print(m)