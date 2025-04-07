#Functions in the programming language is block of code that perform specific task on calling it up and can be
# used multiple times to optimize the code

# In python - function declared done with def keyword and after naming the function : should be used

# Normal function
def print_name():
    print("My name is Gopi")

# Function with arguments
def add_numbers(a, b):
    print(a+b)

# Function with return type
def average_of_numbers(a, b, c):
    d = (a + b + c)/3
    return d

print_name()
add_numbers(3,5)
print(average_of_numbers(8, 9, 7))