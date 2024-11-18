import pandas as pd

data3 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Eve'],
    'Location': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df3 = pd.DataFrame(data3)

merged_df = pd.merge(df, df3, on='Name', how='left')
print("\nMerged DataFrame:\n", merged_df)
