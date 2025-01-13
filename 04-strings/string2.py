# Accessing characters in the string

# Strings are INDEXED and SLICED

# Indexing: Access individual character using their indices (starting at 0)
s = "Satvik"
# print(s[2])
# print(s[3])

# Slicing: Extracts a substring using [start:end:step]
slicing = "hello_world"
print(slicing[0:3])
print(slicing[0:3:1])
print(slicing[0:3:2])
print(slicing[::3])

# Using the concept of slicing, we can reverse the string in a line

print(slicing[::-1])