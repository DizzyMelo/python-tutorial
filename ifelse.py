# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

a = 44
b = 100
if a > b:
    #  Remember that python relies on identation
    print('a is greater than b')
elif a == b:
    print('a is equals to b')
else:
    print('b is greater than a')

if b > a:
    print('b is greater than a')

a = 2
b = 330
print('1') if a > b else print('2')

a = 3
b = 4
print('A') if a > b else print('==') if a == b else print('B')

# The and logical operator

a = 220
b = 33
c = 500
if a > b and c > a:
    print('both conditions are true')

if a > b or a > c:
    print('at least one of the conditions are true')

# Nested If
a = 41
if a > 10:
    print('Above 10')
    if a > 20:
        print('Above 20')
        if a > 40:
            print('Above 40')
        else:
            print('But not above 40')
    else:
        print('But not above 20')

# Pass statement can be used if for some reason you need an empty if statement, which by default will raise an error
if 10 > 5:
    pass
