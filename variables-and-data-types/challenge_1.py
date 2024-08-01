"""
Challenge 1: Employee Management System

In this challenge, you will create a small employee management system that involves various Python data structures. The system will allow you to:

1. Define employee information using dictionaries.
2. Store and manipulate employee data using lists and tuples.
3. Perform calculations using integers and floats.
4. Format and display information using strings.

Your tasks are as follows:

1. Define a dictionary with employee details.
2. Create a list of employee dictionaries.
3. Use a tuple to store a fixed set of job titles.
4. Calculate the average age of the employees.
5. Format and print employee information, including the calculated average age.

Solution:

1. Define the employee dictionary.
2. Create a list of employee dictionaries.
3. Define a tuple with job titles.
4. Calculate the average age.
5. Print the formatted information.
"""


# Lets start by defining the Employee dictionary

employees = {
    "employee_1": { 
        "name": "Hitesh",
        "age": 30,
        "salary": 75000.50,
        "email": "Hitesh@workemail.com",
        "position": "Frontend Developer"
    },
    "employee_2": { 
        "name": "Harry",
        "age": 28,
        "salary": 68000.75,
        "email": "harry@workemail.com",
        "position": "Backend Developer"
    },
    "employee_3": { 
        "name": "Philip",
        "age": 35,
        "salary": 80000.00,
        "email": "Philip@workemail.com",
        "position": "Fullstack Developer"
    } 
}


# Now lets create a list of the Employee dictionary

employee_list = [employees["employee_1"],employees["employee_2"],employees["employee_3"]]
# print(employee_list)

# Now lets create a tuple that is going to store job titles

job_titles = ("Frontend Developer","Backend Developer", "Fullsatck Developer")


# calculate the average age of the employees 

total_age = sum(employee["age"] for employee in employee_list)
average_age = total_age / 3
# print("Average age of all the employees is: ", average_age)


# Now lets print the reformatted data 
print("Employee details:")
for emp in employee_list :
    print(f"Name of the employee is: {emp['name']}" ) 
    print(f"Age of the employee is: {emp['age']}" )
    print(f"Salary of the employee is: {emp['salary']}" )
    print(f"Email of the employee is: {emp['email']}" )
    print(f"Position of the employee is: {emp['position']}" )
