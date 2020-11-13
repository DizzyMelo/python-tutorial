# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.
# x = lambda a : a + 10
def x(a): return a + 10


print(x(5))

# x = lambda a, b: a * b


def x(a, b): return a * b


print(x(4, 50))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# Use that function definition to make a function that always doubles the number you send in:


def my_function(n):
    return lambda a, b: a * n - b


mydoubler = my_function(2)
mytripler = my_function(3)

print(mydoubler(11, 2))
print(mytripler(11, 2))
