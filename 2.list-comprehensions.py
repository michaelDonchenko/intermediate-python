"""
    The basic syntax of a list comprehension is as follows:
    new_list = [expression for item in iterable if condition]
    
    expression: The value you want to include in the new list, 
    derived from each item in the iterable.
    item: A variable that represents each individual item in the iterable.
    iterable: The source collection of items (e.g., a list, tuple, or range) 
    that you want to process.
    condition (optional): An optional filtering condition that determines 
    whether an item is included in the new list.
"""

# regular
squares = []
for x in range(10):
    squares.append(x**2)

# list comprehension
squares = [x**2 for x in range(10)]

# with condition filter
even_squares = [x**2 for x in range(10) if x % 2 == 0]

original_list = [1, 2, 3, 4, 5]
doubled_list = [x * 2 for x in original_list]

print(doubled_list)
