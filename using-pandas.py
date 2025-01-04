# Import necessary libraries
import pandas as pd

# Load the dataset
# Replace 'dataset.csv' with the path to dataset file
df = pd.read_csv('dataset.csv')

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Print the data types of each column
print("\nData types of each column:")
print(df.dtypes)

# Get basic statistics of the dataset
print("\nBasic statistics of the dataset:")
print(df.describe())

# Perform a simple analysis
# Example: Calculate the average value of a numeric column 'num'

average_value = df['num'].mean()
print(f"\nAverage value of 'num': {average_value}")

# Group data by a categorical column and calculate the mean of another column
# Replace 'categorical_column' with the name of the categorical column
# Replace 'numeric_column' with the name of the numeric column
grouped_data = df.groupby('categorical_column')['numeric_column'].mean()
print(f"\nMean of 'numeric_column' grouped by 'categorical_column':")
print(grouped_data)

# Save the grouped data to a new CSV file
grouped_data.to_csv('grouped_data.csv', index=True)
print("\nGrouped data saved to 'grouped_data.csv'")
