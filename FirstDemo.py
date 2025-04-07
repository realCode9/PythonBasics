print("Hello world")

#this is comment in the python how it can be defined

#declare int variable
a = 3
print(a)

#declare string variable
name = "New Jersey"
print(name)

#declare more than one variable at the same line

b, c, d = 12, "third", 2.2
print(b)
print(c)
print(d)

print("{} {}".format("Name is", name))

# How to get the type of variable is
print(type(c))

# you can not concat two different data types
# print("age is " + b)    --> this is not possible in python
# BUT following is possible to concat similar data types like string and string
print("name is " + name)

firstName = "Robo"
lastName = 'Framework'

print("Full name is " + firstName + " " + lastName)

print(b+d)