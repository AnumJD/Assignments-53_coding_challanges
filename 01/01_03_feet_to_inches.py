#Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

foot_in_inches = 12
def main():
    print("Feet to Inches Conversion: ")
    feet: float = float(input("Enter value in feet: "))
    print(f"Converted value of {feet} in inches is {foot_in_inches * feet}")
if __name__=="__main__":
    main()    