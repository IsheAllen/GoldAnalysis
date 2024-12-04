# Import necessary libraries
import pandas as pd
import numpy as np
import os

# Function to load a CSV file
def load_data(filepath):
    """
    Load a dataset from the given filepath.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    return pd.read_csv(filepath)

# Function to check missing values
def check_missing_values(data):
    """
    Check for missing values in the dataset.

    Args:
        data (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Summary of missing values.
    """
    missing_summary = data.isnull().sum()
    print("Missing Values Summary:")
    print(missing_summary[missing_summary > 0])
    return missing_summary

# Function to handle missing values
def handle_missing_values(data, strategy='drop'):
    """
    Handle missing values in the dataset.

    Args:
        data (pd.DataFrame): Input DataFrame.
        strategy (str): Strategy for handling missing values ('drop' or 'fill_mean').

    Returns:
        pd.DataFrame: DataFrame with missing values handled.
    """
    if strategy == 'drop':
        return data.dropna()
    elif strategy == 'fill_mean':
        return data.fillna(data.mean())
    else:
        raise ValueError("Invalid strategy. Use 'drop' or 'fill_mean'.")

# Function to remove duplicates
def remove_duplicates(data):
    """
    Remove duplicate rows from the dataset.

    Args:
        data (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with duplicates removed.
    """
    duplicates_count = data.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates_count}")
    return data.drop_duplicates()

# Data cleaning pipeline
def clean_data(filepath):
    """
    Perform full data cleaning pipeline.

    Args:
        filepath (str): Path to the raw data file.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Load raw data
    raw_data = load_data(filepath)
    print("Data Loaded Successfully")

    # Check missing values
    check_missing_values(raw_data)

    # Handle missing values (choose strategy)
    cleaned_data = handle_missing_values(raw_data, strategy='drop')
    print("Missing Values Handled")

    # Remove duplicates
    cleaned_data = remove_duplicates(cleaned_data)
    print("Duplicates Removed")

    return cleaned_data