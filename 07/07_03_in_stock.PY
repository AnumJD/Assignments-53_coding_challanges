"""Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

Prompt the user to enter a fruit ("Enter a fruit: ")

Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

Here's two sample runs of the program (user input in bold italics):

Enter a fruit: pear

This fruit is in stock! Here is how many:

1000

Enter a fruit: lychee

This fruit is not in stock."""

#Solution: 

# Function to return the number of fruits in stock
def num_in_stock(fruit):
    # Sample inventory dictionary
    inventory = {
        "apple": 50,
        "banana": 30,
        "pear": 1000,
        "orange": 200,
        "grape": 0,
    }
    
    # Return the stock count for the requested fruit, or 0 if not found
    return inventory.get(fruit.lower(), 0)

# Main function to interact with the user
def main():
    fruit = input("Enter a fruit: ").lower()  # Prompt the user for a fruit (convert to lowercase)
    
    # Call num_in_stock to get the quantity in stock
    stock_count = num_in_stock(fruit)
    
    # Check if the fruit is in stock and print the appropriate message
    if stock_count > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock_count)
    else:
        print("This fruit is not in stock.")

# Run the main function
if __name__ == "__main__":
    main()
