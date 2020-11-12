# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ['apple', 'banana', 'cherry']

for x in fruits:
    print(x)

# Loop through each letter of a string

for x in 'banana':
    print(x)

for x in fruits:
    print(x)
    if x == 'banana':
        break

for x in fruits:
    if x == 'banana':
        break
    print(x)

for x in fruits:
    if x == 'banana':
        continue
    print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):
    print(x)

# Change Default start value
for x in range(2, 6):
    print(x)

# Change the default incrementation value
for x in range(2, 30, 3):
    print(x)


# Using the else statement to execute a command in the end of the loop

for x in range(6):
    print(x)
else:
    print('The last index was reached')

# Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# Using the pass command to make and empty loop
for x in [0, 1, 2]:
    pass
