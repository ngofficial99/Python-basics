# We have previously lernt about logical operators we can use them with if-else statements to check for multiple conditions in one step

# Lets say I want to create a login

user = input("enter your username: ")
password = input("enter your password: ")

# Now if both username and password mathches only then we will allow the login else we won't

if user=="admin" and password=="admin123":
    print("welcome admin")
else:
    print("Incorrect username or password")
    
# Similarly we can make use of OR operator which will check that if either of those conditions are true it will let use pass the condition

adhaar_card = True
pan_card = False

if adhaar_card==True or pan_card == True:
    print("you have the required document")
else:
    print("You dont have the required documents")