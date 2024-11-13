"""Fill out the function count_even(lst) which

first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

and then prints the number of even numbers in the list.

If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!"""

#Solution:
def count_even(lst):
    # Prompt the user for integers until they press enter
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Check for empty input
            break  # Exit the loop if the user presses enter
        try:
            num = int(user_input)  # Convert input to an integer
            lst.append(num)  # Add the number to the list
        except ValueError:
            print("That's not a valid integer. Please try again.")  # Handle invalid input

    # Count the even numbers in the list
    even_count = sum(1 for number in lst if number % 2 == 0)
    
    # Print the count of even numbers
    print(f"The number of even numbers is: {even_count}")

# Example usage
numbers = []  # Create an empty list to hold the integers
count_even(numbers)
