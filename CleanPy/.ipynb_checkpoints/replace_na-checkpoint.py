def replace_na(data, replace="average", remove=False, columns):
    """
    This function replaces NA values with either the min, max, median or average 
    value or removes the rows.

    Parameters
    ----------
    data : dataframe
        This is the dataframe that the function will use to replace NAs.
        
    replace : string
        Specifies how to replace missing values.
        values include: "min", "max", "median", "average"
    
    remove : boolean
        Tells the function whether or not to remove rows with NA.
        If True, replace argument will not be used.
    
    columns : list
        List of columns to replace missing values on.
        
    Returns
    -------
    dataframe
        A pandas dataframe where each NAs will be replaced by either 
        min, max, median or average (specified by the user)
    
    >>> replace_na(pd.DataFrame(np.array([[0, 1], [NA, 1]])), replace="min", columns=[0])
    pd.DataFrame(np.array([[0, 1], [0, 1]]))
    """
    
    return