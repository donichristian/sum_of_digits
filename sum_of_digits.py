# Define a function called sum_of_digits that takes an integer n as input
def sum_of_digits():
    """
    Prompts the user to input an integer and calculates the sum of its digits.
    """
    # Prompt user to input an integer
    n = int(input("Enter an integer: "))
    # Call the calculate_sum_of_digits function with input n and store the result
    result = calculate_sum_of_digits(n)
    # Print the sum of the digits of the input integer
    print("The sum of the digits of", n, "is", result)

# Define a recursive function to calculate the sum of the digits of an integer
# Define a recursive function to calculate the sum of the digits of an integer
def calculate_sum_of_digits(n):
    """
    Recursively calculates the sum of the digits of an integer.
    
    Args:
    n: The integer for which the sum of digits is to be calculated.
    
    Returns:
    The sum of the digits of the input integer.
    """
    # Take the absolute value of n to handle negative numbers
    n = abs(n)
    
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Recursive case: return the last digit of n plus the result of calling calculate_sum_of_digits with the remaining digits
    else:
        return n % 10 + calculate_sum_of_digits(n // 10)

# Call the sum_of_digits function to start the program
sum_of_digits()

# The big O notation of the given function sum_of_digits is O(log n), where n is the input integer.

# Step-by-step flow for the function sum_of_digits with the input n=123

# sum_of_digits(123)
# 123 % 10 + sum_of_digits(12)
# 3 + (12 % 10 + sum_of_digits(1))
# 3 + (2 + (1 % 10 + sum_of_digits(0))
# 3 + (2 + (1 + sum_of_digits(0))
# 3 + (2 + (1 + 0))
# 3 + (2 + 1)
# 3 + 3
# 6