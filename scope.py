# Python Scope

# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myFunc():
    x = 300

    def innerfunction():
        print(x)
    innerfunction()


myFunc()

x = 300


def myFunc():
    x = 200
    print(x)


myFunc()
print(x)


def myFunc():
    global y
    y = 50


myFunc()
print(y)


def myFunc():
    global x
    x = 500


myFunc()

print(x)
