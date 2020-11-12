# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(type(thisdict))

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

print(thisdict['model'])

# There is also a method called get() that will give you the same result:

print(thisdict.get('model'))

# Change Values
# You can change the value of a specific item by referring to its key name:

thisdict['year'] = 2018
print(thisdict)

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Will return the keys
for x in thisdict:
    print(x)

# Will return the values
for x in thisdict:
    print(thisdict[x])

# Will return the values
for x in thisdict.values():
    print(x)

# Return both key and value
for x, y in thisdict.items():
    print(x, y)

if 'model' in thisdict:
    print('Yes, the dict contains a field called mocel')
else:
    print('No, the field doesnt exist')

# Check dictionary length
print('Number of items in the dict: {}'.format(len(thisdict)))

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict['color'] = 'red'
print(thisdict)

# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:

thisdict.pop('model')
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict.popitem()
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

del thisdict['year']
print(thisdict)

del thisdict
# print(thisdict) this will raise an error once the dict no longer exists

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.clear()
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# mydict = thisdict.copy()
mydict = dict(thisdict)
print(mydict)

thisdict['color'] = 'red'

print(thisdict)
print(mydict)

# Nested dictionary

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily)
print(myfamily['child1'])

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily)

# The dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary:

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
