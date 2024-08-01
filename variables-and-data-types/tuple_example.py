"""
Tuple Example in Python

In Python, a tuple is an immutable sequence of items. Tuples are similar to lists, but unlike lists, tuples cannot be changed after they are created (i.e., they are immutable). Tuples are typically used to store collections of heterogeneous data, meaning they can contain elements of different data types.

This script demonstrates various operations and methods related to tuples. We'll explore:
1. Creating and accessing tuple elements.
2. Understanding the immutability of tuples.
3. Common tuple operations and methods.
4. Iterating over tuples.
5. Using tuples for multiple assignments.

Let's dive into some examples to understand how tuples work and how they can be utilized in different scenarios.
"""

# The procedure to create a Tuple is very similar as of creating a List

days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# The reason I have chosen days_of_week because it will never change

# To print a Tuple we can use the same method as list
print(days_of_week)

# Just like Lists we can also call individual elements from Tuples
print("First day of week is:", days_of_week[0])
print("Weekend starts at:",days_of_week[5])

# But unlink list we cannot change any element of a tuple hence it is used in cases where we want the data structure to be immutable
# lets attempt to change the element and we all know that this is going to throw an error 
try:
    days_of_week[0]="NishantDay"
except TypeError as e:
    print("Error:",e);

# How ever we can perform operations such as finding the length of my Tuple 
print("Total number of days in a week are:",len(days_of_week))

#  We can also check if an element is present in a Tuple
print("Sunday is a part of week:","Sunday" in days_of_week);

# To iterate over elements we can use a for loop

for day in days_of_week:
    print("days in week are",day);
    
    
# Finally we can create multiple assignments with tuples 
Employee_001 = ("Nishant", "Fullstack Developer", 25, )
name , profession, age = Employee_001
#  Now we can print the key-value pair

print(f"Employee name : {name}, He is {age} years old, and he works as a {profession}")

