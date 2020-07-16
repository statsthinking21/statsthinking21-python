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
#
#
# %%

import numpy as np
import pandas as pd


np.random.seed(12345) 

nhanes_data = load_NHANES_data() #CK: note this gives an error "Specify dtype option on import"
adult_nhanes_data = nhanes_data.query('AgeInYearsAtScreening > 18')
adult_nhanes_data = adult_nhanes_data.dropna(subset=['WeightKg']).rename(columns={'WeightKg': 'Weight'})
#adult_nhanes_data = adult_nhanes_data.drop_duplicates()


# %% [markdown]
#In this chapter we focus specifically on statistical power.
#
## Power analysis
#
#We can compute a power analysis using functions from the `statsmodels.stats.power` package. Let's focus on the power for an independent samples t-test in order to determine a difference in the mean between two groups.  Let's say that we think than an effect size of Cohen's d=0.5 is realistic for the study in question (based on previous research) and would be of scientific interest.  We wish to have 80% power to find the effect if it exists.  We can compute the sample size needed for adequate power using the `TTestIndPower()` function:

# %%

import scipy.stats
import statsmodels.stats.power as smp
import matplotlib.pyplot as plt
import seaborn as sns

power_analysis = smp.TTestIndPower()
sample_size = power_analysis.solve_power(effect_size = 0.5, power = 0.8, alpha = 0.05)
sample_size
#print('Sample Size: %.3f' % sample_size)

# %% [markdown]
#Thus, about 64 participants would be needed in each group in order to test the hypothesis with adequate power.
#
# 
#
## Power curves
#
#We can also create plots that can show us how the power to find an effect varies as a function of effect size and sample size, at the alpha specified in the power analysis. We willl use the `plot_power()` function. The x-axis is defined by the 'dep_var' argument, while sample sizes (nobs) and effect sizes (effect_size) are provided in arrays. 
#
#
# %%

effect_sizes = np.array([0.2, 0.5, 0.8])
sample_sizes = np.array(range(10, 500, 10))

plt.style.use('seaborn')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
fig=power_analysis.plot_power(dep_var='nobs', nobs=sample_sizes, effect_size=effect_sizes, alpha=0.05, ax=ax, title='Power of Independent Samples t-test' + '\n' + r'$\alpha = 0.05$')


#import itertools
#input_df=pd.DataFrame(itertools.product(sample_sizes, effect_sizes))
#input_df

# %% [markdown]
#Using this, we can then perform a power analysis for each combination of effect size and sample size to create our power curves.  In this case, let's say that we wish to perform a two-sample t-test.
%%

#CK: Didn't do this part, since the plot_power function above does it. In case it's better practice, I tried to do it, but got stuck with returning the power result from TTestIndPower.power. Perhaps it can be computed a different way?
#```{r}
# create a function get the power value and
# return as a tibble
#get_power <- function(df){
#  power_result <- pwr.t.test(n=df$sample_sizes, 
#                             d=df$effect_sizes,
#                             type='two.sample')
#  df$power=power_result$power
#  return(df)
#}
# run get_power for each combination of effect size 
# and sample size
#power_curves <- input_df %>%
#  do(get_power(.)) %>%
#  mutate(effect_sizes = as.factor(effect_sizes)) 
#```

#Now we can plot the power curves, using a separate line for each effect size.
#
#```{r fig.width=4,fig.height=4,out.width="50%"}
#ggplot(power_curves, 
#       aes(x=sample_sizes,
#           y=power, 
#           linetype=effect_sizes)) + 
#  geom_line() + 
#  geom_hline(yintercept = 0.8, 
#             linetype='dotdash')
#```

# %% [markdown]
## Simulating statistical power
#
#
#Let's simulate this to see whether the power analysis actually gives the right answer.
#We will sample data for two groups, with a difference of 0.5 standard deviations between their underlying distributions, and we will look at how often we reject the null hypothesis.

#%%

num_runs = 5000
effectSize = 0.5

# perform power analysis to get sample size
power_analysis = smp.TTestIndPower()
sampleSize = power_analysis.solve_power(effect_size = effectSize, power = 0.8, alpha = 0.05)

# round up from estimated sample size
sampleSize=np.int(np.ceil(sampleSize))

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


# %% [markdown]
# This should return a number very close to 0.8.

# %%
