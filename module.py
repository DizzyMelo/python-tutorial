# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.

# The as reserved word creates an allias for the module name

# from mymodules import person1
import platform
import mymodules as mx

mx.greeting()

print(mx.person1['age'])

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

print(platform.system())

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

print(dir(platform))
print(dir(mx))

# Import From Module
# You can choose to import only parts from a module, by using the from keyword.
