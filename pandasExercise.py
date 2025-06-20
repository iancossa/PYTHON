import pandas as pd
import numpy as np

# Create a more complex sample DataFrame
data = {
    'ProductID': [101, 102, 103, 104, 105, 106],
    'ProductName': ['Laptop', 'Keyboard', 'Mouse', 'Monitor', 'Camera', 'Printer'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories', 'Electronics'],
    'Price': [1200.00, 75.00, 25.00, 300.00, np.nan, 150.00],
    'Stock': [50, 150, 200, 30, 75, np.nan]
}
more_sample_df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_filename_more = 'more_sample_data.csv'
more_sample_df.to_csv(csv_filename_more, index=False)

print(f"CSV file '{csv_filename_more}' created successfully.")
df=pd.read_csv("more_sample_data.csv")#importing data
print(df) #dataframe obj
df.drop("ProductID",axis=1,inplace=True)
print(df)
df.to_csv('copy.csv')#exporting data

