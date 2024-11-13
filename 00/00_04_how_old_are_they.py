"""Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen.

Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):"""
#Solution
def main():
    print ("Age of all friends")
    Anton_age: int = 21
    Beth_age: int = Anton_age + 6
    Chen_age: int = Beth_age + 20
    Drew_age: int = Chen_age + Anton_age
    Ethan_age:int = Chen_age
    print(f"Anton_age: {Anton_age}")   
    print(f"Beth_age: {Beth_age}")
    print(f"Chen_age: {Chen_age}")
    print(f"Drew_age: {Drew_age}")
    print(f"Ethan_age: {Ethan_age}")
if __name__ == '__main__':
    main()