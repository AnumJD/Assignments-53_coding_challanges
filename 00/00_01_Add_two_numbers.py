"""Problem Statement: Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

Prompt the user to enter the first number.

Read the input and convert it to an integer.

Prompt the user to enter the second number.

Read the input and convert it to an integer.

Calculate the sum of the two numbers.
Print the total sum with an appropriate message."""
#We are using main() function here. It helps to keep the code organized.

#Solution 
def main():
    print("We are going to add two numbers!")
num1: str = input("Enter your first Number: ")
num1 : int = int(num1)
num2: str = input("Enter your second Number: ")
num2: int = int(num2)
sum : int = print (f"Sum of two numbers {num1} and {num2} is:  {num1+num2}")
if __name__ == '__main__': #This line checks whether the script is run directly (as opposed to being imported as a module in a script)
    #__name__ is a special built-in variable in Python. If the Script is run directly, __name__ is set to '__main__'. If it is imported, __name__ is set to module's name.
    main()
# if condition is true (i.e. if the script runs directly), main() is called, executing the code inside the function. 