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

import summary as sm
# Helper codes
toy_data = pd.DataFrame({"x":[None, "b", "c"], "y": [2, None, None], "z": [3.6, 8.5, None]})
toy_all_na = pd.DataFrame({"x":[None, None, None], "y": [None, None, None], "z": [None, None, None]})
toy_no_na = pd.DataFrame({"x":[1, 2, 3, 4], "y": [1, 2, 3, 4], "z": [1, 2, 3, 4]})
toy_mixed_strings= pd.DataFrame({"x":[1,3,4,5], "y": ["Female", "Female", "Male", "man"]})
toy_mixed_data_type = pd.DataFrame({"x":[1,3,4,5], "y": ["Female", "Female", "Male", 22]}) #typo is 22
numeric_data = pd.DataFrame({"y": [2, None, None], "z": [3.6, 8.5, 10]})

simple_data = pd.DataFrame({"x":["a", "b", None], "y": [ None, 3, 3]})
dict1= {"Unique":["a","b", None], "count" : 2, "count_NAs": 1, "count_unique": 2, "max_": 'NaN', "mean": 'NaN', "median": 'NaN', "min_": 'NaN'}
dict2= {"Unique":['nan', 1.0, 3.0], "count" : 2, "count_NAs": 1, "count_unique": 2, "max_": 3, "mean": 2, "median": 'NaN', "min_": 1}
summary_dict = {}
summary_dict["x"] = dict1
summary_dict["y"] = dict2
simple_answer= pd.DataFrame(summary_dict)

def get_max_list(data):
    return max(len(v) for k, v in data.items())

# Test functions
def test_data_type():
    """
    Test that the function returns an error if 
    the input type is incorrect
    """
    with pytest.raises(NotImplementedError):
        sm.summary("Input Data")
        sm.summary([1, 2, 3, 4, 5])
        sm.summary(True)
        sm.summary((True, "False"))
        sm.summary({"x":[1,2], "y":[3,4]})
        
def test_output_type():
    """
    Test that the output type must be a nested dataframe 
    """
    assert type(sm.summary(toy_data)) == pd.DataFrame
    assert type(sm.summary(toy_all_na)) == pd.DataFrame
    assert type(sm.summary(toy_no_na)) == pd.DataFrame
    assert type(sm.summary(toy_mixed_strings)) == pd.DataFrame 
    
def test_output_shape():
    """
    Test that output has the correct shape
    """
    assert get_max_list(sm.summary(toy_data)) <= toy_data.shape[0]
    assert get_max_list(sm.summary(toy_all_na)) <= toy_all_na.shape[0]
    assert get_max_list(sm.summary(toy_no_na)) <= toy_no_na.shape[0]
    assert len(sm.summary(toy_data)) <= toy_data.shape[1]
    assert len(sm.summary(toy_all_na)) <= toy_all_na.shape[1]
    assert len(sm.summary(toy_no_na)) <= toy_no_na.shape[1]
    
def test_summary_stats():
    '''
    Test that the summary statistics for numeric and categorical data are correct 
    '''
    assert sm.summary(simple_data) == simple_answer
    