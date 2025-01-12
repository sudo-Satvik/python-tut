# Local Scope
# The local scope refers to the scope of variables defined within a function. 
# These variables are accessible only within the function where they are defined.

def greet():
    name = "Satvik"
    print("Hello, ", name)

# name is not accessible here because of local scope


# Enclosing or un-Local scoping
# The enclosing scope refers to variables that are in the scope of a function that encloses another function 
# (e.g., a function inside another function).

def outer():
    outer_var = "I am outer one"
    def inner():
        return outer_var;   # you can see the outer_var is accessible here too
    inner()




# Global Scope
# The global scope refers to variables that are defined at the top level of a script, outside of any functions or classes.
# Accessible from anywhere in the script

global_var = "I am global"  # Global variable

def my_function():
    print(global_var)  # Accessing global variable inside a function

my_function()


# Built-in Scope
# The built-in scope refers to the names that are available in every Python script, such as print(), len(), and other built-in functions 
# and exceptions. These names are part of the Python standard library and are accessible throughout your code.

print(len("Hello"))  # 'len' is a built-in function


"""
LEGB Rule
Python follows the LEGB rule (Local, Enclosing, Global, Built-in) when resolving variable names. This is the order in which Python searches for a variable:

Local: First, Python looks for the variable in the local scope (inside the function).
Enclosing: If it’s not found, Python checks the enclosing function's scope.
Global: If it’s still not found, Python looks in the global scope (top-level variables).
Built-in: Finally, Python checks the built-in scope.

"""