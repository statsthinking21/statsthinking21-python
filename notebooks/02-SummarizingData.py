# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Summarizing Data
#

# %% [markdown]
# This chapter will introduce you to how to summarize data using data frames in Pandas.

# %% [markdown]
# Before doing anything else we need to import the packages that we will use in this chapter.  

# %%
import pandas as pd
import numpy as np

# %% [markdown]
# ## Working with data frames

# %% [markdown]
# In the last chapter you were introduced to the concept of a *data frame*, which we will use throughout much of this book.  
# In particular, we will use a dataset known as [NHANES](https://www.cdc.gov/nchs/nhanes/index.htm) for several of our examples, so let's load the library that provides us access to the data.
# This is a large dataset collected from a sample of individuals in the United States every two years, which measures many different aspects of their health and lifestyles.
# To access the data, we will use a Python package called [nhanes](https://github.com/poldrack/nhanes) that contains a function to load a cleaned-up version of the dataset. 

# %%
from nhanes.load import load_NHANES_data
nhanes_data = load_NHANES_data()

# %% [markdown]
# We can use the ``.head()`` method to look inside the data frame:

# %%
nhanes_data.head()

# %% [markdown]
# Let's look at the structure of this dataset.  We can see the *shape* of the data frame -- that is, the number of rows and columns -- using the ``.shape`` method:

# %%
nhanes_data.shape

# %% [markdown]
# We see that the dataset has many more rows than columns. Let's look more closely at what is contained in the rows and columns.  To obtain the labels for the rows, we use the ``.index`` operator:

# %%
nhanes_data.index

# %% [markdown]
# The index contains a bunch of numbers, each of which refers to one of the individuals in the NHANES data set.  In a data frame, the rows always refer to *observations*, by which mean that each row reflects an individual unit of data.  In the case of a dataset like NHANES, the observations would usually refer to individual people, though as we will see later, we sometimes want the rows to be even more specific.
# We can also look at the content of the columns, which we can access using the ``.columns`` operator:

# %%
nhanes_data.columns

# %% [markdown]
# Each of the columns contains a different *variable* -- that is, a different thing that is measured on each observation.


# %% [markdown]
# ### Selecting rows (observations) and columns (variables)

# %% [markdown]
# We often want to select a subset of rows from a data frame. You saw in the last chapter how we can access specific rows using the ``.loc`` operator.  This operator requires us to refer to the row names (that is, the *index*) and column names.  For example, if we wanted to know the value of the `GeneralHealthCondition` variable for the indivdiual labeled 93707, we could use the following:

# %%
nhanes_data.loc[93707, 'GeneralHealthCondition']

# %% [markdown]
# If there were several variables that we wanted to see for this individual, we could include the names of those variables in a *list*:

# %%
nhanes_data.loc[93707, ['GeneralHealthCondition', 'Gender', 'AgeInYearsAtScreening']]

# %% [markdown]
# This shows us the values for each of those variables for this individual. We could also do the same if there were several individuals that we were interested in:

# %%
nhanes_data.loc[[102951, 102955, 93707], ['GeneralHealthCondition', 'Gender', 'AgeInYearsAtScreening']]

# %% [markdown]
# ### Missing values

# %% [markdown]
# You will notice that the `GeneralHealthCondition` variable for the first individual in the previous cell contained *NaN*, which stands for "not a number".  This is generally used to denote that the data are missing for this particular observation; perhaps they declined to answer the question, or the interviewer failed to properly record the answer.  Missing data are common when we are working with real data.  There are many sophsticated ways to deal with missing data in statistics, but for the moment we will just remove observations that have a missing data on one of our variables of interest, which we can do using the `.dropna()` operator:

# %%
my_subset = nhanes_data.loc[[102951, 102955, 93707], ['GeneralHealthCondition', 'Gender', 'AgeInYearsAtScreening']]
my_subset.dropna()

# %% [markdown]
# This operator removes any rows that have missing values for any of the variables in the data frame.


# %% [markdown]
# ### Selecting rows by value

# %% [markdown]
# Let's say that we want to analyze NHANES data, but only for those individuals who are over 50 years of age.  We can use the `query` operator on a data frame to find rows that match particular conditions:

# %%
over_50_df = nhanes_data.query('AgeInYearsAtScreening >= 50')
over_50_df.shape

# %% [markdown]
# This shows that there were 2898 observations that matched our criterion.  We can also search for specific values: For example, let's say that we want to find anyone who reported that their general health condition was "Good".  This one is a bit tricky, because we are searching for a string of text, which we have to embed in our query, which is also a string of text.  Fortunately, there are two different quotation marks that we can use (`'` or `"`) and Python treats them as distinct operators, so we can surround our text within double quotes, inside a string surrounded by single quotes:

# %%
good_health_df = nhanes_data.query('GeneralHealthCondition == "Good"')
good_health_df.shape

# %% [markdown]
# ## Creating new variables

# %% [markdown]
# We can add a new variable to a data frame easily, by simply giving it a new name. Let's say that we wanted to convert the weight value in NHANES (stored in the `WeightKg` variable) from kilograms to pounds.  

# %%
nhanes_data['WeightLbs'] = nhanes_data['WeightKg'] * 2.205

# %% [markdown]
# This shows another way to refer to a particular variable in a dataframe: simply put its name in square brackets.  Pandas also has the ability to replace particular values in a variable.  First, let's look at the values of the `Gender` variable in the data frame, to see what values it takes. We can see all of the unique values of a variable using the `.unique()` operator:

# %%
nhanes_data['Gender'].unique()

# %% [markdown]
# Now let's say that we wanted to recode the `Gender` variable so that instead of "Female" and "Male" its values were "F" and "M".  One way to do this would be to use the `.rename()` operator on the data frame:


# %%
nhanes_data['GenderMF'] = nhanes_data['Gender'].replace({'Female': 'F', 'Male': 'M'})
nhanes_data['GenderMF'].unique()


# %% [markdown]
# ### Understanding your data

# %% [markdown]
# Let's say that we want to learn more about the variable labeled `GeneralHealthCondition` in the dataset.  We can load some information about that variable using the `open_variable_page()` function from the `nhanes` package:

# %%
from nhanes.load import open_variable_page
open_variable_page('GeneralHealthCondition')

# %% [markdown]
# This shows us the question that was asked ("Would you say {your/SP's} health in general is...").

# %% [markdown]
# ## Summarizing data using a frequency distribution

# %% [markdown]
# Let's say that we want to know the frequencies of all of the different answers to the GeneralHealthCondition question.  We can do this using the `.value_counts()` method of the data frame:

# %%
nhanes_data['GeneralHealthCondition'].value_counts()

# %% [markdown]
# It's usually more helpful to present a *relative frequency distribution*, which shows proportions rather than counts.  We can obtain that by simply dividing the frequency distribution by the total number of cases, which we can obtain using the `.sum()` operator:

# %%
GeneralHealthCondition_frequency_dist = nhanes_data['GeneralHealthCondition'].value_counts()
GeneralHealthCondition_frequency_dist / GeneralHealthCondition_frequency_dist.sum()


# %% [markdown]
# ### Data Cleaning

# %% [markdown]
# When we work with real data, they often have problems that we have to fix before we can analyze them properly.  An example is the `GeneralHealthCondition` variable that we worked with in the previous example. You may have noticed that the values of the variable had some extranous information, which were held over from the way that the question is worded (including "Fair or" and "Poor?").  We can clean these up by replacing the problematic values using the `.replace()` method:

# %%
nhanes_data['GeneralHealthConditionFixed'] = nhanes_data['GeneralHealthCondition'].replace({'Fair or': 'Fair', 'Poor?': 'Poor'})
nhanes_data['GeneralHealthConditionFixed'].unique()

# %% [markdown]
# Now let's look at a more complex example.  Let's say that we want to know who is currently a smokker in the NHANES sample.  If we look more closely at the [details of the smoking questionnaire](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/SMQ_J.htm), we will see that not all individuals got the same questions; for example, if a person said that they had not smoked more than 100 cigarettes in their life (recorded in the `SmokedAtLeast100CigarettesInLife` variable), then they were not asked the question about whether they currently smoked cigarettes (stored as `DoYouNowSmokeCigarettes`).  We can see this in the number of respondents to each question:

# %%
print(nhanes_data['SmokedAtLeast100CigarettesInLife'].value_counts())

# %%
nhanes_data['DoYouNowSmokeCigarettes'].value_counts()

# %% [markdown]
# Looking at these two variables, it's plain to see that there are many more values included in the first question than in the second. Let's look at bit more closely at the data to see what's going on:

# %%
nhanes_data[['SmokedAtLeast100CigarettesInLife', 'DoYouNowSmokeCigarettes']].head(10)

# %% [markdown]
# Here we can see that anyone who said No to the question about having smoked at least 100 cigarettes in their life (which is coded as zero) has a missing value for the question about current smoking (since that question wasn't asked to these individuals).  To clean up these data, we need to do two things. First, we need to remove the individuals who have NaN for both questions, then we need to recode the NaN's for the second question for those people who said no on the first question.  To do this, let's first create a new data frame that contains just the variables we are interested in:

# %%
smoking_df = nhanes_data[['SmokedAtLeast100CigarettesInLife', 'DoYouNowSmokeCigarettes']]
smoking_df.shape

# %% [markdown]
# First let's remove any rows that have NaN in both columns. We can do this using the `.dropna()` method, which has an option that allows us to specify that we only drop rows that are all NaN (by setting `how='all'`):

# %%
smoking_df = smoking_df.dropna(how='all')
smoking_df.shape

# %% [markdown]
# Next we need to recode the NaN values for the second question, for those individuals who said no to the first question.  We will replace them with the answer 'Not at all'.  To do this, we can use the `.loc` operator with a test for the value of the first column:

# %%
smoking_df.loc[smoking_df['SmokedAtLeast100CigarettesInLife']==0, 'DoYouNowSmokeCigarettes'] = 'Not at all'
smoking_df.head()

# %% [markdown]
# This replaced the NaN values in the second question, but only for those individuals who said no to the first question.  Now we can summarize the frequency of smoking across the entire group:

# %%
smoking_df['DoYouNowSmokeCigarettes'].value_counts() / smoking_df['DoYouNowSmokeCigarettes'].value_counts().sum()

# %% [markdown]
# In the next chapter you will learn how to visualize data like these using statistical graphs.

