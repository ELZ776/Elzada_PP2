# Import json module
import json

x = '{ "name": "John", "age": 30, "city": "New York" }'

y = json.loads(x)

print(y["age"])

# Import json module
import json

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)

print(y)

# Import json module
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Import json module
import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

# Import json module
import json


x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


y = json.dumps(x, indent=4)

print(y)

# Import json module
import json


x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x, indent=4, separators=(". ", " = "))

print(y)