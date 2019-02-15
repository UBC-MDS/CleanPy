# CleanPy
This package cleans a dataset and returns summary statistics as well as number, proportion and location of NA values for string and number column inputs. Data cleaning made easy!

### Collaborators
Heather Van Tassel, Phuntsok Tseten, Patrick Tung

## Overview
There is a dire need for a good data cleaning package, and we are trying to develop our version of a good data cleaning package that will help users clean their data in a meaningful way. Data cleaning is usually the first step in any data science problem, and if you don’t clean your data well, it might be really difficult to proceed further. So our motivation for coming up with this idea was to address this very issue of messy data.

CleanPy is especially developed to create a streamlined process to give you an easy to read summary statistics table about your data. CleanPy is able to easily locate all the missing data for you and allow you to locate where exactly it occurs. Not only are you able to locate missing data, you can also define how you would like to deal with your missing data. 

## Function
**Function 1)** `summary`: Summary statistics generator for string and numeric data from dataframes.
```
def summary(data, zero_include=TRUE):
"""
    Parameters
    ----------
    data : dataframe
        This is the dataframe that the function will use to provide summary statistics of each column in the data frame. It will determine the main data type of the column by calculated the type of each row entry in the column, and using the most frequent data type as the expected input for that column. It will perform two different summary statistics based on 2 different groups of datatypes of either 1) string or 2) int/float. For number columns it returns a dictionary of summary statistics including mean value for each column, min, max, count (number of non NA values per column) and count_NA (number of NA values per column). Similarly, for string columns it returns the unique string values and their counts in a dictionary. It will also provide a count of NA values which will include empty strings, and anything other than the correct data type for each column. The column names are the keys.
    
    Returns
    -------
    Summary table of each columns summary statistics
    
    >>> summary(pd.DataFrame(colnames=”Likes coding”, rows= np.array([[4,3,2, 2])))
    pd.DataFrame(col1, values=
        min= 2
        max= 4
        mean= 11/4
        median= 2
        count=4
        count_NA=0
"""
```

**Function 2)** `locate_na`: Returns a dataframe of the count and indices of NA values. This function takes in a dataframe and finds NA values and returns the location of these values along the count of total NAs.

```
def locate_na(data):
    """ 
    Locate and return the indices to all missing values within an inputted dataframe. 
    Each element of the returned dictionary will be a column in a dataframe, which will 
    contain the row indices of the missing values.
    
    Parameters
    ----------
    data : dataframe
        This is the dataframe that the function will use to locate NAs.
        
    Returns
    -------
    dictionary of lists 
        key = column indices that contain missing values
        value = list of row indices that have missing values
        
    >>> locate_na(pd.DataFrame(np.array([[“Yes”, “No”], [None, “Yes”]])))
    {"0": [1]}
    >>> locate_na(pd.DataFrame(np.array([[1, 2, None], [None, 2, 3]])))
    {"0": [1], "2": [0]}
    """
```

**Function 3)** `replace_na`:Replaces missing values with either min, max, median, or average (default) values of the column(s). There will be an option to remove the rows with NAs.

```
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
        values include: "mean", "min", "max", "median"
    
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
```


## CleanPy and Python's Ecosystem
Sometimes, it can get quite annoying  to go through your data line by line, and a quick summary of the data, will not only save you a lot of time but also give you a quick insight and overall picture of your data, which can be very useful to understand the task at hand. Python has a summary function called  `describe()` function from Python's `pandas.DataFrame`. CleanPy's `summary()` function will be quite similar to `describe()` but it will take it a step further and generate summary statistics, which will be presented in a very intuitive manner. The `summary()` function will also provide more information such as the number of missing values, and summaries of string information. In regards to our `locate_na()` and `replace_na()`, there is no similar function in existence in the current Python ecosystem that we are aware of. The only way to do them is to mannually combine a few functions including `pandas.DataFrame.isna()`.

## Installation
`CleanPy` can be installed using the `pip`
```
pip install git+https://github.com/UBC-MDS/CleanPy.git
```

Then you can import our packages using:
```
from CleanPy import summary, locate_na, replace_na
```

## Python Dependencies
- Pandas
- Numpy
