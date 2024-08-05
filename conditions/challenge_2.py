# Create a Python program that takes a student's score as input and prints the corresponding grade based on the following criteria:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

# Solution

# Challenge 2: Grade Calculator

# Get the student's score from the user
score = float(input("Enter the student's score: "))

# Determine the grade based on the score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print the grade
print(f"The student's grade is: {grade}")
