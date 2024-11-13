"""10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd"""
#Solution:
def even_odd_count():
    for i in range(10, 20):  # Iterate from 10 to 19
        if i % 2 == 0:
            print(f"{i} even")
        else:
            print(f"{i} odd")

# Call the function to execute
even_odd_count()
