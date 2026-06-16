# Function with one parameter

def my_function(name):
    print("Hello", name)

my_function("Elzada")

# Function with two arguments

def full_name(fname, lname):
    print(fname, lname)

full_name("Elzada", "Zhumabaikyzy")

# Function with default parameter

def greet(name="friend"):
    print("Hello", name)

greet()
greet("Elzada")

# Using keyword arguments

def pet(animal, name):
    print(animal, name)

pet(name="Buddy", animal="Dog")

# Using positional arguments

def pet(animal, name):
    print(animal, name)

pet("Dog", "Buddy")

# Passing a list to a function

def show_fruits(fruits):
    for fruit in fruits:
        print(fruit)

show_fruits(["apple", "banana", "cherry"])

# Passing a dictionary to a function

def show_person(person):
    print(person["name"])

show_person({"name": "Elzada"})

# Returning a value

def add(x, y):
    return x + y

result = add(5, 3)

print(result)

# Returning a list

def get_fruits():
    return ["apple", "banana", "cherry"]

print(get_fruits())

# Returning a tuple

def get_coordinates():
    return (10, 20)

x, y = get_coordinates()

print(x)
print(y)

# Positional-only argument

def my_function(name, /):
    print("Hello", name)

my_function("Emil")

# Keyword-only argument

def my_function(*, name):
    print("Hello", name)

my_function(name="Emil")

# Combining positional-only and keyword-only arguments

def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c=15, d=20)

print(result)