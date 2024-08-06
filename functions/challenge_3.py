# Suppose you just attended a University examination. The marks you obtained in various subjects are stored in a list like this:

# marks = [55, 64, 75, 80, 65]

# You want to find the average marks you obtained in the exam. And, based on the average marks you want to find your grade. The grading rule is like this:

# - You will get Grade A if the average marks is equal to or above 80
# - You will get Grade B if the average marks is equal to or above 60 and less than 80
# - You will get Grade C if the average marks is equal to or above 50 and less than 60
# - And if the average marks is less than 50, you will get Grade F

# solution
marks = [55, 64, 75, 80, 65]
def grade_calculator(m):
    total_marks = sum(marks)
    average = total_marks/len(marks)
    
    if average >=  80 :
        grade = "A"
    elif average >= 60 and average < 80:
        grade = "B"
    elif average >= 50 and average < 60:
        grade = "C"
    else:
        grade = "F"
    print("Your grade is: ",grade)

grade_calculator(marks)