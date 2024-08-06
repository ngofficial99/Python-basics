# Challenge 1: Check Prime Number
# Description:
# Create a function that checks if a number is prime. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.


# Solution

def is_prime(number):
    """
    This function checks if a number is prime.
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
print(is_prime(11))  # Output: True
print(is_prime(15))  # Output: False
