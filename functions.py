# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.

# Creating a Function
# In Python a function is defined using the def keyword:

def my_function():
    print('this is my first python function')


# Calling a function
my_function()

# Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:


def my_function(fname):
    print(fname + ' this is the function name')


my_function('Daniel')


# Number of Arguments
# By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments,
# not more, and not less.

def my_function(fname, lname):
    print(fname, lname)


my_function('Daniel', 'Melo')

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:


def my_function(*args):
    print(args[2:])


my_function('Daniel', 1, 'Melo', 7.8)


def my_function(fname, lname):
    print(fname, lname)


my_function(lname='Daniel', fname='Melo')

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:


def my_function(**args):
    print(args['fname'], args['lname'])


my_function(fname='Daniel', lname='Melo')

# Default Parameter Value
# The following example shows how to use a default parameter value.

# If we call the function without argument, it uses the default value:


def my_function(country='Norway'):
    print(country)


my_function('EUA')
my_function('Brasil')
my_function('France')
my_function('Spain')
my_function()


def my_function(fruits):
    for x in fruits:
        print(x)


fruits = ['apple', 'banana', 'cherry']

my_function(fruits)
my_function(fruits)

# Return Values
# To let a function return a value, use the return statement:


def my_function(x):
    return x * 5


print(my_function(3))
print(my_function(5))
print(my_function(9))


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.

def my_function():
    pass


my_function()
print('-------------------------')


# Recursion
# Python also accepts function recursion, which means a defined function can call itself.

# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


tri_recursion(1)
