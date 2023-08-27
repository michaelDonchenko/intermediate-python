# Creating a set
fruits = {"apple", "banana", "orange", "apple"}  # Duplicate "apple" is ignored

# Adding elements to a set
fruits.add("grape")

# Removing elements from a set
fruits.remove("banana")  # Raises an error if element is not found
fruits.discard("watermelon")  # Safely removes element even if not found

# Membership test
print("apple" in fruits)  # True
print("pear" in fruits)  # False

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))  # Union
print(set1.intersection(set2))  # Intersection
print(set1.difference(set2))  # Difference
print(set1.symmetric_difference(set2))  # Symmetric difference

# Iterating through a set
for fruit in fruits:
    pass
