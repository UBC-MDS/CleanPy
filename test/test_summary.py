#Test cases: 
#The input data must be a dataframe. Otherwise, the function will return an error message “input_df must be a dataframe”
#Data columns should have one datatype. If datatype is mostly strings, return summary statistics for strings. 
#If datatype is mostly numbers, return summary statistics for numbers 
#If all columns are numbers, return summary statistics with numbers
#If some columns are integers, and some are floats, return summary statistics using each columns data type
#If one column has a mixture of data types (strings, floats or ints) return summary statistics by converting all entries into the predominant datatype
#If a column contains any entries that are not of the type string float or int, return error message “This function only handles strings, floats and integer data types”

import pandas as pd
import numpy as np
import pytest
import sys
sys.path.append("../CleanPy")

import CleanPy as cp
# Helper codes
toy_data = pd.DataFrame({"x":[None, "b", "c"], "y": [2, None, None], "z": [3.6, 8.5, None]})
toy_all_na = pd.DataFrame({"x":[None, None, None], "y": [None, None, None], "z": [None, None, None]})
toy_no_na = pd.DataFrame({"x":[1, 2, 3, 4], "y": [1, 2, 3, 4], "z": [1, 2, 3, 4]})

The input data must be a dataframe. Otherwise, the function will return an error message “input_df must be a dataframe”
def get_max_list(data):
    return max(len(v) for k, v in data.items())

# Test functions
def test_data_type():
    """
    Test that the function returns an error if 
    the input type is incorrect
    """
    with pytest.raises(TypeError):
        cp.summary("Input Data")
        cp.summary([1, 2, 3, 4, 5])
        cp.summary(True)
        cp.summary((True, "False"))
        cp.summary({"x":[1,2], "y":[3,4]})
        
def test_output_type():
    """
    Test that the output type must be a nested dataframe 
    """
    assert type(cp.summary(toy_data)) == pd.DataFrame
    assert type(cp.summary(toy_data2)) == pd.DataFrame
    assert type(cp.summary(toy_all_na)) == df
    assert type(cp.summary(toy_no_na)) == df
    
def test_output_shape():
    """
    Test that output is a nested dataframe
    """
    assert get_max_list(cp.summary(toy_data)) <= toy_data.shape[0]
    assert get_max_list(cp.summary(toy_all_na)) <= toy_all_na.shape[0]
    assert get_max_list(cp.summary(toy_no_na)) <= toy_no_na.shape[0]
    assert len(cp.locate_na(toy_data)) <= toy_data.shape[1]
    assert len(cp.locate_na(toy_all_na)) <= toy_all_na.shape[1]
    assert len(cp.locate_na(toy_no_na)) <= toy_no_na.shape[1]
    
def test_type_data():
    """
    Test for the correct functionality of the function
    """
    