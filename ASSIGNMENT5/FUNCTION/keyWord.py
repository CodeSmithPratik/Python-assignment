# Function with keyword arguments
def print_info(name, age, **kwargs):
    print(f"Name: {name}, Age: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Bob", age=30, city="New York", country="USA")

# Output:
# Name: Bob, Age: 30
# city: New York
# country: USA