from scripts.feature_engineering import feature_engineering_pipeline

# Path to the cleaned dataset
cleaned_file_path = "outputs/cleaned_XAU_1d_data.csv"

# Path to save the enhanced dataset
enhanced_file_path = "outputs/enhanced_XAU_1d_data.csv"

# Run the feature engineering pipeline
enhanced_data = feature_engineering_pipeline(cleaned_file_path)

# Save the enhanced dataset
enhanced_data.to_csv(enhanced_file_path, index=False)
print("Enhanced data saved successfully!")