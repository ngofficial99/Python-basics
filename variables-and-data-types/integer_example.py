# to declare a Integer variable we need to give the variable a name followed by = operator and provide it with an integer value

num1 = 100

num2 = 300

# we can print the vlaue by using the print command and call the variable name

print(num1);

#  we can also make operations by just calling the variable name 

num3 = num1 + num2

print(num3)


# We can also take user input and store it in a Varible

# Taking user input for the year they were born
birth_year = int(input("Please enter the year you were born: "))

# Importing the datetime module to get the current year
import datetime

# Getting the current year
current_year = datetime.datetime.now().year

# Calculating the age
age = current_year - birth_year

# Printing the age
print(f"You are {age} years old.")