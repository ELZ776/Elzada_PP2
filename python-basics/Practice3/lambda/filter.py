# Using lambda with filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Numbers greater than 5
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)