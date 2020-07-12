# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Summarizing Data
#

# This chapter will introduce you to how to summarize data using data frames in Pandas.

# Before doing anything else we need to import the packages that we will use in this chapter.  

import pandas as pd
import numpy as np

# ## Working with data frames

# In the last chapter you were introduced to the concept of a *data frame*, which we will use throughout much of this book.  
# In particular, we will use a dataset known as [NHANES](https://www.cdc.gov/nchs/nhanes/index.htm) for several of our examples, so let's load the library that provides us access to the data.
# This is a large dataset collected from a sample of individuals in the United States every two years, which measures many different aspects of their health and lifestyles.
# To access the data, we will use a Python package called [nhanes](https://github.com/poldrack/nhanes) that contains a function to load a cleaned-up version of the dataset. 

from nhanes.load import load_NHANES_data
nhanes_data = load_NHANES_data()

# We can use the ``.head()`` method to look inside the data frame:

nhanes_data.head()

# Let's look at the structure of this dataset.  We can see the *shape* of the data frame -- that is, the number of rows and columns -- using the ``.shape`` method:

nhanes_data.shape

# We see that the dataset has many more rows than columns. Let's look more closely at what is contained in the rows and columns.  To obtain the labels for the rows, we use the ``.index`` operator:

nhanes_data.index

# The index contains a bunch of numbers, each of which refers to one of the individuals in the NHANES data set.  In a data frame, the rows always refer to *observations*, by which mean that each row reflects an individual unit of data.  In the case of a dataset like NHANES, the observations would usually refer to individual people, though as we will see later, we sometimes want the rows to be even more specific.
# We can also look at the content of the columns, which we can access using the ``.columns`` operator:

nhanes_data.columns

# Each of the columns contains a different *variable* -- that is, a different thing that is measured on each observation.


# ### Selecting rows (observations) and columns (variables)

# We often want to select a subset of rows from a data frame. You saw in the last chapter how we can access specific rows using the ``.loc`` operator.  This operator requires us to refer to the row names (that is, the *index*) and column names.  For example, if we wanted to know the value of the `GeneralHealthCondition` variable for the indivdiual labeled 93707, we could use the following:

nhanes_data.loc[93707, 'GeneralHealthCondition']

# If there were several variables that we wanted to see for this individual, we could include the names of those variables in a *list*:

nhanes_data.loc[93707, ['GeneralHealthCondition', 'Gender', 'AgeInYearsAtScreening']]

# This shows us the values for each of those variables for this individual. We could also do the same if there were several individuals that we were interested in:

nhanes_data.loc[[102951, 102955, 93707], ['GeneralHealthCondition', 'Gender', 'AgeInYearsAtScreening']]

# ### Missing values

# You will notice that the `GeneralHealthCondition` variable for the first individual in the previous cell contained *NaN*, which stands for "not a number".  This is generally used to denote that the data are missing for this particular observation; perhaps they declined to answer the question, or the interviewer failed to properly record the answer.  Missing data are common when we are working with real data.  There are many sophsticated ways to deal with missing data in statistics, but for the moment we will just remove observations that have a missing data on one of our variables of interest, which we can do using the `.dropna()` operator:

my_subset = nhanes_data.loc[[102951, 102955, 93707], ['GeneralHealthCondition', 'Gender', 'AgeInYearsAtScreening']]
my_subset.dropna()

# This operator removes any rows that have missing values for any of the variables in the data frame.


# ### Selecting rows by value

# Let's say that we want to analyze NHANES data, but only for those individuals who are over 50 years of age.  We can use the `query` operator on a data frame to find rows that match particular conditions:

over_50_df = nhanes_data.query('AgeInYearsAtScreening >= 50')
over_50_df.shape

# This shows that there were 2898 observations that matched our criterion.  We can also search for specific values: For example, let's say that we want to find anyone who reported that their general health condition was "Good".  This one is a bit tricky, because we are searching for a string of text, which we have to embed in our query, which is also a string of text.  Fortunately, there are two different quotation marks that we can use (`'` or `"`) and Python treats them as distinct operators, so we can surround our text within double quotes, inside a string surrounded by single quotes:

good_health_df = nhanes_data.query('GeneralHealthCondition == "Good"')
good_health_df.shape

# ## Creating new variables

# We can add a new variable to a data frame easily, by simply giving it a new name. Let's say that we wanted to convert the weight value in NHANES (stored in the `WeightKg` variable) from kilograms to pounds.  

nhanes_data['WeightLbs'] = nhanes_data['WeightLbs'] * 2.205

# This shows another way to refer to a particular variable in a dataframe: simply put its name in square brackets.  Pandas also has 
