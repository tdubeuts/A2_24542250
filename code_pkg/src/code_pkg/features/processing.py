import pandas as pd

def merge_dataframes(df1, df2, left_index=True, right_index=True):
    """
    Merges two DataFrames on their indexes.

    Parameters:
    df1 (pd.DataFrame): The first DataFrame.
    df2 (pd.DataFrame): The second DataFrame.
    left_index (bool): Whether to use the index from the left DataFrame as the join key.
    right_index (bool): Whether to use the index from the right DataFrame as the join key.

    Returns:
    pd.DataFrame: The merged DataFrame.
    """
    df = pd.merge(df1, df2, left_index=left_index, right_index=right_index)

    return df

def unpivot_cols(df, columns):
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
    df = df[columns].values.tolist()
            
    return df



def filter_columns(df, exclude_cols):
    """
    Filters out specified columns from a DataFrame.

    Parameters:
    df (pd.DataFrame): The original DataFrame.
    exclude_cols (list): The list of columns to exclude.

    Returns:
    list: A list of columns that are not in the exclude_cols list.
    """
    filtered_columns = [col for col in df.columns if col not in exclude_cols]
    return filtered_columns
def unpivot_dataframe(df, id_vars, value_vars, var_name='d', value_name='sales'):
    """
    Unpivots a DataFrame, keeping specified columns fixed and unpivoting the rest.

    Parameters:
    df (pd.DataFrame): The DataFrame to unpivot.
    id_vars (list): The list of columns to keep fixed.
    value_vars (list): The list of columns to unpivot.
    var_name (str): The name of the variable column.
    value_name (str): The name of the value column.

    Returns:
    pd.DataFrame: The unpivoted DataFrame.
    """
    unpivoted_df = pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name=var_name, value_name=value_name)
    return unpivoted_df

def concatenate_dataframes(train_df, test_df, keys=['train', 'test'], key_name='key'):
    """
    Concatenates the training and test DataFrames, adds a key column, and resets the index.

    Parameters:
    train_df (pd.DataFrame): The training DataFrame.
    test_df (pd.DataFrame): The test DataFrame.
    keys (list): The keys to use for the concatenated DataFrame.
    key_name (str): The name of the key column.

    Returns:
    pd.DataFrame: The concatenated DataFrame with a key column.
    """
    concatenated_df = pd.concat([train_df, test_df], keys=keys).reset_index(level=0).rename(columns={'level_0': key_name})
    return concatenated_df

def cal_merge(df1, df2, on_column, how='inner'):
    """
    Merges two DataFrames on a specified column.

    Parameters:
    df1 (pd.DataFrame): The first DataFrame.
    df2 (pd.DataFrame): The second DataFrame.
    on_column (str): The column name to merge on.
    how (str): The type of merge to be performed. Default is 'inner'.

    Returns:
    pd.DataFrame: The merged DataFrame.
    """
    merged_df = df1.merge(df2, on=on_column, how=how)
    return merged_df

def merge_sales_with_calendar(sales_df, calendar_df, on_column='d', how='inner'):
    """
    Merges the sales DataFrame with the calendar DataFrame on a specified column.

    Parameters:
    sales_df (pd.DataFrame): The sales DataFrame.
    calendar_df (pd.DataFrame): The calendar DataFrame.
    on_column (str): The column name to merge on. Default is 'd'.
    how (str): The type of merge to be performed. Default is 'inner'.

    Returns:
    pd.DataFrame: The merged DataFrame.
    """
    merged_df = sales_df.merge(calendar_df, on=on_column, how=how)
    return merged_df

def merge_sales_with_price(sales_df, price_df, on_columns, how='inner'):
    """
    Merges the sales DataFrame with the price DataFrame on specified columns.

    Parameters:
    sales_df (pd.DataFrame): The sales DataFrame.
    price_df (pd.DataFrame): The price DataFrame.
    on_columns (list): The list of columns to merge on.
    how (str): The type of merge to be performed. Default is 'inner'.

    Returns:
    pd.DataFrame: The merged DataFrame.
    """
    merged_df = sales_df.merge(price_df, on=on_columns, how=how)
    return merged_df

def convert_d_column(df, column, delimiter, part_index, new_type):
    """
    Splits the values in a specified column by a delimiter, extracts a part, and converts the type.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the column to process.
    column (str): The name of the column to split and convert.
    delimiter (str): The delimiter to split the column values.
    part_index (int): The index of the part to extract after splitting.
    new_type (type): The new type to convert the extracted part to.

    Returns:
    pd.DataFrame: The DataFrame with the processed column.
    """
    def convert(input):
        return input.split(delimiter)[part_index]

    df[column] = df[column].apply(convert).astype(new_type)
    return df

def save_Sales(Sales=None, path='../data/processed/'):

    import numpy as np

    if Sales is not None:
      np.save(f'{path}X_train', Sales)
    