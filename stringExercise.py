

string1 = "I love India, love Maharashtra"
slicedString1=string1[2:6]
print(slicedString1)
slicedString2=string1[:6]
print(slicedString2)
slicedString3=string1[6:14]
print(slicedString3)

replacedString1=string1.replace("love", "Admire")
print(replacedString1)

lengthOfString = len(string1)
print(lengthOfString)

print(slicedString3)
strippedString= slicedString3.strip()
print(strippedString)

#As we can not concatenate different data types in python we can use format method to do so
name = "Vijay"
age= 28
livenIn = 'Pune'

completeInfo = "My name is {} with age {} and I live in {}.".format(name, age, livenIn)
print(completeInfo) #My name is Vijay with age 28 and I live in Pune.

print(completeInfo.index("Vijay"))

#in keyword returns true if substring present in main string
print("Vijay" in completeInfo)
print("India" in completeInfo)

print(completeInfo.startswith("I"))
print(completeInfo.startswith("My"))

print(completeInfo.endswith(livenIn+"."))
