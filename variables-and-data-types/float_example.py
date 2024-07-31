# A float (short for "floating-point number") is a numerical data type used in Python to represent real numbers that include a fractional part. Floats are used when more precision is needed than what integers can provide, such as in scientific calculations, measurements, and financial applications.

# To create a folat variable the procedure is very similar to creating a Integer variable except we have to mention a number with the decimal point

pi = 3.75

print("The value of Pi is:", pi)

# Similarly we can take the user input for Float aswell and perform calculations

# Lets try to find the radius of a circle 

radius = float(input("Enter the Radius of the Circle in CM: "))

area = pi * (radius * radius)

print("The Area of the Circle is:", area, "CM sqare")