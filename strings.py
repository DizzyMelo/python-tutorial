
# multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# Single quote assignment
b = 'Hello'

# double quote assignment
c = "World"

print(a)
print(b)
print(c)

# Strings and Arrays
# Get the character at position 1 (remember that the first character has the position 0):

a = 'Hello World'
print(a[0])

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# The last number not included

b = 'Hello world'
print(b[2:7])

# String Length
# To get the length of a string, use the len() function.

a = 'Hello world'
print(len(a))

# String methods

# strip() - removes whitespaces from the beginning and the end a.strip()
# lower() - puts every character to lower case a.lower()
# upper() - puts every character to upper case a.upper()
# replace() - replace characters a.replace('h', 'w')
# split() - breaks the string into an array based on a character a.split(' ')

# Check String
# To check if a certain phrase or character is present in a string, we can use the keywords in or not in.

txt = "The rain in Spain stays mainly in the plain"
print("ain" in txt)

txt = "The rain in Spain stays mainly in the plain"
print("ain" not in txt)

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

a = "Hello"
b = "World"
c = a + ' ' + b
print(c)

# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

name = 'Daniel'
age = 26
txt = "My name is {}, I am {}"
price = 45
print(txt.format(name, age))

# Using indexes to order the parameters

name = 'Daniel'
age = 26
txt = "My name is {1}, I am {2} and I want this shoe that costs {0}"
price = 45
print(txt.format(name, age, price))

txt = "I am a \"Viking\""
print(txt)

strOne = str('a')
strTwo = 'a'

print(strOne == strTwo)
print(strOne is strTwo)

'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''
