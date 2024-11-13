#Problem Statement: Simulate rolling two dice, three times. Print the results of each die roll. This program is used to show how variable scope works.
#Solution
import random
NUM_SIDES = 6
def roll_dice():
    die1: int= random.randint(1,NUM_SIDES)
    die2: int= random.randint(1,NUM_SIDES)
    total: int = die1+die2
    print("Total of two dice is", total)

def main():
    die1:int=10
    print("Value of die_1 is" + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("Value of die_1 is" + str(die1))

if __name__ == "__main__":
    main()