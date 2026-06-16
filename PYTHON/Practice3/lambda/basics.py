# Basic lambda functions

# One argument
add_ten = lambda a: a + 10
print(add_ten(5))

# Two arguments
multiply = lambda a, b: a * b
print(multiply(5, 6))

# Three arguments
sum_values = lambda a, b, c: a + b + c
print(sum_values(5, 6, 2))

# Lambda returned from a function
def multiplier(n):
    return lambda a: a * n

double = multiplier(2)
triple = multiplier(3)

print(double(11))
print(triple(11))