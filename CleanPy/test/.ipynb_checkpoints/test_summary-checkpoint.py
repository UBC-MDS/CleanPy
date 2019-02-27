import pandas as pd
import numpy as np
import pytest
import sys
sys.path.append("../../")

import cleanpy as sm

# Helper codes
toy_data = pd.DataFrame({"x":[None, "b", "c"], "y": [2, None, None], "z": [3.6, 8.5, None]})
toy_all_na = pd.DataFrame({"x":[None, None, None], "y": [None, None, None], "z": [None, None, None]})
toy_no_na = pd.DataFrame({"x":[1, 2, 3, 4], "y": [1, 2, 3, 4], "z": [1, 2, 3, 4]})
toy_mixed_strings= pd.DataFrame({"x":[1,3,4,5], "y": ["Female", "Female", "Male", "man"]})
toy_mixed_data_type = pd.DataFrame({"x":[1,3,4,5], "y": ["Female", "Female", "Male", 22]}) #typo is 22
numeric_data = pd.DataFrame({"y": [2, None, None], "z": [3.6, 8.5, 10]})

simple_data = pd.DataFrame({"x":["a", "b", None], "y": [None, 1, 3]})
dict1= {"Unique":simple_data["x"].unique(), "count" : 2, "count_NAs": 1, "count_unique": 2, "max_": np.nan, "mean": np.nan, "median": np.nan, "min_": np.nan}
dict2= {"Unique":simple_data["y"].unique(), "count" : 2, "count_NAs": 1, "count_unique": 3, "max_": 3, "mean": 2, "median": 2, "min_": 1}
summary_dict = {"x": dict1, "y": dict2}
simple_answer= pd.DataFrame(summary_dict)


# Test functions
def test_data_type():
    """
    Test input data type, and that the function returns an error if 
    the input type is incorrect
    """
    with pytest.raises(NotImplementedError):
        sm.summary("Input Data")
        sm.summary([1, 2, 3, 4, 5])
        sm.summary(True)
        sm.summary((True, "False"))
        #sm.summary({"x":[1,2], "y":[3,4]})
        
def test_output_type():
    """
    Test that the output type must be a dataframe 
    """
    assert type(sm.summary(toy_data)) == pd.core.frame.DataFrame
    assert type(sm.summary(toy_all_na)) == pd.core.frame.DataFrame
    assert type(sm.summary(toy_no_na)) == pd.core.frame.DataFrame
    assert type(sm.summary(toy_mixed_strings)) == pd.core.frame.DataFrame 
    
def test_output_shape():
    """
    Test that output has the correct shape. Can't have more output columns than data input columns
    """
    assert sm.summary(toy_data).shape[1] <= toy_data.shape[1]
    assert sm.summary(toy_all_na).shape[1] <= toy_all_na.shape[1]
   
    
def test_summary_stats():
    '''
    Test that the summary statistics for numeric and categorical data are correct 
    '''
    pd.util.testing.assert_frame_equal(sm.summary(simple_data), simple_answer)
    