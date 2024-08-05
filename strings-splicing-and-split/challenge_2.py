# challenge2.py

"""
Challenge 2: Email Slicer

In this challenge, you will create a program that slices an email address to extract the username and domain. The program will:
1. Take user input for an email address.
2. Slice the email address to get the username (part before the '@') and the domain (part after the '@').
3. Print the username and domain.

Solution:
1. Get the email address input from the user.
2. Find the index of the '@' symbol.
3. Slice the email address to extract the username and domain.
4. Print the username and domain.
"""

# Get the email address input from the user
email = input("Enter your email: ")

# Slice the email address to get the username and domain
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

# Print the username and domain
print(f"Your username is {username} and domain is {domain}")
