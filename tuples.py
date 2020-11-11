# Tuple
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thistuple = ('banana', 'apple', 'cherry')
print(thistuple)
print(type(thistuple))

# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:

print(thistuple[1])

# Negative Indexing, -1 will retrieve the last index

print(thistuple[-1])

# Range of Indexes, first index inclusive, last index exclusive

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Negative Index Range
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# To change a value inside a tuple, convert the tuple to a list and then conver the list back to a tuple
x = list(thistuple)
x[1] = 'pineapple'
thistuple = tuple(x)
print(thistuple)


# Looping through a tuple
for x in thistuple:
    print(x)

# Check if item exists

if 'pinea' in thistuple:
    print('item exists')
else:
    print('item doesnt exist')

print(len(thistuple))

# Cant add a value to the tuple
# thistuple[7] = 'watermelon'
# print(thistuple)

# Create a tuple with one item
thistuple = ('apple',)  # this is a tuple
# thistuple = ('apple')   this is a string not a tuple
print(thistuple)

del thistuple
# print(thistuple) # this will raise an error once the tuple was deleted

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

thistuple = tuple(('apple', 'banana'))  # note the double round-bracket
print(thistuple)
