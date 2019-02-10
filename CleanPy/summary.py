#!/usr/bin/env python
# coding: utf-8

# In[7]:


#!/usr/bin/env python

def summary(input_df, zero_include=True):
    '''
    Parameters
    ----------
    input_df : dataframe
        This is the dataframe that the function will use to provide summary statistics of each column in the data frame. It will determine the main data type of the column by calculated the type of each row entry in the column, and using the most frequent data type as the expected input for that column. It will perform two different summary statistics based on 2 different groups of datatypes of either 1) string or 2) int/float. For number columns it returns a dictionary of summary statistics including mean value for each column, min, max, count (number of non NA values per column) and count_NA (number of NA values per column). Similarly, for string columns it returns the unique string values and their counts in a dictionary. It will also provide a count of NA values which will include empty strings, and anything other than the correct data type for each column. The column names are the keys, and 
 .

    Returns
    -------
    Summary table of each columns summary statistics
    
    >>> summary(pd.DataFrame(colnames=”Likes coding”, rows= np.array([[4,3,2, 2])))
       pd.DataFrame(col1: 
       min= 2
       max= 4
       mean= 11/4
       median= 2
       count=4
       count_NA=0
    '''
    return 


# In[ ]:




