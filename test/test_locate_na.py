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

def get_max_list(data):
    return max(len(v) for k, v in data.items())

# Test functions
def test_data_type():
    """
    Thest that the function returns an error if 
    the input type is incorrect
    """
    with pytest.raises(TypeError):
        cp.locate_na("Input Data")
        cp.locate_na([1, 2, 3, 4, 5])
        cp.locate_na(True)
        cp.locate_na((True, "False"))
        cp.locate_na({"x":[1,2], "y":[3,4]})
        
def test_output_type():
    """
    Test that the output type must be a dictionary 
    """
    assert type(cp.locate_na(toy_data)) == dict
    assert type(cp.locate_na(toy_all_na)) == dict
    assert type(cp.locate_na(toy_no_na)) == dict
    
def test_output_shape():
    """
    Test that output cannot have have more rows and 
    columns than the original input data
    """
    assert get_max_list(cp.locate_na(toy_data)) <= toy_data.shape[0]
    assert get_max_list(cp.locate_na(toy_all_na)) <= toy_all_na.shape[0]
    assert get_max_list(cp.locate_na(toy_no_na)) <= toy_no_na.shape[0]
    assert len(cp.locate_na(toy_data)) <= toy_data.shape[1]
    assert len(cp.locate_na(toy_all_na)) <= toy_all_na.shape[1]
    assert len(cp.locate_na(toy_no_na)) <= toy_no_na.shape[1]
    
def test_functionality():
    """
    Test for the correct functionality of the function
    """
    toy_result = {"x":[0], "y":[1,2], "z":[2]}
    all_na_result = {"x":[0,1,2], "y":[0,1,2], "y":[0,1,2]}
    no_na_result = {}
    
    assert cp.locate_na(toy_data) = toy_result
    assert cp.locate_na(toy_all_na) = all_na_result
    assert cp.locate_na(toy_no_na) = no_na_result
