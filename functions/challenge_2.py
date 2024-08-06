# Description:
# Create a function that calculates the factorial of a number using recursion. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.

def factorial(n):
    """
    This function calculates the factorial of a number using recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120
print(factorial(7))  # Output: 5040

    