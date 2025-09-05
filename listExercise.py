lst = list((23, "age", "name", "Varun", 67))
print(len(lst))

poppedElement = lst.pop()       #No index to pop is given so it will remove last element of list by default
print(poppedElement)
print(lst)

lst.append(68)
print(lst)
lst.extend((69, "dist", 70))
print(lst)
lst.extend("abcd")
print(lst)
lst.extend([12, 13, 14])
print(lst)

for item in lst:
    print(item)

lst.insert(12, "This is Pyhton Basics")

lengthOfList = len(lst)
print("Length of the updated, added, extended, removed, popped list")
print(lengthOfList)
print("------------====-------------")

for i in range(lengthOfList):
    print(lst[i])

print("Index of element inserted")
indexOfPythonBasic = lst.index("This is Pyhton Basics")
print(indexOfPythonBasic)