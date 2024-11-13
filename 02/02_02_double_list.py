"""Problem Statement: Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]"""

#Solution
def main():
    data = [1,2,3,4]
    for i in range(len(data)):
        indexing_of_data = data[i]
        data[i]=indexing_of_data*2
    print(data)
if __name__=="__main__":
    main()