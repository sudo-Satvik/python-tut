# List methods

l1 = [1,8,7,2,21,15]
print("Original List: ", l1)

# method-1: sort()
l1.sort()
print("Sorted List: ", l1)

# method-2: reverse()
l1.reverse()
print("Reverse List: ", l1)

# method-3: append(element) ~ adds at end of the list
l1.append(100_000)
print(l1)

# method-3: insert(index, element) 
l1.insert(3, False)
print(l1)

# method-4: pop(index) ~ will delete element at index 2 and return its value
print(l1.pop(1))
print(l1)

# method-5: remove(element) ~ will remove element from the list
l1.remove(21)
print(l1)