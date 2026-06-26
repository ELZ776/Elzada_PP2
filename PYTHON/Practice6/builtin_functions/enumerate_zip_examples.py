# enumerate() gives index and value from a list
names = ["Ali", "Dana", "Miras"]
for index, name in enumerate(names):
    print(index, name)

# enumerate() can start counting from any number
subjects = ["Math", "Python", "Physics"]
for number, subject in enumerate(subjects, start=1):
    print(number, subject)

# zip() combines two lists together
names = ["Ali", "Dana", "Miras"]
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(name, score)

# type() shows the data type
# isinstance() checks the data type

x = 25
name = "Python"
print(type(x))
print(type(name))
print(isinstance(x, int))
print(isinstance(name, str))