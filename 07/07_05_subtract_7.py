"""Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture."""

#Solution: 
def subtract_seven(num):
    """Subtract 7 from the given number."""
    return num - 7

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the subtract_seven function and store the result
    result = subtract_seven(num)
    
    # Print the result
    print(f"The result after subtracting 7 is: {result}")

# Run the main function
if __name__ == "__main__":
    main()
