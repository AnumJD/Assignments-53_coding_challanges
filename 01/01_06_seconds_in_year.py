"""Problem Statement: Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

There are 5 seconds in a year!

You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute."""

#Solution
days_in_one_year:int = 365
hours_in_a_day:int = 24
minutes_in_an_hour:int = 60
seconds_in_minute:int = 60
def main():
    print("Let's calculate seconds in a year")
    seconds_in_a_year:int= days_in_one_year*hours_in_a_day*minutes_in_an_hour*seconds_in_minute
    print(f"There are {seconds_in_a_year} seconds in a year")
if __name__=="__main__":
    main()