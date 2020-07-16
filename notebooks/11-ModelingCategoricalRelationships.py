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
# # Modeling categorical relationships in Python
#
# So far we have discussed the general concept of statistical modeling and hypothesis testing, and applied them to some simple analyses. In this chapter we will focus on the modeling of *categorical* relationships, by which we mean relationships between variables that are measured qualitatively.  These data are usually expressed in terms of counts; that is, for each value of the variable (or combination of values of multiple variables), how many observations take that value?  For example, when we count how many people from each major are in our class, we are fitting a categorical model to the data.
# As an example, we will use the NHANES dataset to ask whether there is a relationship between being a smoker and having ever had cancer (of any type).

# %%
from nhanes.load import load_NHANES_data
nhanes_data = load_NHANES_data()
adult_nhanes_data = nhanes_data.query('AgeInYearsAtScreening > 17')

# clean up smoking variables
adult_nhanes_data.loc[adult_nhanes_data['SmokedAtLeast100CigarettesInLife'] == 0, 'DoYouNowSmokeCigarettes'] = 'Not at all'
adult_nhanes_data.loc[:, 'SmokeNow'] = (adult_nhanes_data['DoYouNowSmokeCigarettes'] != 'Not at all')

categorical_df = adult_nhanes_data[['SmokeNow', 'EverToldYouHadCancerOrMalignancy']].dropna().astype('int').rename(columns={'EverToldYouHadCancerOrMalignancy': 'HadCancer'})


# %% [markdown]
# ## The Pearson Chi-squared test
# The Pearson Chi-squared test is used to test for an association between two categorical variables, against the null hypothesis of independence. We will use the `statsmodels.stats.Table` function for this, which has a number of useful features.

# %%
import statsmodels.api as sm
table = sm.stats.Table.from_data(categorical_df, shift_zeros=False)
table.table_orig

# %% [markdown]
# We can also see the predicted frequencies under the null hypothesis of independence, which are stored in the `.fittedvalues` element:

# %%
table.fittedvalues

# %% [markdown]
# Using these, we can compute the chi-squared statistic:

# %%
import numpy as np
orig_vector = np.ravel(table.table_orig)
independence_vector = np.ravel(table.fittedvalues)
squared_resid = (orig_vector - independence_vector)**2
chi2 = np.sum(squared_resid/independence_vector)
chi2


# %% [markdown]
# We can confirm this by comparing it to the result from the built-in function to compute the association:
#
# chi2_result = table.test_nominal_association()
# print(chi2_result)

# %% [markdown]
# We can also see the standardized residuals:

# %%
table.standardized_resids


# %% [markdown]
# This shows that there is an unexpectedly large number of people who smoke but don't have cancer, and similarly an unexpectedly low number of smokers who report having had cancer before.  Does this tell us that smoking results in lower rates of cancer?
