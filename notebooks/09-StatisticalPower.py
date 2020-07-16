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
# # Statistical Power Analysis in Python
# In this chapter we focus specifically on statistical power.  We will use the NHANES dataset, so let's first set that up.
# %%

import numpy as np
import pandas as pd

np.random.seed(12345) 

from nhanes.load import load_NHANES_data

nhanes_data = load_NHANES_data() 
adult_nhanes_data = nhanes_data.query('AgeInYearsAtScreening > 18')
adult_nhanes_data = adult_nhanes_data.dropna(subset=['WeightKg']).rename(columns={'WeightKg': 'Weight'})


# %% [markdown]
# ## Power analysis
#
# We can compute a power analysis using functions from the `statsmodels.stats.power` package. Let's focus on the power for an independent samples t-test in order to determine a difference in the mean between two groups.  Let's say that we think than an effect size of Cohen's d=0.5 is realistic for the study in question (based on previous research) and would be of scientific interest.  We wish to have 80% power to find the effect if it exists.  We can compute the sample size needed for adequate power using the `TTestIndPower()` function:

# %%

import scipy.stats
import statsmodels.stats.power as smp
import matplotlib.pyplot as plt

power_analysis = smp.TTestIndPower()
sample_size = power_analysis.solve_power(effect_size=0.5, power=0.8, alpha=0.05)
sample_size

# %% [markdown]
# Thus, about 64 participants would be needed in each group in order to test the hypothesis with adequate power.
#
# ## Power curves
#
# We can also create plots that can show us how the power to find an effect varies as a function of effect size and sample size, at the alpha specified in the power analysis. We will use the `plot_power()` function. The x-axis is defined by the `dep_var` argument, while sample sizes (nobs) and effect sizes (effect_size) are provided as arrays. 
# %%
#+
effect_sizes = np.array([0.2, 0.5, 0.8])
sample_sizes = np.array(range(10, 500, 10))

plt.style.use('seaborn')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
fig = power_analysis.plot_power(
    dep_var='nobs', nobs=sample_sizes,  
    effect_size=effect_sizes, alpha=0.05, ax=ax, 
    title='Power of Independent Samples t-test\n$\\alpha = 0.05$')

#-

# %% [markdown]
# ## Simulating statistical power
#
# We can also simulate data to see whether the power analysis actually gives the right answer.
# We will sample data for two groups, with a difference of 0.5 standard deviations between their underlying distributions and a sample size based on power analysis, and we will then look at how often we reject the null hypothesis.
# %%
#+
num_runs = 5000
effectSize = 0.5

# perform power analysis to get sample size
power_analysis = smp.TTestIndPower()
sampleSize = power_analysis.solve_power(
    effect_size=effectSize, power=0.8, alpha=0.05)

# round up from estimated sample size
sampleSize = np.int(np.ceil(sampleSize))

# create a function that will generate samples and test for
# a difference between groups using a two-sample t-test


def get_t_result(sampleSize, effectSize):
    """
    perform a ttest on random data of n=sampSize
    """
    
    group1 = np.random.normal(loc=0.0, scale=1.0, size=sampleSize)
    group2 = np.random.normal(loc=effectSize, scale=1.0, size=sampleSize)
    ttresult = scipy.stats.ttest_ind(group1, group2)
    return(ttresult.pvalue)


# create input data frame for output
power_sim_results = pd.DataFrame({'p_value': np.zeros(num_runs)})

for run in range(num_runs):
    power_sim_results.loc[run, 'p_value'] = get_t_result(sampleSize, effectSize)


p_reject = np.mean(power_sim_results['p_value'] < 0.05)
p_reject
#-


# %% [markdown]
# This should return a number very close to 0.8.
