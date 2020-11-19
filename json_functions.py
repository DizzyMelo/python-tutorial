# Python JSON
# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.

# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.

import json

# some JSON:
jsonStr = '{ "name":"John", "age":30, "city":"New York"}'

# parse jsonStr:
x = json.loads(jsonStr)

# the result is a Python dictionary:
print(x['name'])
print(type(x))

# a Python object (dict):
x = {
    'name': 'Daniel',
    'age': 45,
    'city': 'Natal'
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))

# You can convert Python objects of the following types, into JSON strings:

# Basically, the loads() method is resposible for converting a valid json string into a dictionary, and the dumps()
# method is responsible for converting an object into a valid json string

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
