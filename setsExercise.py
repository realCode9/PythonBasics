from os import remove

s = {1, 2, 3, 4, 5, 5}
print(s)
s.add(12)
print(s)
s.add("Varun")
print(s)

print("_______Print set items___________")
# access set items
for item in s:
    print(item)

# Set methods
print(len(s))
if 15 in s:
    print("Item is present in set")
elif 23 not in s:
    print("Correct item is not in list")
# s.clear()     #This will clear all the elements from the set and returns empty set as set()
print(s)
s.remove(12)    #If item to be removed is not present in the set then it will show error
print(s)
s.discard(17)   #If item to be removed is not present in the set then it will not show error
print(s)

# Join Sets\
set1 = {2, 5, 7, 10, 12, 15}
set2 = {3, 6, 8, 10, 15, 5}
set3 = set1.union(set2)
print(set3)

print("Union using |")
set4 = set1 | set2
print(set4)

# intersection
print("intersection using method name")
set5 = set1.intersection(set2)
print(set5)
print("intersection using & name")
set6 = set1 & set2
print(set6)
set7 = set1.difference(set2)    #Difference will check not common items from first set only and returns it
print(set7)

set8 = set1.update(set2)        #Update method will not return new set with update it will add all items of second set into first set and return first set
print(set1)

s1 = {2, 5, 7, 10, 12, 15}
s2 = {3, 6, 8, 10, 15, 5}

s1.intersection_update(s2)   #also keep the duplicates but will not return new set make changes to first set only
print(s1)