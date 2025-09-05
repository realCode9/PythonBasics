tup = (1, 2, 3, 4,33, 3)
print(tup)

tup.count(2)
print(tup.count(3))

print(tup.index(33))

print(tup[-1])
print(tup[-4])
print(tup[-4:])
print(tup[1:3])
print("---------------==============----------------")
#Packing and unpacking tuples
print("---------------=======-----Packing and unpacking-------=======----------------")
fruits = ("banana", "orange", "Kiwi", "Guava")
(one, two, three, four) = fruits
print(one)
print(two)
print(three)
print(four)

print(fruits)

print("___________UNPACKING TUPLE______________")

fruits1 = ("banana", "orange", "Kiwi", "Guava", "Dragon", "Apple", "Strawberry", "Cherry")
(dailyFruit, *occasionalFruit, primeFruits) = fruits1
print(occasionalFruit)
print(dailyFruit)
print(primeFruits)

#Looping onto tuple
# for item in tup:
#     print("Tuple item index")
#     print(tup.index(item))
#     print(item)
print("---------------==============----------------")
# Using for Loop with range
print("Print values of tuple with in range")
# for i in range(len(tup)):
#     print(tup[i])

print("-----------------Print values of tuple with while loop--------------------")
i=0
while i<len(tup):
    print(tup[i])
    i=i+1
#Join tuple
print("---------------==============----------------")

tup1 = (1, 2, 4)
tup2 = ("Varun", "Tarun", "Arun")
tup3 = tup1 + tup2
print("Tuple Join Result below")
print(tup3)
#Multiply tuple
print(tup1 * 2)
#CHanging and updating tuple
updateTup = list(tup)       #As we can not directly update tuple can change it to list using list constructor and update/modify.add
print(updateTup)
print(tup)
updateTup.append("UpdateValue")
print(updateTup)

#CHeck value in tuple
if 33 in tup:
    print("Value is present in the tuple")