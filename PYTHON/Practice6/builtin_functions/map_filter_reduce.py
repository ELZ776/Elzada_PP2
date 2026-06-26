# map() applies a function to each item in a list
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print(result)

# map() can change every string in a list
words = ["apple", "banana", "cherry"]
result = list(map(lambda word: word.upper(), words))
print(result)

# filter() keeps only items that satisfy the condition
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

# filter() keeps only words longer than 5 letters
words = ["cat", "elephant", "dog", "python", "sun"]
result = list(filter(lambda word: len(word) > 5, words))
print(result)