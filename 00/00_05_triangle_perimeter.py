"""Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

Here's a sample run of the program (user input is in bold italics):

What is the length of side 1? 3

What is the length of side 2? 4

What is the length of side 3? 5.5

The perimeter of the triangle is 12.5"""
#Solution
def main():
    print("Enter length of each side of a triangle")
    side_1: float = float(input("What is the length of side_1?: "))
    side_2: float = float(input("What is the length of side_2?: "))
    side_3: float = float(input("What is the length of side_3?: "))
    perimeter_of_triangle: int = side_1 + side_2 + side_3
    print(f"The perimeter of the triangle is: {perimeter_of_triangle}")
if __name__ == "__main__":
    main()