def greet(name):
    """Greets the user with a personalized message."""
    print(f"Hello, {name}! Welcome.")

greet("Pratik")
# Using the lambda function
square = lambda x: x * x
result = square(5)
print("The square of 5 is:", result)

# Combining functions and lambda functions
def apply_operation(number, operation):
    """Applies the given operation to the number."""
    return operation(number)

double = lambda x: x * 2
result = apply_operation(3, double)
print("Double of 3 is:", result)