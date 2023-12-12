import pandas as pd

# # Path to your CSV file
# csv_file_path = 'per_water.csv'

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv(csv_file_path)

# # Define your custom function to rename values
# def custom_renaming_algorithm(value):
#     # Implement your algorithm or conditions here
#     # For example, let's convert strings to uppercase
#     return " ".join(value.split("_")).lower()

# # Apply the custom function to the 'ColumnToRename' column
# df['constituency'] = df['constituency'].apply(custom_renaming_algorithm)

# # Save the updated DataFrame to a new CSV file
# updated_csv_file_path = 'per_water.csv'
# df.to_csv(updated_csv_file_path, index=False)

# print(f"Updated data saved to {updated_csv_file_path}")




# # Path to your CSV files
# file1_path = 'per_water.csv'
# file2_path = 'merged_file_1.csv'

# # Read the CSV files into pandas DataFrames
# df1 = pd.read_csv(file1_path)
# df2 = pd.read_csv(file2_path)

# # Merge DataFrames based on the common column
# merged_df = pd.merge(df1, df2, on='constituency', how='inner')  # Change 'how' parameter if needed

# # Save the merged DataFrame to a new CSV file
# merged_file_path = 'merged_file_5.csv'
# merged_df.to_csv(merged_file_path, index=False)

# print(f"Merged data saved to {merged_file_path}")




## Path to your CSV file
# csv_file_path = 'merged_file_5.csv'

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv(csv_file_path)

# # Remove duplicate rows based on all columns
# df_no_duplicates = df.drop_duplicates()

# # Save the DataFrame without duplicates to a new CSV file
# updated_csv_file_path = 'merged_file_5.csv'
# df_no_duplicates.to_csv(updated_csv_file_path, index=False)

# print(f"Updated data saved to {updated_csv_file_path}")
