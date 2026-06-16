# Class with __init__()
class Person:
    def __init__(self, name, age):
        self.name = name  # Object property
        self.age = age    # Object property

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

# Class without __init__()
class Person:
    pass

p1 = Person()

p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

# Class with __init__()
class Person:
    def __init__(self, name, age):
        self.name = name  # Set name
        self.age = age    # Set age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)

# Class with default age
class Person:
    def __init__(self, name, age=18):
        self.name = name  # Set name
        self.age = age    # Set age or default age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

# Class with multiple parameters
class Person:
    def __init__(self, name, age, city, country):
        self.name = name        # Set name
        self.age = age          # Set age
        self.city = city        # Set city
        self.country = country  # Set country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)