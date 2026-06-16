print(True)   # Boolean value: True
print(False)  # Boolean value: False

print(bool("Python"))  # Non-empty string returns True
print(bool(100))       # Non-zero number returns True
print(bool(""))        # Empty string returns False
print(bool(0))         # Zero returns False

def my_function():
    return True        # Function returns a Boolean value
print(my_function())

x = 200
print(isinstance(x, int))  # Checks if x is an integer, returns True