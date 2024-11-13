"""Ask the user for a number and print its square (the product of the number times itself)."""
#Solution
def main():
    print("Type the number to see its sqaure")
number: float = float(input("Type the number: "))
Square: float = number*number
print(f"Square of the number is {Square}")
if __name__== "__main__":
    main() 