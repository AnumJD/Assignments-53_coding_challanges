"""Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high) Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

#SOLUTION:

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True

    # If not in range, return False
    return False