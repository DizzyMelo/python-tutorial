# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:

# Example
# The try block will generate an exception, because x is not defined:

try:
    print('ola')
except NameError:
    print('An exception occured')
except:
    print('Another error')

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:

try:
    print('Hello World')
except NameError:
    print('An exception occured')
except:
    print('Another error')
else:
    print('Everything went OK')

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print('asdf')
except NameError:
    print('Name error occured')
finally:
    print('End of try')

# This can be useful to close objects and clean up resources:

# Example
# Try to open and write to a file that is not writable:

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    # f.close()
    print('close')

# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.

x = -1

# if x < 0:
#     raise Exception('No numbers below 0 allowed')


# The raise keyword is used to raise an exception.

# You can define what kind of error to raise, and the text to print to the user.

x = 'Hello'

if not type(x) is int:
    raise TypeError('It has to be a number')
