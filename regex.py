# Python RegEx
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:
import re

txt = 'The rain in Spain'

# Search the string to see if it starts with "The" and ends with "Spain":

x = re.search('^The.*Spain$', txt)
if x:
    print('Match!')
else:
    print('No match')


# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:

# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string


# Metacharacters
# Metacharacters are characters with a special meaning:

# Character	Description	Example
# []	A set of characters	"[a-m]"
x = re.findall('[a-m]', txt)
print(x)
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# Find all digit characters:
txt2 = "That will be 59 dollars"
x = re.findall('\d', txt2)
print(x)
# .	Any character (except newline character)	"he..o"
x = re.findall('S...n', txt)
print(x)
# ^	Starts with	"^hello"
txt = 'hello hello bye world'
x = re.findall('^hello', txt)
print(x)
# $	Ends with	"world$"
x = re.findall('world$', txt)
print(x)
# *	Zero or more occurrences	"aix*"
x = re.findall('hell*', txt)
y = re.search('hell*', txt)
print(x)
print(y)
# +	One or more occurrences	"aix+"
x = re.findall('hell+', txt)
y = re.search('hell+', txt)
print(x)
print(y)
# {}	Exactly the specified number of occurrences	"al{2}"
# #Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall('el{2}', txt)
print(x)
# |	Either or	"falls|stays"
x = re.findall('hello|bye', txt)
print(x)
# ()	Capture and group

txt = 'The rain in 78 Spain'
# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# Character	Description	Example
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
x = re.findall('\AThe', txt)
print(x)
# \b	Returns a match where the specified characters are at the beginning or at the end of a word

# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"
x = re.findall(r'\brai', txt)
print(x)
#
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"

x = re.findall(r'\Bain', txt)
print(x)

#
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"

x = re.findall(r'\d', txt)
print(x)

# \D	Returns a match where the string DOES NOT contain digits	"\D"

x = re.findall('\D', txt)
print(x)

# \s	Returns a match where the string contains a white space character	"\s"

x = re.findall(r'\s', txt)
print(x)

# \S	Returns a match where the string DOES NOT contain a white space character	"\S"

x = re.findall(r'\S', txt)
y = re.search(r'\S', txt)
print(x)
# print(y)

# \w	Returns a match where the string contains any word characters
# (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"

x = re.findall(r'\w', txt)
print(x)

# \W	Returns a match where the string DOES NOT contain any word characters	"\W"

x = re.findall(r'\W', txt)
print(x)

# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

x = re.findall(r'Spain\Z', txt)
print(x)

# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:

# Set	Description
# [arn]	Returns a match where one of the specified characters (a, r, or n) are present
x = re.findall('[arn]', txt)
print(x)
# [a-n]	Returns a match for any lower case character, alphabetically between a and n

x = re.findall('[a-t]', txt)
# x = re.findall('[a-tA-T]', txt)
print(x)

# [^arn]	Returns a match for any character EXCEPT a, r, and n

x = re.findall('[^arn]', txt)
print(x)

# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present

x = re.findall('[6789]', txt)
print(x)

# [0-9]	Returns a match for any digit between 0 and 9

x = re.findall('[0-9]', txt)
print(x)

# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59

x = re.findall('[0-8][0-9]', txt)
print(x)

# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case

# x = re.findall('[^a-zA-Z]', txt) - This will check the characters which are not inside the interval specified
x = re.findall('[a-zA-Z]', txt)
print(x)

# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

txt = 'The rain in Spain'

# A list will be returned with the matches
x = re.findall('ai', txt)
print(x)

# When there is no match, an empty list will be returned
x = re.findall('Portugal', txt)
print(x)

# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.

# If there is more than one match, only the first occurrence of the match will be returned:

# Example
# Search for the first white-space character in the string:
x = re.search(r'\s', txt)
print('The first white space is located at index', x.start())

# Example
# Make a search that returns no match:

x = re.search('Portugal', txt)
print(x)

# The split() Function
# The split() function returns a list where the string has been split at each match:

x = re.split(r'\s', txt)
print(x)

# You can control the number of occurrences by specifying the maxsplit parameter:

x = re.split(r'\s', txt, 2)
print(x)

# Join a list of string separated by an empty space
print(' '.join(x))

# The sub() Function
# The sub() function replaces the matches with the text of your choice:

# Example
# Replace every white-space character with the number 9:

x = re.sub('\s', '9', txt)
print(x)

# You can control the number of replacements by specifying the count parameter:

x = re.sub('\s', '9', txt, 2)
print(x)


# Match Object
# A Match Object is an object containing information about the search and the result.

# Note: If there is no match, the value None will be returned, instead of the Match Object.

# Example
# Do a search that will return a Match Object:

# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
# .start() returns the first index in the span

x = re.search(r'\bS\w+', txt)
print(x)

print(x.span())
print(x.string)
print(x.group())
