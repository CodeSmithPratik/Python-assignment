import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}


df = pd.DataFrame(data)


df.to_csv('prince.csv', index=False)

print("CSV file 'prince.csv' has been created.")
