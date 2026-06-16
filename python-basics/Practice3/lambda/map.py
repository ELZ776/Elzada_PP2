# Using lambda with map()

numbers = [1, 2, 3, 4, 5]

# Double every number
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Square every number
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Add 100 to every number
plus_hundred = list(map(lambda x: x + 100, numbers))
print(plus_hundred)