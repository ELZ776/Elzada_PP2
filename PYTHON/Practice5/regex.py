import re

# 1. Match a string that has 'a' followed by zero or more 'b's
def task1(text):
    pattern = r"ab*"
    return bool(re.fullmatch(pattern, text))


# 2. Match a string that has 'a' followed by two to three 'b'
def task2(text):
    pattern = r"ab{2,3}"
    return bool(re.fullmatch(pattern, text))


# 3. Find sequences of lowercase letters joined with an underscore
def task3(text):
    pattern = r"\b[a-z]+_[a-z]+\b"
    return re.findall(pattern, text)


# 4. Find sequences of one uppercase letter followed by lowercase letters
def task4(text):
    pattern = r"\b[A-Z][a-z]+\b"
    return re.findall(pattern, text)


# 5. Match a string that has 'a' followed by anything, ending in 'b'
def task5(text):
    pattern = r"a.*b"
    return bool(re.fullmatch(pattern, text))


# 6. Replace all occurrences of space, comma, or dot with a colon
def task6(text):
    pattern = r"[ ,.]"
    return re.sub(pattern, ":", text)


# 7. Convert snake case string to camel case string
def task7(text):
    return re.sub(r"_([a-z])", lambda match: match.group(1).upper(), text)


# 8. Split a string at uppercase letters
def task8(text):
    return re.split(r"(?=[A-Z])", text)


# 9. Insert spaces between words starting with capital letters
def task9(text):
    return re.sub(r"(?<!^)(?=[A-Z])", " ", text)


# 10. Convert camel case string to snake case
def task10(text):
    snake_case = re.sub(r"(?<!^)(?=[A-Z])", "_", text)
    return snake_case.lower()


# Test examples
print("Task 1:", task1("abbb"))
print("Task 2:", task2("abb"))
print("Task 3:", task3("hello_world test_example Python_Code"))
print("Task 4:", task4("Hello World python Test"))
print("Task 5:", task5("a12345b"))
print("Task 6:", task6("Hello, world. Python regex"))
print("Task 7:", task7("hello_world_python"))
print("Task 8:", task8("HelloWorldPython"))
print("Task 9:", task9("HelloWorldPython"))
print("Task 10:", task10("helloWorldPython"))