import pandas as pd
import numpy as np

def add_rolling_averages(data, windows=[50, 200]):
    """
    Add rolling averages to the dataset.

    Args:
        data (pd.DataFrame): Input DataFrame.
        windows (list): List of rolling average windows (in days).

    Returns:
        pd.DataFrame: DataFrame with rolling averages added.
    """
    for window in windows:
        data[f"MA_{window}"] = data['Close'].rolling(window=window).mean()
    print("Rolling Averages Added")
    return data

def add_volatility(data, window=20):
    """
    Add rolling standard deviation (volatility) to the dataset.

    Args:
        data (pd.DataFrame): Input DataFrame.
        window (int): Rolling window size.

    Returns:
        pd.DataFrame: DataFrame with volatility added.
    """
    data['Volatility'] = data['Close'].rolling(window=window).std()
    print("Volatility Added")
    return data

def add_daily_returns(data):
    """
    Add daily returns to the dataset.

    Args:
        data (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with daily returns added.
    """
    data['Daily_Return'] = data['Close'].pct_change()
    print("Daily Returns Added")
    return data

def calculate_rsi(data, window=14):
    """
    Calculate Relative Strength Index (RSI).

    Args:
        data (pd.DataFrame): Input DataFrame.
        window (int): Rolling window size for RSI calculation.

    Returns:
        pd.DataFrame: DataFrame with RSI added.
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    print("RSI Added")
    return data

def add_cumulative_returns(data):
    """
    Add cumulative returns to the dataset.

    Args:
        data (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with cumulative returns added.
    """
    data['Cumulative_Return'] = (1 + data['Daily_Return']).cumprod()
    print("Cumulative Returns Added")
    return data

def feature_engineering_pipeline(filepath):
    """
    Perform full feature engineering pipeline.

    Args:
        filepath (str): Path to the cleaned data file.

    Returns:
        pd.DataFrame: Enhanced DataFrame with new features.
    """
    # Load the cleaned data
    data = pd.read_csv(filepath)
    print("Cleaned Data Loaded")

    # Add features
    data = add_rolling_averages(data)
    data = add_volatility(data)
    data = add_daily_returns(data)
    data = calculate_rsi(data)
    data = add_cumulative_returns(data)

    # Drop rows with NaN values resulting from rolling calculations
    data = data.dropna()
    print("Feature Engineering Complete")
    return data