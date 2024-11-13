"""Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

Here's a sample run (user input is in blue):

Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']"""

#Solution
# Initialize an empty list to store the values
user_list = []

# Continuously prompt the user for input
while True:
    value = input("Enter a value: ")
    # Check if the input is empty
    if value == "":
        break
    # Add the input to the list
    user_list.append(value)

# Print the final list
print("Here's the list:", user_list)
