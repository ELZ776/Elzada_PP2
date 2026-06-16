# Creating a class

class MyClass:
    x = 5

p1 = MyClass()

print(p1.x)

# Creating multiple objects

class MyClass:
    x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# Deleting an object

class MyClass:
    x = 5

p1 = MyClass()

del p1

# Empty class

class Person:
    pass