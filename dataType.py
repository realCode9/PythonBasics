# There are mainly five data types in python
# 1. Numeric
#     int, float, long and complex lie into parent numeric data type in python
#     There is no need to declare data type in front of variable name in python when declared
# 2. String
#        String can be written in single or double quote
#        we can concat similar data type in python using + symbol
#        We can also concat numeric datatype but it will calculated as sum of two numbers
# 3. List
#       List is a data type that allows to store multiple values that may be of any data type
#       We can add, update, delete, append(enter value at the end of the list)
#       Also we can get value at the last index of the list with -1
#       we can replace values from the list

person = ["Varun", 19, "Square one, New Jersey", 8989765438, 99.01]
# print list
print(person)
# get values at the index
print(person[0])    #Varun
print(person[2])
print(person[4])

# print value at the last using -1
print(person[-1])
# add at the last index of the list and print
person.append("Joint Family")
print(person)

# Update joint family object of person to individual
person[5]   = 'Individual'
print(person)

# Deleted family type individual
del person[5]
print(person)

# Replace age 19 to 20
person[1]  = 20
print(person)
# 4. Dictionary
# In dictionary we can store values in key value pair and can be accessed with the help of key assigned to the value
#If key is string use "" while access
#  If Value is String it will return as string

# It will be written in CURLY BRACKETS

dicData = {1: "Gopi", 2:"Gud", "age": 24, "interest": 6.8}
print(dicData[1])
print(dicData["age"])
print(dicData["interest"])


# 5. Tuple
#Touple is the data type to store values but immutable that means assignments/update/delete/replace will not
# possible like LISTS
#It will be written in the  ROUND BRACKETS
tupleData = (1, 2, 33, "Gopi", 4.4)
print(tupleData[0])
print(tupleData[3])
# tupleData[2] = 50     This will give compilation error - Touple dont support item assignments

