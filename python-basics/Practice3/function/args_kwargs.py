# Using *args to accept multiple arguments

def my_function(*kids):
    print("The youngest child is", kids[2])

my_function("Emil", "Tobias", "Linus")

# Accessing values from *args

def my_function(*args):
    print(type(args))
    print(args[0])
    print(args[1])

my_function("Emil", "Tobias", "Linus")

# Combining regular parameters and *args

def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

# Summing values with *args

def my_function(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print(my_function(1, 2, 3))

# Finding maximum value with *args

def my_function(*numbers):
    return max(numbers)

print(my_function(3, 7, 2, 9, 1))

# Using **kwargs to accept keyword arguments

def my_function(**kid):
    print("Last name:", kid["lname"])

my_function(fname="Tobias", lname="Refsnes")

# Accessing values from **kwargs

def my_function(**data):
    print(type(data))
    print(data["name"])

my_function(name="Tobias", age=30)

# Combining regular parameters and **kwargs

def my_function(username, **details):
    print(username)

    for key, value in details.items():
        print(key, value)

my_function("emil123", age=25, city="Oslo")

# Using *args and **kwargs together

def my_function(title, *args, **kwargs):
    print(title)
    print(args)
    print(kwargs)

my_function("User Info", "Emil", "Tobias", age=25, city="Oslo")

# Unpacking a list with *

def my_function(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

print(my_function(*numbers))

# Unpacking a dictionary with **

def my_function(fname, lname):
    print(fname, lname)

person = {
    "fname": "Emil",
    "lname": "Refsnes"
}

my_function(**person)