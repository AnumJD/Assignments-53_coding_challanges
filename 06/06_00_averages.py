"""Write a function that takes two numbers and finds the average between the two."""
#SOLUTION: 
def find_average(num1,num2):
    average = (num1+num2)/2
    return average
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Average Numberis:  {find_average(num1,num2)}")