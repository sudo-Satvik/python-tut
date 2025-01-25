# A Python dictionary is a data structure that stores the value in key: value pairs. 
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.

a = {
    "key" : "value",
    "name" : "Satvik",
    "marks" : 100,
    "notes" : [10, 20, 50]
}

print(a["key"])
print(a["name"])
print(a["marks"])
print(a["notes"])


# Property of mutable
a["marks"] = 150
print(a)
