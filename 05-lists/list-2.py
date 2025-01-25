# List Indexing==============================

arr = [1, 2, 3]

print(arr[0])      # 1
print(arr[1])      # 2
print(arr[2])      # 3


# List Slicing
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr2[0:3])
print(arr2[::-1])



# Checking if list is mutable(able to change) or immutable(unable to change)

arr2[1] = "Stars"
print(arr2)

arr2 = arr
print(arr2)

# This means Python lists are mutable. You can change their contents after they are created.