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
    
        
# toy_data_tbl <- tribble(
#   ~x, ~y,  ~z,
#   NA, 2,  3.6,
#   "b", NA, 8.5,
#   "c", NA, NA
# )
# toy_data_df <- as.data.frame(toy_data_tbl)
# toy_all_na <- tibble(x = c(NA,NA,NA), y = c(NA,NA,NA), z = c(NA, NA, NA))
# toy_no_na <- tibble(x = c(1,2,3,4), y = c(5,6,7,8))

# test_that("Test that input data is a tbl or data.frame", {
#   expect_error(locate_na("Input Data"), "Input is not a tibble or data.frame")
#   expect_error(locate_na(c(1:10)), "Input is not a tibble or data.frame")
#   expect_error(locate_na(list(1:3)), "Input is not a tibble or data.frame")
#   expect_error(locate_na(TRUE), "Input is not a tibble or data.frame")
# })

# test_that("Test valid output format", {
#   expect_is(locate_na(toy_tbl), "list")
#   expect_is(locate_na(toy_data_df), "list")
# })

# test_that("Test for correct functionality of the function", {
#   toy_result <- list(x=c(1), y=c(2,3), z=c(3))
#   all_na_result <- list(x=c(1,2,3), y=c(1,2,3), z=c(1,2,3))
#   no_na_result <- list(x=c(0), y=c(0))

#   expect_equal(locate_na(toy_data_tbl), toy_result)
#   expect_warning(locate_na(toy_all_na), "All values are missing.")
#   expect_warning(locate_na(toy_no_na), "No NAs are in the input data.")
# })