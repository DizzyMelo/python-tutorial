g = 'Daniel'

# x, y, z = 'l', 't', 'v'
# x = y = z = 'l', 't', 'v'
x = y = z = 'l'


def myFunction():
    global g
    g = 'Hugh'
    print('My name is ' + g)


myFunction()
print(type(g))
print(x)
print(y)
print(z)
