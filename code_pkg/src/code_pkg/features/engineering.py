import pandas as pd
from sklearn.preprocessing import LabelEncoder


def datetime_to_integer(df, datetime_column):
    """
    Converts a datetime column in a DataFrame to an integer representing the number of seconds since the Unix epoch.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the datetime column.
    datetime_column (str): The name of the datetime column to convert.

    Returns:
    pd.DataFrame: The DataFrame with the datetime column converted to an integer.
    """

    df[datetime_column + '_int'] = df[datetime_column].astype(int) // 10**9
    return df
    
def datetime_to_day_month_year(df, datetime_column):
    """
    Converts a datetime column in a DataFrame into separate columns for day, month, and year.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the datetime column.
    datetime_column (str): The name of the datetime column to convert.

    Returns:
    pd.DataFrame: The DataFrame with separate columns for day, month, and year.
    """
    df[datetime_column] = pd.to_datetime(df[datetime_column])
    df['day'] = df[datetime_column].dt.day
    df['month'] = df[datetime_column].dt.month
    df['year'] = df[datetime_column].dt.year
    return df


def encode_and_combine_columns(df, num_cols, cat_cols):
    """
    Encodes categorical columns in a DataFrame using LabelEncoder, drops the original columns,
    and combines the numerical columns with the encoded categorical columns.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the categorical and numerical columns.
    num_cols (list): The list of numerical columns to keep.
    cat_cols (list): The list of categorical columns to encode and drop.

    Returns:
    pd.DataFrame: A new DataFrame with numerical columns and encoded categorical columns.
    """
    label_encoder = LabelEncoder()
    for column in cat_cols:
        df[column + '_encoded'] = label_encoder.fit_transform(df[column])
    
    # Create a new DataFrame with numerical columns and encoded categorical columns
    new_df = df[num_cols + [column + '_encoded' for column in cat_cols]].copy()
    
    return new_df

