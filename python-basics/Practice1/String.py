# Working with strings and length
message = "Hello Python"

print(message)
print(len(message))

# Checking if a word exists in a string

text = "Python programming is fun"

if "Python" in text:
    print("Word found")

if "Java" not in text:
    print("Java is not present")

# Accessing different positions in a string
city = "Atyrau"

print(city[0])
print(city[3])
print(city[5])

# Basic slicing
text = "Programming"

print(text[0:4])
print(text[4:7])

# Slice from start and to end
word = "Python"

print(word[:3])
print(word[3:])

# Negative slicing
text = "Hello, World!"

print(text[-6:-1])

# Demonstrating common string methods
text = " Hello, Python World! "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Python", "Programming"))
print(text.split(","))

# Creating a sentence using concatenation
subject = "Python"
level = "Beginner"

message = subject + " " + level

print(message)

#Using f-string with variables

name = "Elzada"
age = 18 

print(f"My name is {name}")
print(f"I am {age} years old")

# Demonstrating common escape characters
print("Hello\nWorld")
print("Name:\tElzada")
print("He said \"Python is fun\"")

# Using escape characters in file paths
path = "C:\\Users\\Elzada\\Documents"

print(path)

quote = "It's a \"great\" day"

print(quote)