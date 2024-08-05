# Challenge 2: Pyramid Pattern
# Description:

# The pyramid pattern challenge involves printing a right-angled triangle of asterisks. The number of rows in the triangle should be specified by the user.

# Challenge:

# Write a Python script that uses nested for loops to print a pyramid pattern. The number of rows should be taken as input from the user. Each row should contain a number of asterisks (*) equal to the row number.

# Solution
 
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i)+ "*" * (2 * i - 1))