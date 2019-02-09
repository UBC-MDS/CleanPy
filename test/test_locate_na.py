import pandas as pd
import numpy as np
import pytest
import sys
sys.path.append("../CleanPy")

import CleanPy as cp

# Return TypeError if type is incorrect
def test_data_type():
    with pytest.raise(TypeError):

