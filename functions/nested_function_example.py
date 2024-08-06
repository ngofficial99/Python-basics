# nested_function_example.py

# Example of a nested function
def outer_function(name):
    """
    This function contains a nested function that greets the user.
    """
    def inner_function():
        """
        This nested function prints a personalized greeting message.
        """
        print(f"Hello, {name}! This is an example of nested functions.")
    
    # Call the nested function
    inner_function()

# Call the outer function
outer_function("Nishant")

# Example of a nested function with return values
def multiply_by_factor(factor):
    """
    This function contains a nested function that multiplies a number by a given factor.
    """
    def multiplier(number):
        """
        This nested function multiplies the given number by the outer function's factor.
        """
        return number * factor
    
    return multiplier

# Create a multiplier function for factor 3
times_three = multiply_by_factor(3)

# Use the multiplier function
result = times_three(5)
print(f"5 multiplied by 3 is: {result}")
