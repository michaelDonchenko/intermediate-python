import random

"""
    A generator in Python is a special type of function that allows
    you to create an iterator using the yield keyword.
    It provides a convenient way to iterate over a sequence of values without
    having to store the entire sequence in memory.
    Generators are particularly useful for working with large datasets or when
    you want to produce values lazily as they are needed.
"""


# A simple generator that mimics the built-in range() function:
def custom_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step


for num in custom_range(1, 10, 1):
    print(num)


# A generator that reads lines from a file and yields each line:
def read_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


for line in read_lines("./data.txt"):
    print(line)


# A generator that generates random numbers within a specified range:
def random_numbers(min_value, max_value, count):
    for _ in range(count):
        yield random.randint(min_value, max_value)


for num in random_numbers(1, 100, 5):
    print(num)
