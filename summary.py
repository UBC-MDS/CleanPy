# [reference](https://github.com/pandas-dev/pandas/blob/v0.24.1/pandas/core/generic.py#L9484-L9815)
import pandas as pd
import numpy as np

def summary(data):
    '''
    This function computes summary statistics for text and numerical column_data from a given column_dataframe.
    Input: dictionary or column_dataframe
    Returns summary statistics for each column in a nested pandas column_dataframe. Since pandas only accepts one data type per column, 
    we only need to test the type of each column once.
    It will perform two different summary statistics based on 2 column_datatypes of either
    1) string/bool or 2) int/float/datetime object. For numeric data columns it returns a dictionary of summary statistics including
    mean value for each column, min, max, mean, median and count (number of non NA values per column) and count_NA
    (number of NA values per column). Similarly, for string columns it returns the unique string values and
    their counts in a dictionary. The column summary statistics are then nested into a pandas dataframe and returned.
    
    Parameters
    ----------
    data : pd.DataFrame
        used to provide summary statistics of each column.
    
    Returns
    -------
    Summary pandas dataframe of each column's summary statistics
    >>> summary(pd.column_dataFrame(colnames="Likes coding", rows= np.array([[4,3,2, 2])))
    pd.DataFrame(
        min= 2
        max= 4
        mean= 11/4
        median= 2
        count= 4
        count_NA= 0)
    '''
    #find unique values in a list
    def unique(seq): 
        noDupes = []
        [noDupes.append(i) for i in seq if not noDupes.count(i)]
        return noDupes
    
    def get_numeric_stats(column_data):
        col_df= pd.DataFrame(column_data)
        col_vals= column_data.values
        stats_dict = {
            "Unique"      :   column_data.unique(),
            "count"       :   column_data.count(),
            "count_NAs"   :   column_data.isna().sum(),
            "count_unique":   len(column_data.unique()),
            "min_"        :   np.min(column_data),
            "max_"        :   np.max(column_data),
            "mean"        :   np.mean(column_data),
            "median"      :   np.median(column_data),
        }
        return(stats_dict)
                
    def get_categorical_stats(column_data):
        #find unique strings and assign them as keys in a dictionary with their counts as values 
        
        objcounts = column_data.value_counts()
        count_unique = len(objcounts[objcounts != 0]) 
        stats_dict = {
            "Unique"       : column_data.unique(), #could add counts of each word with countvectorizer
            "count"        : len(objcounts),
            "count_unique" : len(objcounts[objcounts != 0]),
            "count_NAs"    : column_data.isna().sum()
        }             
        return stats_dict
    
    #check that input is a pandas df 
    if isinstance(data, pd.DataFrame) == False:
        raise NotImplementedError("Input should be a pandas dataframe. Use pd.DataFrame(data)")
    # check dimensions
    if data.ndim >= 3:
        msg = "Summary is not implemented on Panel objects."
        raise NotImplementedError(msg)
    elif data.ndim == 2 and data.columns.size == 0:
        raise ValueError("Cannot describe a column_dataFrame without columns")
    column_names = list(data.columns.values)
    summary_dict = {}
    for column in column_names:
        #print(data[column])
        if (data[column].dtype == "float64" or data[column].dtype == "int64" or data[column].dtype == "timedelta64"): # Numeric Data Column
            summary_stats = get_numeric_stats(data[column])
        else: # Categorical Data Column
            summary_stats = get_categorical_stats(data[column])
        summary_dict[column] = summary_stats
    return(pd.DataFrame(summary_dict))