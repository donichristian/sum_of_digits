import unittest

# Define the function to be tested
def calculate_sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    else:
        return n % 10 + calculate_sum_of_digits(n // 10)

# Define the test class
class TestSumOfDigits(unittest.TestCase):
    
    # Test case for input 0
    def test_sum_of_digits_zero(self):
        result = calculate_sum_of_digits(0)
        print("Result for input 0:", result)
        self.assertEqual(result, 0)
    
    # Test case for input 123
    def test_sum_of_digits_123(self):
        result = calculate_sum_of_digits(123)
        print("Result for input 123:", result)
        self.assertEqual(result, 6)
    
    # Test case for input -456
    def test_sum_of_digits_negative(self):
        result = calculate_sum_of_digits(-456)
        print("Result for input -456:", result)
        self.assertEqual(result, 15)

# Run the tests
if __name__ == '__main__':
    unittest.main()