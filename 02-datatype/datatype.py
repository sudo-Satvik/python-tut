# 1 Numeric datatype

# 1.1 Integer
x = -10
# print("Negative Integer:", x)
y = 10
# print("Positive Integer:", y)


#1.2 Float
z = 10.5
# print("Float:", z)

#1.3 Complex
a = 3 + 4j
# print("Complex:", a)
# print("Real:", a.real)
# print("Imaginary:", a.imag)


# 2 Sequence datatype

# 2.1 String(str)

name = "Satvik Sharma"
# print("String:", name)

# 2.2 List: Ordered, mutable collection of items.
rollNo = [101, 102, 103, 104]
# print("List:", rollNo)

# 2.3 Tuple: Ordered, immutable collection of items.
uniqueId = ("1f2e3d", "2f3e4d", "3f4e5d")
# print("Tuple:", uniqueId)


# 3 Mapping datatype

#3.1 Dictionary: Unordered, mutable collection of key-value pairs. Key must be unique, otherwise error
person = {
    "name": "Satvik Sharma",
    "age": 21,
    "isMale": True
}

print("Dictionary:", person)
print("Hello, I am", person['name'])


# 4 Set datatype

#4.1 set: Unordered, mutable collection of unique items.

fruits = {"apple", "apple", "banana", "cherry"}
print("Set:", fruits)


#4.2 frozenset: Unordered, immutable collection of unique items.
vegetables = frozenset(["cucumber", "tomato", "potato", "onion"])
print("Frozen Set: ", vegetables)


# 5 Boolean datatype

is_python_fun = True
is_js_boring = False


# 6 NoneType: Represents the absence of a value or a null value
weather_data_failed = None

