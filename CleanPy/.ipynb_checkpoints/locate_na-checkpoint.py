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
        Each list in the dictionary represents a column and
        holds the indices of missing values in the dataframe. 
        
    >>> locate_na(pd.DataFrame(np.array([[“Yes”, “No”], [“”, “Yes”]])))
    [(1, 0)]
    >>> locate_na(pd.DataFrame(np.array([[“Yes”, “No”, “”], [“”, “Yes”, “Yes”]])))
    [(0, 2), (1, 0)]
    """
    
    return 