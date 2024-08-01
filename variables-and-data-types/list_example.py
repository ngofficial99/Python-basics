"""
List Example in Python

In Python, a list is a versatile data type that allows you to store an ordered collection of items. Lists are mutable, meaning their content can be changed after they are created. They can hold items of different data types, including other lists.

This script demonstrates various operations and methods related to lists. We'll explore:
1. Creating and accessing list elements.
2. Modifying lists (adding, removing, and changing elements).
3. Common list methods and operations.
4. Iterating over lists.
5. Nested lists.

Let's dive into some examples to understand how lists work and how they can be utilized in different scenarios.
"""
# To Create a list we will use a variable name followed by [] sqaure brackets and the elements of the list will be comma seperated.

# lets create a list of ToDo's

todo =["water the plants", "take out the laundry", "pay the electricity bill", "Work on Python github Repo"]

# now that we have our list created we can print the entire list by using print command
print(todo)

# Now if I want to print any specific element of the list I can call it using the Index
print("The first task is: ",todo[0])
print("The Second task is: " ,todo[1])
print("The Third task is: ",todo[2]) 
print("The Fourth task is: ",todo[3]) 


# Now if I want to add more elements or more tasks in our example how will we do It?
# we can make use of append
print("Append example :")
todo.append("Take Sylvie on walk")

print("The fifth task is: ", todo[4])

# Now lets say I am done with a particular Todo and I want to get rid of the same to delete an element we can make use of remove operations

todo.remove("water the plants")
print("Showing the remove operation: ")
print(todo)

# Now Lets say an urgent work came-up and we have to get it done before taking out the laundry, how will I alter the list and put a element before the first todo.
todo[0] = "Provide Blood sample for blood test"
print("ALter an element example: ")
print(todo[0])
 
# Now if I wanto to check how many items are there on the list we can do that using the len fucntion

print("Total number of tasks we need to perform today :", len(todo));

# Now if I want to check if a particular item is on the list or not we can to that using in operator

print("Is taking Sylvie for a walk on the list: ", "Take Sylvie on walk" in todo);

# If i want to iterate over the items on a list we can use the for loop for the same.
for task in todo:
    print("Tasks: ", task)
    
#  We can also create whats called a Nested Lists
# A nested list is a list that contains other lists as its elements. This allows you to create multi-dimensional data structures, such as matrices or tables.

# Lets create a list which will have countries and the list will have multiple lists in side based on continent these counrty belong to 

contries =[["India","Russia","China","Nepal"],["Scotland","Italy","Spain","Germany"],["USA","Canada"]]

# We can print all the countries
print("Learning Nested Lists")
print(contries)
# Now we can print the countries based on there continent 
print("Countries in Asia:",contries[0])
print("Countries is Europe:",contries[1])
print("Countries in North America:",contries[2])

# We can also print a specific element from the list inside a list
print("Biggest country in Asia is:",contries[0][2])