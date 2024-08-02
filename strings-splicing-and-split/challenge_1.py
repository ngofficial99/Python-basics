"""
Challenge 1: Username Validation

In this challenge, you will create a program that validates a username based on the following criteria:
1. The username should not be more than 12 characters.
2. The username should not contain any numbers.
3. The username should not contain any spaces.

Your task is to:
1. Take user input for the username.
2. Validate the username based on the above criteria.
3. Print whether the username is valid or not.

Solution:
1. Get the username input from the user.
2. Check the length of the username.
3. Check if the username contains any numbers.
4. Check if the username contains any spaces.
5. Print the validation result.
"""

# Take the user input
username = input("Enter your username")
# Check if there are no digits
check_number = username.find(" ")
# Check if it contains only alphabets
check_alphabet = username.isalpha()
if len(username) > 12 :
    print("Username should not be more than 12 characters")
elif not check_number == -1:
    print("There should be no spaces used in the username")
elif not check_alphabet == 1:
    print("User name should not contain any numbers")
else:
    print(f"Welcome {username}")



