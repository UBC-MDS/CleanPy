#!/usr/bin/env python

def locate_na(data):
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
    {"1": [0]}
    >>> locate_na(pd.DataFrame(np.array([[1, 2, None], [None, 2, 3]])))
    {"0": [2], "1": [0]}
    """
    
    return 