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
# # Hypothesis testing in Python
# In this chapter we will present several examples of using Python to perform hypothesis testing.
#
# ## Simple example: Coin-flipping (Section \@ref(randomization-very-simple))
# Let's say that we flipped 100 coins and observed 70 heads. We would like to use these data to test the hypothesis that the true probability is 0.5.
# First let's generate our data, simulating 100,000 sets of 100 flips. We use such a large number because it turns out that it's very rare to get 70 heads, so we need many attempts in order to get a reliable estimate of these probabilties.  This will take a couple of minutes to complete.

# %%

import numpy as np
import pandas as pd

num_runs = 1000000

def toss_coins_and_count_heads(num_coins=100, p_heads=0.5):
    """
    flip a coin num_coins times and return number of heads
    """

    flips = np.random.rand(num_coins) > (1 - p_heads)
    return(np.sum(flips))

    
flip_results_df = pd.DataFrame({'n_heads': np.zeros(num_runs)})

for run in range(num_runs):
    flip_results_df.loc[run, 'n_heads'] = toss_coins_and_count_heads()


# %% [markdown]
# Now we can compute the proportion of samples from the distribution observed when the true proportion of heads is 0.5.  

# %%
import scipy.stats

pvalue = 1 - scipy.stats.percentileofscore(flip_results_df, 0.7)
pvalue

# %% [markdown]
# For comparison, we can also compute the p-value for 70 or more heads based on a null hypothesis of $P_{heads}=0.5$, using the binomial distribution.
#
# ```{r}
# # compute the probability of 69 or fewer heads, 
# # when P(heads)=0.5
# p_lt_70 <- pbinom(69, 100, 0.5) 
#
# # the probability of 70 or more heads is simply 
# # the complement of p_lt_70
# p_ge_70 <- 1 - p_lt_70
#
# p_ge_70
# ```
#
# ## Simulating p-values
#
# In this exercise we will perform hypothesis testing many times in order to test whether the p-values provided by our statistical test are valid.  We will sample data from a normal distribution with a mean of zero, and for each sample perform a t-test to determine whether the mean is different from zero.  We will then count how often we reject the null hypothesis; since we know that the true mean is zero, these are by definition Type I errors.
#
# ```{r}
# nRuns <- 5000
#
# # create input data frame for do()
# input_df <- tibble(id=seq(nRuns)) %>%
#   group_by(id)
#
# # create a function that will take a sample
# # and perform a one-sample t-test
#
# sample_ttest <- function(sampSize=32){
#   tt.result <- t.test(rnorm(sampSize))
#   return(tibble(pvalue=tt.result$p.value))
# }
#
# # perform simulations
#
# sample_ttest_result <- input_df %>%
#   do(sample_ttest())
#
# p_error <-
#   sample_ttest_result %>%
#   ungroup() %>%
#   summarize(p_error = mean(pvalue<.05)) %>%
#   pull()
#
# p_error
#
# ```
#
# We should see that the proportion of samples with $p < .05$ is about 5%.
#
#
#
#

# %%
