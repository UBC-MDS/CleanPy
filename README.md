# CleanPy
This package cleans a dataset and returns summary statistics as well as number, proportion and location of NA values for string and number column inputs. Data cleaning made easy!

### Collaborators
Heather Van Tassel, Phuntsok Tseten, Patrick Tung

## Overview
There is a dire need for a good data cleaning package, and we are trying to develop our version of a good data cleaning package that will help users clean their data in a meaningful way. Data cleaning is usually the first step in any data science problem, and if you don’t clean your data well, it might be really difficult to proceed further. So our motivation for coming up with this idea was to address this very issue of messy data.

CleanPy is especially developed to create a streamlined process to give you an easy to read summary statistics table about your data. CleanPy is able to easily locate all the missing data for you and allow you to locate where exactly it occurs. Not only are you able to locate missing data, you can also define how you would like to deal with your missing data. 

## Functions
**Function 1)**


**Function 2)** `locate_na`: Returns a dataframe of the count and indices of NA values.  This function takes in a dataframe and finds NA values and returns the location of these values along the count of total NAs.

```
def locate_na(data):
"""Locate and return the indices to all missing values within an inputted dataframe.
   Parameters
   ----------
   data : dataframe
      This is the dataframe that the function will use to locate NAs.
      
   Returns
   -------
   List of tuples
   Each tuple in the list represents a the indices of a missing value in the dataframe. 
   >>> locate_na(pd.DataFrame(np.array([[“Yes”, “No”], [“”, “Yes”]])))
   [(1, 0)]
   >>> locate_na(pd.DataFrame(np.array([[“Yes”, “No”, “”], [“”, “Yes”, “Yes”]])))
   [(0, 2), (1, 0)]
"""
```

**Function 3)** `replace_na`:Replaces missing NA values with either min, max, median, or average (default) values of the column(s). There will be an option to remove the rows with NAs.

```
def replace_na(data replace=’min’, ‘max’, ‘median’, ‘average’, ‘remove’ , diff_columns=list of replace values in order of columns):

"""
This function replaces na values with either the min, max, median or average value or removes the
rows

"""
Parameters
   ----------
   data : dataframe
      This is the dataframe that the function will use to replace NAs.
      
   Returns
   -------
   A list of tuples where each NAs will be replaced by either min, max, median or average.
   Each tuple in the list represents  the indices of a NA in the dataframe. 
   >>> replace_na(pd.DataFrame(np.array([[“Yes”, “No”], [“”, “Yes”]])))
   [(min, max, median, average)]
  
"""
```


## CleanPy and Python's Ecosystem

## Installation
*Will be developed next milestone*

## Package Dependencies
- Pandas
- Numpy

