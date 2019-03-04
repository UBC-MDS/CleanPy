#!/usr/bin/env python

import pandas as pd
import numpy as np

def locate_na(data: pd.DataFrame) -> dict:
    """ 
    Locate and return the indices to all missing values within an inputted dataframe. 
    Each element of the returned dictionary will be a column in a dataframe, which will 
    contain the row indices of the missing values.
    
    Parameters
    ----------
    data : dataframe
        This is the dataframe that the function will use to locate NAs.
        
    Returns
    -------
    dictionary of lists 
        key = column indices that contain missing values
        value = list of row indices that have missing values
        
    >>> locate_na(pd.DataFrame(np.array([[“Yes”, “No”], [None, “Yes”]])))
    {"0": [1]}
    >>> locate_na(pd.DataFrame(np.array([[1, 2, None], [None, 2, 3]])))
    {"0": [1], "2": [0]}
    """
    try:
        if not isinstance(data, pd.DataFrame):
            raise(TypeError)
        col_na: dict = {}
        for i in data:
            row_na: list = []
            for j in range(len(data[i])):
                if (pd.isna(data[i][j])):
                    row_na.append(j)
            if (len(row_na) != 0):
                col_na[i] = row_na
        if (len(col_na) == 0):
            print("There are no missing values.")
        return col_na
    except TypeError:
        print("Input data type is not of type pd.DataFrame.")
        raise