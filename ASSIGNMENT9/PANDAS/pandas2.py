import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 22, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Selecting a specific column
print("\nNames:\n", df['Name'])

filtered_df = df[df['Age'] > 30]
print("\nPeople older than 30:\n", filtered_df)

df['Salary'] = [50000, 60000, 45000, 70000]
print("\nDataFrame with Salary:\n", df)

print("\nAverage Age:", df['Age'].mean())

