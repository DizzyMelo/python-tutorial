a = 50
b = 60
if a > b:
    print('a is greater than b')
else:
    print('b is greater than a')

print(bool("Hello"))
print(bool(15))
print(bool('a'))

x = "Hello"
y = 0

print(bool(x))
print(bool(y))

# False values
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# class return a boolean


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


# Function returns a boolean


def myFunction():
    return True


print(myFunction())

# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))
