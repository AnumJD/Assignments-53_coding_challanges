'''Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).'''
#Solution
def main():
    print("Tell me your favourite animal")
Favourite_Animal : str = input("Please Enter your favorite animal: ")
print(f"My Favourite Animal is also {Favourite_Animal}!")
if __name__ == '__main__':
    main()