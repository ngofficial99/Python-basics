# Challenge 1: FizzBuzz
# Description:

# The FizzBuzz problem is a classic exercise used to teach looping and conditional logic. The task is to print numbers from 1 to 100, but with the following rules:

# Print "Fizz" for numbers divisible by 3.
# Print "Buzz" for numbers divisible by 5.
# Print "FizzBuzz" for numbers divisible by both 3 and 5.
# Print the number itself if it is not divisible by 3 or 5.
# Challenge:

# Create a Python script that uses a for loop to implement the FizzBuzz logic and prints the appropriate output for each number from 1 to 100.


# Solution:
    
for i in range(1,101):
    if (i%3 ==0 ):
        print("Fizz")
    elif(i%5 == 0):
        print("Buzz")
    elif(i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
    else:
        print(i)
    