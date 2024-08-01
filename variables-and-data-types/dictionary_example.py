"""
Dictionary Example in Python

In Python, a dictionary is a collection of key-value pairs. Each key is unique, and each key is associated with a value. Dictionaries are also known as hash maps or associative arrays in other programming languages. They are highly efficient for looking up values by their keys.

This script demonstrates various operations and methods related to dictionaries. We'll explore:
1. Creating and accessing dictionary elements.
2. Adding, modifying, and deleting key-value pairs.
3. Common dictionary methods and operations.
4. Iterating over dictionaries.
5. Nesting dictionaries.

Let's dive into some examples to understand how dictionaries work and how they can be utilized in different scenarios.
"""

# To create a dictionary we make use of curly brackets
myself = {
    "name": "Nishant",
    "Age": 25,
    "Profession": "Software Developer",
    "Degrees": ["BCA", "MCA", "PG in Cloud Computing"]
}


# Now that we have a Dictionary we can print it aswell
print(myself)

#  we can also access indicidual elements of a dictionary by access the key.

print("Employee name is",myself["name"])
print("Employee's qualifications are",myself["Degrees"])


#  Now we can also alter the dictionary so lets try to add another element
myself["height"] = 5.10
print(myself)
# we can also alter existing key value pair
myself["Profession"] = "Software engineer"
print(myself["Profession"])

#  we can also delete an element from the key value pair

del myself["height"]
print("updated person: ", myself)

#  we also have the propvision to only print the keys, only the values or both 

# only keys
print(myself.keys())

# only values
print(myself.values())

# noth keys and values
print(myself.items())