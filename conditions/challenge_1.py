# Create a Python program that asks the user to input the current temperature in Celsius. The program should then determine if the temperature is cold, warm, or hot based on the following conditions:

# If the temperature is below 10°C, print "It's cold outside."
# If the temperature is between 10°C and 25°C (inclusive), print "It's warm outside."
# If the temperature is above 25°C, print "It's hot outside."


# Solution:

# Challenge 1: Temperature Check

# Get the current temperature from the user
temperature = float(input("Enter the current temperature in Celsius: "))

# Determine if the temperature is cold, warm, or hot
if temperature < 10:
    print("It's cold outside.")
elif 10 <= temperature <= 25:
    print("It's warm outside.")
else:
    print("It's hot outside.")
