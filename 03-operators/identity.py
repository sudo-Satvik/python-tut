# Identity operators are used to compare the memory location of two objects.

# is	            Returns True if both variables refer to the same object
# is not	        Returns True if both variables refer to different objects

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)

print(a is not b)
print(a is not c) 
