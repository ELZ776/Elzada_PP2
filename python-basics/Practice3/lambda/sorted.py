# Using lambda with sorted()

# Sort tuples by age
students = [
    ("Emil", 25),
    ("Tobias", 22),
    ("Linus", 28)
]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)

# Sort strings by length
words = ["apple", "pie", "banana", "cherry"]

sorted_words = sorted(words, key=lambda x: len(x))

print(sorted_words)

# Sort numbers descending
numbers = [5, 2, 8, 1, 9]

sorted_numbers = sorted(numbers, key=lambda x: x, reverse=True)

print(sorted_numbers)