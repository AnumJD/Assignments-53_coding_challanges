#Problem Statement: Simulate rolling two dice, and print results of each roll as well as the total.
#Solution
import random
SIDE_OF_DICE = 6
def main():
    dice1: int = random.randint(1,SIDE_OF_DICE)
    dice2: int = random.randint(1,SIDE_OF_DICE)
    print(f"Value of dice1 is: {dice1}, and value of dice2 is: {dice2}, Total is: {dice1+dice2}")
if __name__=="__main__":
    main()