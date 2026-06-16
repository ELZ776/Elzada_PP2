# Creating a function
def my_function():
    print("Hello from a function")

# Calling the function
my_function()

# Calling the same function multiple times
def my_function():
    print("Hello from a function")

my_function()
my_function()
my_function()

# Function with a parameter
def say_hello(name):
    print("Hello", name)

say_hello("Ashley")

# Function returning a value
def get_greeting():
    return "Hello from a function"

print(get_greeting())

# Saving the returned value
def get_greeting():
    return "Hello from a function"

message = get_greeting()

print(message)

# Function performing a calculation
def add():
    return 2 + 3

result = add()

print(result)

# Reusing code with a function
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# Empty function placeholder
def my_function():
    pass