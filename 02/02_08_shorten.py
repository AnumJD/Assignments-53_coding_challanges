"""Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program."""

#Solution:

MAX_LENGTH = 3  # Set the maximum length

def shorten(lst):
    # Keep removing elements from the end until the list length is MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last item
        print("Removed:", removed_item)  # Print the removed item

# Example main function to get a list and call shorten
def main():
    # Get input from the user and create a list
    n = int(input("Enter the number of elements in the list: "))
    user_list = []

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    print("Original list:", user_list)

    # Call the shorten function
    shorten(user_list)

    # Display the list after shortening
    print("Shortened list:", user_list)

# Run the main function
main()
