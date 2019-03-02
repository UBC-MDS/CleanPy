#!/usr/bin/env python3

import pandas as pd
import numpy as np 

def replace_na(data, columns, replace="mean", remove=False):
    """
    This function replaces NA values with either the min, max, median or mean
    value or removes the rows.
    Parameters
    ----------
    data : dataframe
        This is the dataframe that the function will use to replace NAs.
        
    columns : list
        List of columns to replace missing values on.
        
    replace : string
        Specifies how to replace missing values.
        values include: "mean","min", "max", "median"
    
    remove : boolean
        Tells the function whether or not to remove rows with NA.
        If True, replace argument will not be used.
        
    Returns
    -------
    dataframe
        A pandas dataframe where each NAs will be replaced by either mean,
        min, max, median  (specified by the user)
    
    >>> replace_na(pd.DataFrame(np.array([[0, 1], [NA, 1]])), replace="min", columns=[0])
    pd.DataFrame(np.array([[0, 1], [0, 1]]))
    """
    z = data.copy()
    
    # Return error if data has only missing values
    if data.isna().all(axis = None):
        raise TypeError("Input must not be all missing values.")
    
    # Return error if the data argument is a dataframe
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input data must be a pandas dataframe.")
        
    # Return error if the columns argument is a list
    if not (isinstance(columns, list) or isinstance(columns, np.ndarray)) :
        raise TypeError("Please make sure the column(s) you would like to replace is a list or numpy array type.")
    
    # Return error if columns have numeric types
    for i in columns:
        if not (data[i].dtypes == 'float64' or data[i].dtypes == 'int64'):
            raise KeyError("Please make sure the column you are replacing is numeric.")

    if replace=="mean":
        for i in columns:
            mean = data[i].mean()
            z = z.fillna({i: mean})
    #elif replace=="min":
        #for i in columns:
            #min_ = data[i].min()
            #z= z.fillna({i: min_})
    #elif replace=="median":
        #for i in columns:
            #median = data[i].median()
            #z = data.fillna({i: median})
    #elif replace=="max":
        #for i in columns:
            #max_ = data[i].max()
            #z = data.fillna({i: max_})
    return z
#

    
