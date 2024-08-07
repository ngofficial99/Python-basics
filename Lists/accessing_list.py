# we can access individual elements of a single dimensional list 

# A single dimensional list is a list where elements are listed one after the other 
#   Lets create a list from the multiples of 5 to 20 each element will be having a unique id called the index


multiple_of_five = [5,10,15,20]

# In this list the first element whos value is 5 will have the index 0, second will have 1 and so on. 

# Now if I want to access an individual element of the list that element can be identified using the index

num1 = multiple_of_five[0]

# in the above code i have stored the first element whos index is 0 and value is five in the variable num1

print(num1)


# Now lets understand Negative indexing 
# Negative indexing means accessing numbers from the last 
# Similar tto normal indexing where from go from first element to last element in negative indexing we have index from last element to the first element
# The index of the last element will be -1 then second last will by -2 and so on 

num2 = multiple_of_five[-1]
print(num2)
# In the above example we can see that we have printed the last element of the list using the negative index
# Negative indexing is useful in senarios where we dont know the length of the list and we need the last element of the list
# The last element of any list will always be -1

# Now lets understand how to access elements of a multi-dimensional list
# A multi-dimensional list is a list which contains another list that means there must be a list within a list

# Example
two_d_list = [[12,123,1234],"Hello",[555,666,777]]

# Now its confusing what if I want to access element 2 from the 3rd element.

# So if i want to access 12 which is the first element of the list which is also the first element of two_d_list we will use 2 [] the first [will contain the index of the primary list][second one will contain the value of the secondary list]

num3 = two_d_list[0][0]
print(num3)

#  So lets say if i want to access the value 555
num4 = two_d_list[2][0] 

print(num4)

# Lets make it more complicated make it a 3-d list 

three_d_list = [1,2,"num",[[12,123,1234],"ram",True]]

# How would we get the value 123 from the above list 

num5 = three_d_list[3][0][1]
print(num5)
