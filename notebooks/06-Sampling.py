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
# # Sampling
# In this chapter we will learn how to use Python to understand sampling and sampling error.
#
# ## Sampling error
# Here we will repeatedly sample from the NHANES Height variable in order to obtain the sampling distribution of the mean. First let's load the data and clean them up.

# %%

from nhanes.load import load_NHANES_data
nhanes_data = load_NHANES_data()
adult_nhanes_data = nhanes_data.query('AgeInYearsAtScreening > 17')
adult_nhanes_data = adult_nhanes_data.dropna(subset=['StandingHeightCm']).rename(columns={'StandingHeightCm': 'Height'})


# %% [markdown]
# Now let's repeatedly sample 50 individuals from the dataset, compute the mean, and store the resulting values.  For this we are going to use a *for loop*, which allows us to repeatedly perform a particular set of actions.

# %%
#+
sample_size = 50
num_samples = 5000

import pandas as pd
# set up a variable to store the result
sampling_results = pd.DataFrame({'mean': np.zeros(num_samples)})

for sample_num in range(num_samples):
    sample = adult_nhanes_data.sample(sample_size)
    sampling_results.loc[sample_num, 'mean'] = sample['Height'].mean()
#-

# %% [markdown]
# Now let's plot the sampling distribution.  We will also overlay the sampling distribution of the mean predicted on the basis of the population mean and standard deviation, to show that it properly describes the actual sampling distribution.

# %%


# ```{r fig.width=8,fig.height=4,out.height='50%'}

# # pipe the sampMeans data frame into ggplot
# sampMeans %>% 
#   ggplot(aes(meanHeight)) +
#   # create histogram using density rather than count
#   geom_histogram(
#     aes(y = ..density..),
#     bins = 50,
#     col = "gray", 
#     fill = "gray"
#   ) +
#   # add a vertical line for the population mean
#   geom_vline(xintercept = mean(NHANES_adult$Height),
#              size=1.5) +
#   # add a label for the line
#   annotate(
#     "text",
#     x = 169.6, 
#     y = .4,
#     label = "Population mean",
#     size=6
#   ) +
#   # label the x axis
#   labs(x = "Height (cm)") +
#   # add normal based on population mean/sd
#   stat_function(
#       fun = dnorm, n = sampSize,
#       args = list(
#         mean = mean(NHANES_adult$Height),
#         sd = sd(NHANES_adult$Height)/sqrt(sampSize)
#       ), 
#       size = 1.5,
#       color = "black",
#       linetype='dotted'
#     ) 
  

# ```

# ## Central limit theorem

# The central limit theorem tells us that the sampling distribution of the mean becomes normal as the sample size grows.  Let's test this by sampling a clearly non-normal variable and look at the normality of the results using a Q-Q plot. We saw in Figure \@ref(fig:alcDist50) that the variable `AlcoholYear` is distributed in a very non-normal way. Let's first look at the Q-Q plot for these data, to see what it looks like.  We will use the `stat_qq()` function from `ggplot2` to create the plot for us.

# ```{r fig.width=4, fig.height=4}
# # prepare the dta
# NHANES_cleanAlc <- NHANES %>%
#   drop_na(AlcoholYear)

# ggplot(NHANES_cleanAlc, aes(sample=AlcoholYear)) +
#   stat_qq() + 
#   # add the line for x=y
#   stat_qq_line()
# ```

# We can see from this figure that the distribution is highly non-normal, as the Q-Q plot diverges substantially from the unit line.

# Now let's repeatedly sample and compute the mean, and look at the resulting Q-Q plot.  We will take samples of various sizes to see the effect of sample size.  We will use a function from the `dplyr` package called `do()`, which can run a large number of analyses at once.  

# ```{r}
# set.seed(12345)

# sampSizes <- c(16, 32, 64, 128) # size of sample
# nsamps <- 1000 # number of samples we will take

# # create the data frame that specifies the analyses
# input_df <- tibble(sampSize=rep(sampSizes,nsamps),
#                       id=seq(nsamps*length(sampSizes)))


# # create a function that samples and returns the mean
# # so that we can loop over it using replicate()
# get_sample_mean <- function(sampSize){
#   meanAlcYear <- 
#     NHANES_cleanAlc %>%
#     sample_n(sampSize) %>%
#     summarize(meanAlcoholYear = mean(AlcoholYear)) %>%
#     pull(meanAlcoholYear)
#   return(tibble(meanAlcYear = meanAlcYear, sampSize=sampSize))
# }

# # loop through sample sizes
# # we group by id so that each id will be run separately by do()
# all_results = input_df %>% 
#   group_by(id) %>%
#   # "." refers to the data frame being passed in by do()
#   do(get_sample_mean(.$sampSize))



# ```

# Now let's create separate Q-Q plots for the different sample sizes.  

# ```{r fig.width=8, fig.height=8}

# # create empty list to store plots

# qqplots = list()

# for (N in sampSizes){
#   sample_results <- 
#     all_results %>%
#     filter(sampSize==N)

#   qqplots[[toString(N)]] <- ggplot(sample_results, 
#                                 aes(sample=meanAlcYear)) +
#     stat_qq() + 
#     # add the line for x=y
#     stat_qq_line(fullrange = TRUE) + 
#     ggtitle(sprintf('N = %d', N)) + 
#    xlim(-4, 4) 

# }

# plot_grid(plotlist = qqplots)

# ```

# This shows that the results become more normally distributed (i.e. following the straight line) as the samples get larger.

# ## Confidence intervals (Section \@ref(confidence-intervals))

# Remember that confidence intervals are intervals that will contain the population parameter on a certain proportion of times.  In this example we will walk through the simulation that was presented in Section \@ref(confidence-intervals) to show that this actually works properly.  Here we will use a function called `do()` that lets us 

# ```{r echo=FALSE}
# # compute how often the confidence interval contains the true population mean
# nsamples <- 2500
# sampSize <- 100

# ci_data <- tibble(run=seq(nsamples), sampSize=sampSize) %>%
#   group_by(run)

# # create a function that takes a sample and returns the confidence interval

# get_ci <- function(sampSize){
#   result <- NHANES_adult %>%
#     sample_n(sampSize) %>%
#     summarize(
#       mean = mean(Height),
#       sem = sd(Height) / sqrt(sampSize)
#     ) %>%
#     mutate(
#       CI_upper = mean + 1.96 * sem,
#       CI_lower = mean - 1.96 * sem
#     )
# }

# ci_results <- do(ci_data, get_ci(sampSize))
# pop_mean <- mean(NHANES_adult$Height)
# ci_results <- 
#   ci_results %>%
#   mutate(pop_mean_within_ci = CI_upper > pop_mean & CI_lower < pop_mean) %>%
#   summarize(p_popmean_within_ci=mean(pop_mean_within_ci)) %>%
#   pull()

# ```



# %%
