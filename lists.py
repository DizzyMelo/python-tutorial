thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

# print the first item
print(thislist[0])

# print the last item
print(thislist[-1])

# print item inside the interval, last index not included
print(thislist[2:5])

# print items from the beginning to the fourth position
print(thislist[:4])

# print from the third position (index 2) to the end of the list
print(thislist[2:])

# Negative intervals from item -4 (included) to item -1 (excluded)
print(thislist[-4:-1])

# Change item value

thislist[1] = 'blackcurrant'
print(thislist)

# Loop through a list

for x in thislist:
    print(x)

# List Comprehension

# Example without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(fruits)
print(newlist)

# Example with List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# 1 - declare variable
# 2 - for in loop
# 3 - condition

newlist = [x for x in fruits if "a" in x]

print(fruits)
print(newlist)

fruit = 'banana'

if fruit in thislist:
    print('There is ' + fruit + ' in the list')
else:
    print('There is not ' + fruit + ' inside the list')

print('The size of the list is {}'.format(len(thislist)))


# Append one item to the end of the list
thislist.append('pineapple')
print(thislist)

# Inserts one item in the specified position
thislist.insert(1, 'strawberry')
print(thislist)

# Removes specified item
thislist.remove('apple')
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop(4)
print(thislist)

# Deletes specified index

del thislist[0]
print(thislist)

# Deletes the list completly, not all the items, but the list itself

del thislist

# The method clear removes all the items inside the list
thislist = ["apple", "banana", "cherry"]
# thislist.clear()
print(thislist)

# Copy list using the copy() method
mylist = thislist.copy()
print(mylist)

# Copy list using the built-in method list()
newlist = list(thislist)
print(newlist)

# Join two lists

superlist = mylist + newlist
print(superlist)

# It is possible to join two lists using a for loop and appending each item (not recomended).
# Or using the extended() method, this method alters the list in which the method is used
mylist.extend(newlist)
print(mylist)

# The list constructor

# remember the double round-brackets
thislist = list(('banana', 'apple', 'mango'))
newlist = [x for x in thislist if 'n' in x]
print(thislist)
print(newlist)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
