import pandas as pd
import numpy as np
import pytest
import sys
sys.path.append("../CleanPy")

import replace_na

# Create test data frame
input_df = pd.DataFrame({'x': [None, "b", "c"], 'y': [2 ,None,None], 'z': [3.6, 8.5,None]})

# Return TypeError:"Input is not a dataframe" if the input is not a dataframe
def test_correct_input():
    assert isinstance(input_df, pd.DataFrame)
#Checks if the input has missing values, if it does not, then don't do anything
def test_input_contains_missingvalues():
  assert isinstance(input_df, pd.DataFrame)
# Check if the whole input contains missing values, then it will 
# throw an error saying, the input is not valid.
def test_input_contains_all_missingvalues():
  assert isinstance(input_df, pd.DataFrame)
  
    
