a = {
    "key" : "value",
    "name" : "Satvik",
    "marks" : 100,
    "notes" : [10, 20, 50]
}

print("Original Dictionary: ",a)

# Returns a list of (key,value)tuples
print(a.items())

# Returns a list containing dictionary's keys
print(a.keys())

# Updates the dictionary with supplied key-value pairs
a.update({"notes": True})
print(a)

# Returns the value of the specified keys (and value is returned)
print(a.get("marks"))