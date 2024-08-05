# while` Loop:
#    - Repeatedly executes a block of code as long as a specified condition is true.
#    - Useful when the number of iterations is not known beforehand.


# Example 1: Basic While Loop
print("Basic While Loop Example:")
# Initialize a counter
count = 0

# Execute the loop while the counter is less than 5
while count < 5:
    # Print the current count value
    print("Count:", count)
    # Increment the counter
    count += 1

# Example 2: While Loop with User Input
print("\nWhile Loop with User Input:")
# Initialize the user input variable
user_input = ""

# Continue asking the user for input until they enter 'exit'
while user_input.lower() != 'exit':
    # Prompt the user for input
    user_input = input("Enter 'exit' to stop the loop: ")
    # Print a message if the user input is not 'exit'
    if user_input.lower() != 'exit':
        print(f"You entered: {user_input}")

# Example 3: While Loop with Break Statement
print("\nWhile Loop with Break Statement:")
# Initialize a counter
number = 0

# Execute the loop
while True:
    # Print the current number value
    print("Number:", number)
    # Increment the number
    number += 1
    # Exit the loop if the number is 5
    if number == 5:
        break

# Example 4: While Loop with Continue Statement
print("\nWhile Loop with Continue Statement:")
# Initialize a counter
num = 0

# Execute the loop while num is less than 10
while num < 100:
    # Increment the counter
    num += 1
    # Skip the rest of the loop if num is even
    if num % 2 == 0:
        continue
    # Print the current num value if it is odd
    print("Odd number:", num)

# Example 5: While Loop with Else Clause
print("\nWhile Loop with Else Clause:")
# Initialize a counter
counter = 0

# Execute the loop while the counter is less than 3
while counter < 3:
    # Print the current counter value
    print("Counter:", counter)
    # Increment the counter
    counter += 1
else:
    # This block executes after the while loop completes
    print("Loop completed successfully.")
