#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:02:49 2018

@author: phuntsoktseten
"""
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
    if data.isna().all(axis = None):
        raise TypeError("Input must not be all missing values")
    if replace=="mean":
        for i in columns:
            mean = data[i].mean()
            z = z.fillna({i: mean})
        return z

    if replace=="min":
        for i in columns:
            min_ = data[i].min()
            z= z.fillna({i: min_})
        return z

    if replace=="median":
        for i in columns:
            median = data[i].median()
            z = data.fillna({i: median})
        return z
            
    if replace=="max":
        for i in columns:
            max_ = data[i].max()
            z = data.fillna({i: max_})
        return z
   
