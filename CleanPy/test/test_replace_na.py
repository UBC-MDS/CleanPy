import pandas as pd
import numpy as np
import pytest
import sys
sys.path.append("../")

import replace_na as rp

# Helper codes
toy_data = pd.DataFrame({"x":[None, 4, 6], "y": [2, None, None], "z": [3.6, 8.5, None]})
toy_all_na = pd.DataFrame({"x":[None, None, None], "y": [None, None, None], "z": [None, None, None]})
toy_no_na = pd.DataFrame({"x":[1, 2, 3, 4], "y": [1, 2, 3, 4], "z": [1, 2, 3, 4]})

# Test data type
print (toy_data)

def test_correct_input():
    """
    Test that the function returns an error if 
    the input type is wrong
    """
    with pytest.raises(TypeError):
        rp.replace_na("Input Data")
        rp.replace_na([1, 2, 3, 4, 5])
        rp.replace_na(True)
        rp.replace_na((True, "False"))
        rp.replace_na({"x":[1,2], "y":[3,4]})
        
# Test output type

def test_output_type():
    """
    Test that the output type is also a  dataframe 
    """
    columns_1 = toy_data.columns.values
    columns_2 = toy_all_na.columns.values
    columns_3 = toy_no_na.columns.values
    assert type(rp.replace_na(toy_data, columns_1)) == pd.DataFrame
  
    assert type(rp.replace_na(toy_no_na, columns_3)) == pd.DataFrame
    
# Test for the functionality of the function

def test_functionality():
    """
    Test for the correct functionality of the function
    """
    toy_result = pd.DataFrame({"x":[5,4,6], "y":[2,2,2], "z":[3.6,8.5,6.05]})
    all_na_result = pd.DataFrame({"x":[0,0,0], "y":[0,0,0], "z":[0,0,0]})
    no_na_result = pd.DataFrame({"x":[1, 2, 3, 4], "y": [1, 2, 3, 4], "z": [1, 2, 3, 4]})
    columns_1 = toy_data.columns.values
    columns_2 = toy_all_na.columns.values
    columns_3 = toy_no_na.columns.values
    a = rp.replace_na(toy_data, columns_1) == toy_result
    c = rp.replace_na(toy_no_na, columns_3) == no_na_result
    assert a.all(axis = None)
    assert c.all(axis = None)

# If the data frame contains all missing values(NAs)
columns_2 = toy_all_na.columns.values
def test_input_contains_all_missingvalues():
    with pytest.raises(TypeError):
          rp.replace_na(toy_all_na, columns_2)
    
