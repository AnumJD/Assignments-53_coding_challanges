#Problem Statement: Write a function that takes a list of numbers and returns the sum of those numbers.
def add_many_numbers(numbers):
    total = 0
    for i in numbers:
        total+= i
    return total
def main():
    numbers = [1,3,4,5,7]
    sum = add_many_numbers(numbers)
    print(f"Sum of numbers= {sum}")
if __name__ == "__main__":
    main()