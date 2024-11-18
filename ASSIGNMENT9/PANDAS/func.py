import pandas as pd

data2 = {
    'Department': ['HR', 'Finance', 'HR', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Salary': [50000, 60000, 55000, 70000]
}

df2 = pd.DataFrame(data2)

grouped = df2.groupby('Department')['Salary'].mean().reset_index()
print("\nMean Salary by Department:\n", grouped)
