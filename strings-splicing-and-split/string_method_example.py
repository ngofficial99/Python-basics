"""
String Methods Example in Python

In this script, we will explore various string methods using Python. String methods allow you to manipulate and analyze text data in different ways. We will:

1. Get user input for name and phone number.
2. Use string methods to analyze and modify the input.
3. Print the results of these operations.

The following string methods will be demonstrated:
- len(): Get the length of the string.
- find(): Find the index of a substring.
- capitalize(): Capitalize the first character of the string.
- upper(): Convert the string to uppercase.
- lower(): Convert the string to lowercase.
- isdigit(): Check if the string consists of digits only.
- isalpha(): Check if the string consists of alphabetic characters only.
- count(): Count occurrences of a substring.
- replace(): Replace parts of the string with another substring.
"""

# Lets take some user input which we will manipulate

# name = input("Enter your name: ")

# phone_number = input("Enter your phone #: ")

# entering name andd phone number again and again is a task so i will just hard code a variable when you are using you can just uncomment and use the above input variables.

name = "Nishant Gupta"
phone_number = "7908110229"

# Now if I want to find the length of the name and phone number I can use len()
print("Length of name is:", len(name))
print(len(phone_number))

# We can store the values we are getting from the len function into a variable by 

length_of_name = len(name);

# Now if I want to find the first occurance of a particular character for that we will make use of find() method

song = "jenny of oldstone"

# Now in the following string lets try to find the first occurance of the letter 's'

print(song.find("s"))

# lets try to find the first occurance of space

print(song.find(" "))

# If I want to find from reverse order instead of find we will use rfind where R stands for Reverse.

print(song.rfind("o"))


#  Now if we want to capatalize the first element in a string we will use capitalize() fucntion
capital_song = song.capitalize();
print(capital_song)

# If you want to make the entire string Capital we will make use of upper() function

print(song.upper());

#  Similarly we can also make the entire string lower case using the lower() function

print(song.lower());

# Now if I want to check if the string only consists of numeric digits we will make use of isdigit() function

print("does the phone number variable contain only numiric digits: ", phone_number.isdigit())

# Now if I want to check if the string only consists of n alphabets we will make use of isalpha() function

print("Dose name variable only contain alphabets:" , name.isalpha()); 
# we will get false because we have a space in the name()

# Now if I want to check how many times a substring has been repeated we can make use of count() method

print(song.count("e"));

# Finally if I want to replace a Substing in a string we will make use of replace() function

we_need = "quick buck"

# now lets replace the space with a -

print(we_need.replace(" ", "-"))




