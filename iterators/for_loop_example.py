# This file demonstrates the use of a `for` loop to iterate over elements of a list. It shows how to access and print each element.

# Define a list of fruits
fruits = ["apple", "banana", "cherry", "date"]

# Using a for loop to iterate over each fruit in the list
print("Iterating over a list of fruits:")
for fruit in fruits:
    # Print the current fruit
    print(fruit)

# Example of using the for loop with the range function
print("\nUsing for loop with the range function:")
# Define a range of numbers from 1 to 5
for number in range(1, 6):
    # Print the current number
    print(number)

# Example of iterating over a dictionary
print("\nIterating over a dictionary:")
# Define a dictionary with fruits and their quantities
fruit_quantities = {
    "apple": 10,
    "banana": 5,
    "cherry": 7
}

# Iterate over the dictionary items (key-value pairs)
for fruit, quantity in fruit_quantities.items():
    # Print the fruit and its quantity
    print(f"{fruit}: {quantity}")

# Example of using a for loop with list comprehension
print("\nUsing list comprehension with a for loop:")
# Create a list of squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
# Print the list of squares
print(squares)

# Example of nested for loops
print("\nUsing nested for loops:")
# Define a 2D list (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate over each row in the matrix
for row in matrix:
    # Iterate over each item in the current row
    for item in row:
        # Print the item with a space, and keep printing on the same line
        print(item, end=' ')
    # Print a newline character after each row is printed
    print()
