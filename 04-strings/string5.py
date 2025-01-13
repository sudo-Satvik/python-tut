# String Formatting: Python supports several ways to format strings:

# 1: Using f-strings [python 3.6+]
name = "Satvik"
age = 21
print(f"My name is {name} and my age is {age}.")

# 2: Using format()
print("My name is {} and my age is {}".format(name, age))

# 3: Using % operator ~ an older way to format the strings
"""
%s: String (or any object with a string representation) 
%d: Integer
%f: Floating-point number
%x: Hexadecimal(lowercase)
%o: Octal
%e: Scientific notation (lowercase e)
"""
print("My name is %s and I am %d years old" % (name, age))