# Lambda function to calculate the factorial of a number
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
print(factorial(5))  
print('\n')

# Output: 120