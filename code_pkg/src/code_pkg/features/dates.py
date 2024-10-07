import pandas as pd
from datetime import datetime

def convert_to_date(df, cols:list):
    """Convert specified columns from a Pandas dataframe into datetime

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    cols : list
        List of columns to be converted

    Returns
    -------
    pd.DataFrame
        Pandas dataframe with converted columns
    """
    import pandas as pd

    for col in cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])
    return df
    
def add_weekday_column(df, date_column):
    """
    Adds a new column 'weekday' to the DataFrame with the day of the week extracted from the date column.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the date column.
    date_column (str): The name of the date column in the DataFrame.

    Returns:
    pd.DataFrame: The DataFrame with the new 'weekday' column.
    """
    df['weekday'] = df[date_column].dt.dayofweek
    return df

def if_weekends(df,weekends = [5,6]):
    if df in weekends:
        return 1
    else:
        return 0
from datetime import datetime



def convert_and_replace(dfs, column_name):
    # Define the conversion function
    def convert_int_to_date(timestamp):
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    
    # Iterate over each DataFrame in the list
    for df in dfs:
        # Apply the conversion function to the specified column and replace it
        df[column_name] = df[column_name].apply(convert_int_to_date)
    
    return dfs