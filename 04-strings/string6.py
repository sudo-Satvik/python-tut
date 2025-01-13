# Escape sequences
# \' -> single quote
# \" -> double quote
# \\ -> backslash
# \n -> new line
# \t -> tab
# \r -> carriage return

print('Hello\rWorld')

# use case of carriage return 
import time
for i in range(4):
    print("\rLoading" + "." * i, end="")
    time.sleep(0.5)


# Raw strings: use raw strings (r"") to treat backslashes as literal characters (useful for file paths or regex).

path = r"C:\Users\Alice\Documents"
print(path)  # Output: C:\Users\Alice\Documents
