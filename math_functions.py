# Python Math
# Python has a set of built-in math functions, including an extensive math module, that allows you to
# perform mathematical tasks on numbers.

# Built-in Math Functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable:
import math


x = (5, 10, 3)
y = [5, 10, 3]

print(min(x))
print(max(x))

print(min(y))
print(max(y))

# The abs() function returns the absolute (positive) value of the specified number:

x = abs(-7.45)

print(x)

# The pow(x, y) function returns the value of x to the power of y (xy).

x = pow(4, 3)

print(x)

# The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.

# To use it, you must import the math module:

# When you have imported the math module, you can start using methods and constants of the module.

# The math.sqrt() method for example, returns the square root of a number:

x = math.sqrt(64)

# The math.ceil() method rounds a number upwards to its nearest integer, and
# the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

x = math.ceil(64.8)
y = math.floor(64.8)
print(x)
print(y)

# The math.pi constant, returns the value of PI (3.14...):

x = math.pi
print(round(x, 2))
