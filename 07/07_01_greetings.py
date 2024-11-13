"""We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

Here's a sample run of the program (user input in bold italics):

What's your name? Sophia

Greetings Sophia!"""

#Solution:
def greet(name):
    """Prints a greeting message with the given name."""
    print(f"Greetings {name}!")

def main():
    # Get the user's name
    name = input("What's your name? ")
    
    # Call the greet function with the user's name
    greet(name)

# Run the main function
if __name__ == "__main__":
    main()
