# nested_loops_example.py

# Define a 2D list (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate over the rows
for row in matrix:
    # Iterate over the columns in each row
    for item in row:
        print(item, end=' ')
    print()
