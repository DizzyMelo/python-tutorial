# Python Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class
# To create a class, use the keyword class:

class MyClass:
    x = 5

# Create Object
# Now we can use the class named MyClass to create objects:

# Example
# Create an object named p1, and print the value of x:


p1 = MyClass()
print(p1.x)


# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello! My name is {}!'.format(self.name))


p1 = Person('Daniel', 26)
p2 = Person('Kaynara', 23)

p1.greet()
print(p1.name, p1.age)
print(p2.name, p2.age)

# Note: The __init__() function is called automatically every time the class is being used to create a new object.
# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It doesnt necesserally needs to be the name self, it could be whatever name

# Modify Object Properties
# You can modify properties on objects like this:

p1.age = 50
print(p1.age)

# Delete Object Properties
# You can delete properties on objects by using the del keyword:

del p1.age

# Delete Objects
# You can delete objects by using the del keyword:

del p1

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content,
# put in the pass statement to avoid getting an error.


class Person:
    pass
