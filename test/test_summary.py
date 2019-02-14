import pandas as pd
import numpy as np
import pytest
import sys
sys.path.append("../CleanPy")

import summary

# Helper codes
toy_data = pd.DataFrame({"x":[None, "b", "c"], "y": [2, None, None], "z": [3.6, 8.5, None]})
toy_all_na = pd.DataFrame({"x":[None, None, None], "y": [None, None, None], "z": [None, None, None]})
toy_no_na = pd.DataFrame({"x":[1, 2, 3, 4], "y": [1, 2, 3, 4], "z": [1, 2, 3, 4]})
toy_mixed_strings= pd.DataFrame({"x":[1,3,4,5], "y": ["Female", "Female", "Male", "man"]})
toy_mixed_data_type = pd.DataFrame({"x":[1,3,4,5], "y": ["Female", "Female", "Male", 22]}) #typo is 22

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
    assert type(cp.summary(toy_all_na)) == pd.DataFrame
    assert type(cp.summary(toy_no_na)) == pd.DataFrame
    
def test_output_shape():
    """
    Test that output is a nested dataframe
    """
    assert get_max_list(cp.summary(toy_data)) <= toy_data.shape[0]
    assert get_max_list(cp.summary(toy_all_na)) <= toy_all_na.shape[0]
    assert get_max_list(cp.summary(toy_no_na)) <= toy_no_na.shape[0]
    assert len(cp.summary(toy_data)) <= toy_data.shape[1]
    assert len(cp.summary(toy_all_na)) <= toy_all_na.shape[1]
    assert len(cp.summary(toy_no_na)) <= toy_no_na.shape[1]
    