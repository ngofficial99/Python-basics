# nested_condition.py

# Initialize variables
a = 10
b = 20

# Outer if statement
if a > 5:
    print("a is greater than 5")
    
    # Nested if statement
    if b > 15:
        print("b is greater than 15")
        
        # Another level of nesting
        if a + b > 30:
            print("The sum of a and b is greater than 30")
        else:
            print("The sum of a and b is not greater than 30")
    else:
        print("b is not greater than 15")
else:
    print("a is not greater than 5")
