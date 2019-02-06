# Milestone 1


## Functions & Test Cases
**Function 1)** Summary statistics generator for text and integer data from dataframes.
Def summary(input_df, zero_include=TRUE):
```
   Parameters
    ----------
    input_df : dataframe
        This is the dataframe that the function will use to provide summary statistics of each column in the data frame. It will determine the main data type of the column by calculated the type of each row entry in the column, and using the most frequent data type as the expected input for that column. It will perform two different summary statistics based on 2 different groups of datatypes of either 1) string or 2) int/float. For number columns it returns a dictionary of summary statistics including mean value for each column, min, max, count (number of non NA values per column) and count_NA (number of NA values per column). Similarly, for string columns it returns the unique string values and their counts in a dictionary. It will also provide a count of NA values which will include empty strings, and anything other than the correct data type for each column. The column names are the keys, and 
 .

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

Dataframe %>%
For colname in dataframe[columns]:
If column data type is string: 
summarise(unique(n),
    count=  ) countvectorizer or output word cloud
df= 
Elseif column data type is float or int:
summarise(total.count=n(),
  count=sum(is.na(colname)),
  avg.col[i]=mean(colname,na.rm=TRUE),
  max.col[i]=max(colname, na.rm=TRUE)
  Min =
  Median =
  df=
Return multiple data frames 

Test cases: 
1) The input data must be a dataframe. Otherwise, the function will return an error message “input_df must be a dataframe”
Data columns should have one datatype. If datatype is mostly strings, return summary statistics for strings. 
2) If datatype is mostly numbers, return summary statistics for numbers 
3) If all columns are floats, return summary statistics with floats
4) If all columns are integers, return summary statistics with integers
5) If some columns are integers, and some are floats, return summary statistics using each columns data type
6) If one column has a mixture of data types (strings, floats or ints) return summary statistics by converting all entries into the predominant datatype
7) If a column contains any entries that are not of the type string float or int, return error message “This function only handles strings, floats and integer data types”



**Function 2)** `locate_na`: Returns a dataframe of the count and indices of NA values.  This function takes in a dataframe and finds NA values and returns the location of these values along the count of total NAs.

```
def locate_na(input_df):
"""Locate and return the indices to all missing values within an inputted dataframe.

   Parameters
   ----------
   input_df : dataframe
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

*Test cases for `locate_na`*:
- If `data` is not of type dataframe, the function will return an error telling the user that the input data is not a dataframe.
- Dataframe with 0 NAs should return an empty list with no NA indices.
- Dataframe with 1 NA should return a list with the indices of the NA. 

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

*Test cases for `replace_na`*:
- If `data` is not of type dataframe, the function will return an error telling the user that the input data is not a dataframe.
- Dataframe with 0 NAs should not do anything.
- Dataframe with NA should be replaced by either the mean, max, median or average
- If everthing in the data frame in NA, it will throw a warning that the input is not valid.






