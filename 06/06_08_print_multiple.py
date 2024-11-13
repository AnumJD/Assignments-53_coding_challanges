"""Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

Here's a sample run of the program (user input is in blue):

Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!"""
#Solution:
def print_multiple(message, repeats):
    """Prints the message the specified number of times."""
    for _ in range(repeats):  # Loop to print the message 'repeats' times
        print(message, end=" ")  # Print the message with a space after each

def main():
    message = input("Please type a message: ")  # Prompt for the message
    repeats = int(input("Enter a number of times to repeat your message: "))  # Prompt for repeats
    print_multiple(message, repeats)  # Call the function with the user inputs

# Run the main function
if __name__ == "__main__":
    main()
