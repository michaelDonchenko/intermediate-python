from typing import List, Dict, Union

# lambda arguments: expression


def squared(x: int):
    return x**2


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(squared, numbers))

print("Squared numbers: %s" % squared_numbers)

people: list[tuple[str, int]] = [("Alice", 25), ("Bob", 30), ("Eve", 22)]
sorted_people = sorted(people, key=lambda person: person[1], reverse=True)

print("Sorted people: %s" % sorted_people)

Person = Dict[str, Union[str, int]]

people_list: List[Person] = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Eve", "age": 22},
]
oldest_person = max(people_list, key=lambda person: person["age"])

print("Oldest person: %s" % oldest_person)
