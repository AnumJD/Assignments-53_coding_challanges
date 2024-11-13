"""Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

Here's a sample run (user input is in blue):

Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12"""

#Solution:
def print_divisors(num):
    """Print all divisors of the given number."""
    print(f"Here are the divisors of {num}:")
    for i in range(1, num + 1):  # Loop through all numbers from 1 to num
        if num % i == 0:  # Check if i is a divisor of num
            print(i, end=" ")  # Print the divisor followed by a space
    print()  # Print a newline for better formatting

def main():
    user_input = int(input("Enter a number: "))  # Prompt the user for input
    print_divisors(user_input)  # Call the function to print divisors

# Run the main function
if __name__ == "__main__":
    main()
