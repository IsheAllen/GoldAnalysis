from scripts.data_cleaning import clean_data

# Path to your dataset
file_path = "datasets/XAU_1d_data_2004_to_2024-09-20.csv"

# Clean the dataset
cleaned_data = clean_data(file_path)

# Save the cleaned dataset
cleaned_data.to_csv("outputs/cleaned_XAU_1d_data.csv", index=False)
print("Cleaned data saved successfully!")