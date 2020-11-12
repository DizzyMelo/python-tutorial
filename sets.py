# Set
# A set is a collection which is unordered and unindexed. In Python, sets are written with curly brackets.

thisset = {'apple', 'banana', 'cherry'}
print(thisset)

# Access Items
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

for x in thisset:
    print(x)

# Example
# Check if "banana" is present in the set:

print('banana' in thisset)

# Add Items
# To add one item to a set use the add() method.

# To add more than one item to a set use the update() method.

thisset.add('mango')
print(thisset)

thisset.update(['pineapple', 'orange', 'lime'])
print(thisset)

# Get the lenght of the set collection
print(len(thisset))

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# if the item doesnt exist, remove() will raise an error
thisset.remove('mango')
print(thisset)

# If the item doesnt exist, discard() will not raise an error
thisset.discard('banana')
print(thisset)

# You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

# The return value of the pop() method is the removed item.

thisset.pop()
print(thisset)

# Example
# The clear() method empties the set:
thisset.clear()
print(thisset)

thisset = {'banana', 'apple', 'cherry'}
print(thisset)

# Delete the set completely
del thisset

# Join Two Sets
# There are several ways to join two or more sets in Python.

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = {4, 5, 6}
set4.update(set3)
print(set4)

thisset = set(('banana', 'apple', 'cherry'))  # note the double rounded bracket
print(thisset)
print('--------------------------------------------')

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others
