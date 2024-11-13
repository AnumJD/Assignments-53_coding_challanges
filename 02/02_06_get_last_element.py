"""Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length."""
#Solution
def get_last_element(lst):
    # Print the last element of the list
    print("Last element:", lst[-1])

# Prompting user for input to create the list
n = int(input("Enter the number of elements in the list: "))
user_list = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

# Display the list
print("Your list:", user_list)

# Call the function to print the last element
get_last_element(user_list)
