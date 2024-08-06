# functions_example.py

# Function without arguments
def greet():
    """
    This function prints a greeting message.
    """
    print("Hello! Welcome to the world of Python functions.")

# Call the function
greet()

# Function with arguments
def greet_user(name):
    """
    This function takes a name as an argument and prints a personalized greeting message.
    """
    print(f"Hello, {name}! Welcome to the world of Python functions.")

# Call the function with an argument
greet_user("Nishant")

# Function with multiple arguments
def add_numbers(a, b):
    """
    This function takes two arguments and returns their sum.
    """
    return a + b

# Call the function with multiple arguments
result = add_numbers(5, 3)
print(f"The sum of 5 and 3 is: {result}")

# Function with default arguments
def greet_user_default(name="Guest"):
    """
    This function takes an optional name argument and prints a personalized greeting message. If no name is provided, it uses "Guest" as the default.
    """
    print(f"Hello, {name}! Welcome to the world of Python functions.")

# Call the function with and without an argument
greet_user_default("Nishant")
greet_user_default()
