#!/usr/bin/env python

def summary(data, zero_include=True):
    """
    It will determine the main data type of the column by calculated the type 
    of each row entry in the column, and using the most frequent data type as 
    the expected input for that column. It will perform two different summary 
    statistics based on 2 different groups of datatypes of either 1) string or 
    2) int/float. For number columns it returns a dataframe of columns which 
    contain dataframes of summary statistics including mean value for each column, 
    min, max, count (number of non NA values per column) and count_NA (number of 
    NA values per column). Similarly, for string columns it returns the unique 
    string values and their counts. It will also provide a count of NA values 
    which will include empty strings, and anything other than the correct data 
    type for each column.
    
    Parameters
    ----------
    data : dataframe
        This is the dataframe that the function will use to provide summary statistics on.  
        
    zero_include : boolean
        True, if you want zeros to represent values. Otherwise, False, if you
        you want to count them as missing values. 

    Returns
    -------
    dataframe
        Returns a nested dataframe where the columns would represent the columns 
        of the original data set. The inner dataframes would contain the summary 
        statistics of the particular column of the original data. 
    
    >>> summary(pd.DataFrame({"x": [1, 1, 1], "y": [2, 2, 2]}))
    pd.DataFrame({pd.DataFrame("x": {"min":1, "max":1, "mean":1}), pd.DataFrame("y": {"min":2, "max":2, "mean":2})})
    """
    
    return 