# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

x = 5
# list Sequence type
x = ['a', 'b', 'c', 'd']

# tuple Sequence type
x = ('a', 'b', 'c', 'd')

# list Sequence type
x = range(6)

# Dictionary Mapping type
x = {'name': 'Daniel', 'age': 26}

# Set Set type
x = {'a', 'b', 'c', 'd'}

# Frozenset Set type
x = frozenset({'a', 'b', 'c', 'd'})

# Bytes Bynary type
x = b"Hello"

# Bytearray Bynary type
x = bytearray(5)

# Memoryview Bynaty type
x = memoryview(bytes(5))

# Boolean
x = True

x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))

print(type(x))
print(x)
