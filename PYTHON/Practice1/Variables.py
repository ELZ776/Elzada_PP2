# Creating variables with different data types
student_name = "Elzada"
student_age = 19

print(student_name)
print(student_age)

# Assigning multiple values in one line
city, country, year = "Almaty", "Kazakhstan", 2026

print(city)
print(country)
print(year)

# Assigning the same value to multiple variables
x = y = z = 100

print(x)
print(y)
print(z)

# Unpacking a list into variables
colors = ["red", "green", "blue"]

a, b, c = colors

print(a)
print(b)
print(c)

# Printing multiple variables using commas
first_name = "Elzada"
last_name = "Zhumabaikyzy"

print(first_name, last_name)

# Combining strings with the + operator
word1 = "Python "
word2 = "is "
word3 = "fun"

print(word1 + word2 + word3)

# Using indentation inside an if statement

if 7 > 3:
    print("Condition is true")

# Global variable remains unchanged 

course = "PP2"

def my_course():
    course = "Math"
    print("Inside function:",course)

my_course()

print("Outside function:",course)