"""Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time."""

#SOLUTION

def get_first_element(lst):
    # Print the first element of the list
    print("First element:", lst[0])

# Prompting user for input to create the list
n = int(input("Enter the number of elements in the list: "))
user_list = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

# Display the list
print("Your list:", user_list)

# Call the function to print the first element
get_first_element(user_list)
