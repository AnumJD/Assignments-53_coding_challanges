#Problem Statement: Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
#Solution
def main():
    num1:float = float (input("Enter first number: "))
    num2:float = float (input("Enter second number: "))
    result = num1//num2
    reminder = num1%num2
    print(f"Division of two number is: {result} and reminder is: {reminder}")
if __name__=="__main__":
    main()