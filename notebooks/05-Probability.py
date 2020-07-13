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
# # Probability
# In this chapter we will go over how to perform probability computations in Python.
#
# ## Basic probability calculations
#
# Let's create a vector of outcomes from one to 6, using the `np.arange()` function to create such a sequence.  This function takes the minimum and maximum values as its inputs, but note that the maximum is not included in the sequence; that is, the sequence goes up to but not including the maximum.  Thus, we would have to give 1 and 7 as the minimum and maximum in order to get a sequence of numbers from 1 to 6:

# %%
import numpy as np
outcomes = np.arange(1, 7)
outcomes

# %% [markdown]
# Now let's create a vector of logical values based on whether the outcome in each position is equal to 1. Remember that `==` tests for equality of each element in a vector:

# %%
outcome1isTrue = outcomes == 1 
outcome1isTrue

# %% [markdown]
# Remember that the simple probability of an outcome is number of occurrences of the outcome divided by the total number of events.  To compute a probability, we can take advantage of the fact that TRUE/FALSE are equivalent to 1/0 in Python.  The formula for the mean (sum of values divided by the number of values) is thus exactly the same as the formula for the simple probability!  So, we can compute the probability of the event by simply taking the mean of the logical vector.

# %%
p1isTrue = np.mean(outcome1isTrue)
p1isTrue

# %% [markdown]
# ## Empirical frequency (Section \@ref(empirical-frequency))
# Let's walk through how [we computed empirical frequency of rain in San Francisco](https://statsthinking21.github.io/statsthinking21-core-site/probability.html#empirical-frequency).
#
# First we load the data:

# %%
#+
import pandas as pd
SFrain = pd.read_csv('https://raw.githubusercontent.com/statsthinking21/statsthinking21-python/master/notebooks/data/SanFranciscoRain.csv')

# we will remove the STATION and NAME variables 
# since they are identical for all rows

SFrain = SFrain.drop(columns=['STATION', 'NAME'])
SFrain
#-

# %% [markdown]
# We see that the data frame contains a variable called `PRCP` which denotes the amount of rain each day. Let's create a new variable called `rainToday` that denotes whether the amount of precipitation was above zero:

# %%
SFrain['rainToday'] = SFrain['PRCP'] > 0
SFrain

# %% [markdown]
# Now we will summarize the data to compute the probability of rain:

# %%
pRainInSF = SFrain['rainToday'].mean()
pRainInSF

# %% [markdown]
# ## Conditional probability (Section \@ref(conditional-probability))
# Let's determine the conditional probability of someone having hearing problems, given that they are over 70 years of age, using the NHANES dataset.  First, let's create a new variable called `Over70` that denotes whether each individual is over 70 or not.

# %%
from nhanes.load import load_NHANES_data
nhanes_data = load_NHANES_data()

nhanes_data['Over70'] = nhanes_data['AgeInYearsAtScreening'] > 70

# %% [markdown]
# Now let's create a cleaned-up dataset that only includes the over70 variable along with the variable called `HaveSeriousDifficultyHearing` that denotes whether a person reports having serious hearing difficulty (coded as 1 for "yes" and 0 for "no").

# %%
hearing_data = nhanes_data[['Over70', 'HaveSeriousDifficultyHearing']].dropna()
hearing_data

# %% [markdown]
# First, what's the probability of being over 70?

# %%
p_over_70 = hearing_data['Over70'].mean()
p_over_70

# %% [markdown]
# Second, what's the probability of having hearing problems?

# %%
p_hearing_problem = hearing_data['HaveSeriousDifficultyHearing'].mean()
p_hearing_problem

# %% [markdown]
# What's the probability for each combination of unhealthy/healthy and over 70/ not? We can create a table that finds the joint probability for each combination:

# %%
joint_table = pd.crosstab(hearing_data.Over70, hearing_data['HaveSeriousDifficultyHearing'], normalize=True)
joint_table

# ```{r}
# pBoth <- healthDataFrame %>% 
#   mutate(
#     both = Unhealthy*Over70
#   ) %>%
#   summarise(
#     pBoth = mean(both)) %>% 
#   pull()

# pBoth
# ```

# Finally, what's the probability of someone being unhealthy, given that they are over 70 years of age?

# ```{r}

# pUnhealthyGivenOver70 <-
#   healthDataFrame %>%
#   filter(Over70 == TRUE) %>% # limit to Over70
#   summarise(pUnhealthy = mean(Unhealthy)) %>% 
#   pull()

# pUnhealthyGivenOver70


# ```

# ```{r}
# # compute the opposite:
# # what the probability of being over 70 given that 
# # one is unhealthy?
# pOver70givenUnhealthy <-
#   healthDataFrame %>%
#   filter(Unhealthy == TRUE) %>% # limit to Unhealthy
#   summarise(pOver70 = mean(Over70)) %>% 
#   pull()

# pOver70givenUnhealthy

# ```



# %%
