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
# # Fitting simple models
#
# In this chapter we will focus on how to compute the measures of central tendency and variability that were covered in the previous chapter.  Most of these can be computed using a built-in Python function, but we will show how to do them manually in order to give some intuition about how they work. First let's load the NHANES data that we will use for our examples.

# %%
from nhanes.load import load_NHANES_data
nhanes_data = load_NHANES_data()
adult_nhanes_data = nhanes_data.query('AgeInYearsAtScreening > 17')

# %% [markdown]
# Since we will be analyzing the `StandingHeightCm` variable, we should exclude any observations that are missing this measurement.  We will also recode the variable to be called `Height` in order to simplify the coding later.

# %%
adult_nhanes_data = adult_nhanes_data.dropna(subset=['StandingHeightCm']).rename(columns={'StandingHeightCm': 'Height'})


# %% [markdown]
# ## Mean
# The mean is defined as the sum of values divided by the number of values being summed:
# $$
# \bar{X} = \frac{\sum_{i=1}^{n}x_i}{n}
# $$
# Let's say that we want to obtain the mean height for adults in the NHANES database (contained in the data `Height`).  We would sum the individual heights (using the `.sum()` operator) and then divide by the number of values:

# %%
adult_nhanes_data['Height'].sum()/adult_nhanes_data['Height'].shape[0]

# There is, of course, a built-in operator for the data frame called `.mean()` that will compute the mean.  

# %%
adult_nhanes_data['Height'].mean()


# ## Median
# The median is the middle value after sorting the entire set of values. First we sort the data in order of their values:

# %%

# ```{r}
# height_sorted <- sort(height_noNA)
# ```

# Next we find the median value.  If there is an odd number of values in the list, then this is just the value in the middle, whereas if the number of values is even then we take the average of the two middle values.  We can determine whether the number of items is even by dividing the length by two and seeing if there is a remainder; we do this using the `%%` operator, which is known as the *modulus* and returns the remainder:

# ```{r}
# 5 %% 2
# ```

# Here we will test whether the remainder is equal to one; if it is, then we will take the middle value, otherwise we will take the average of the two middle values.  We can do this using an if/else structure, which executes different processes depending on which of the arguments are true:

# ```
# if (logical value) {
#   functions to perform if logical value is true
# } else {
#   functions to perform if logical value is false

# }
# ```
 
# Let's do this with our data.  To find the middle value when the number of items is odd, we will divide the length and then round up, using the `ceiling()` function:

# ```{r}
# if (length(height_sorted) %% 2 == 1){
#   # length of vector is odd
#   median_height <- 
#     height_sorted[ceiling(length(height_sorted) / 2)]
# } else {
#   median_height <- 
#     (height_sorted[length(height_sorted) / 2] + 
#         height_sorted[1 + length(height_sorted) / (2)])/2
# }

# median_height
# ```

# We can compare this to the result from the built-in median function:

# ```{r}
# median(height_noNA)
# ```


# ## Mode

# The mode is the most frequent value that occurs in a variable. R has a function called `mode()` but if you look at the help page you will see that it doesn't actually copute the mode.  In fact, R doesn't have a built-in function to compute the mode, so we need to create one. Let start with some toy data:

# ```{r}
# mode_test = c('a', 'b', 'b', 'c', 'c', 'c')
# mode_test
# ```

# We can see by eye that the mode is "a" since it occurs more often than the others.  To find it computationally, let's first get the unique values

# To do this, we first create a table with the counts for each value, using the `table()` function:

# ```{r}
# mode_table <- table(mode_test)
# mode_table
# ```

# Now we need to find the maximum value.  We do this by comparing each value to the maximum of the table; this will work even if there are multiple values with the same frequency (i.e. a tie for the mode).

# ```{r}
# table_max <- mode_table[mode_table == max(mode_table)]
# table_max
# ```

# This variable is a special kind of value called a *named vector*, and its name contains the value that we need to identify the mode.  We can pull it out using the `names()` function:

# ```{r}
# my_mode <- names(table_max)[1]
# my_mode
# ```

# Let's wrap this up into our own custom function:

# ```{r}
# getmode <- function(v, print_table=FALSE) {
#   mode_table <- table(v)
#   if (print_table){
#     print(kable(mode_table))
#   }
#   table_max <- mode_table[mode_table == max(mode_table)]
#   return(names(table_max))
# }
# ```

# We can then apply this to real data.  Let's apply this to the `MaritalStatus` variable in the NHANES dataset:

# ```{r}
# getmode(NHANES$MaritalStatus)
# ```

# ## Variability

# Let's first compute the *variance*, which is the average squared difference between each value and the mean.  Let's do this with our cleaned-up version of the height data, but instead of working with the entire dataset, let's take a random sample of 150 individuals:

# ```{r}
# height_sample <- NHANES %>%
#   drop_na(Height) %>%
#   sample_n(150) %>%
#   pull(Height)
# ```


# First we need to obtain the sum of squared errors from the mean. In R, we can square a vector using `**2`:

# ```{r}
# SSE <- sum((height_sample - mean(height_sample))**2)
# SSE
# ```

# Then we divide by N - 1 to get the estimated variance:

# ```{r}
# var_est <- SSE/(length(height_sample) - 1)
# var_est
# ```

# We can compare this to the built-in `var()` function:

# ```{r}
# var(height_sample)
# ```

# We can get the *standard deviation* by simply taking the square root of the variance:

# ```{r}
# sqrt(var_est)
# ```

# Which is the same value obtained using the built-in `sd()` function:

# ```{r}
# sd(height_sample)
# ```

# ## Z-scores

# A Z-score is obtained by first subtracting the mean and then dividing by the standard deviation of a distribution.  Let's do this for the `height_sample` data.

# ```{r}
# mean_height <- mean(height_sample)
# sd_height <- sd(height_sample)

# z_height <- (height_sample - mean_height)/sd_height
# ```

# Now let's plot the histogram of Z-scores alongside the histogram for the original values. We will use the `plot_grid()` function from the `cowplot` library to plot the two figures alongside one another.  First we need to put the values into a data frame, since `ggplot()` requires the data to be contained in a data frame.

# ```{r fig.height=4, fig.width=8}
# height_df <- data.frame(orig_height=height_sample, 
#                         z_height=z_height)

# # create individual plots
# plot_orig <- ggplot(height_df, aes(orig_height)) + 
#   geom_histogram()
# plot_z <- ggplot(height_df, aes(z_height)) + 
#   geom_histogram()

# # combine into a single figure
# plot_grid(plot_orig, plot_z)

# ```

# You will notice that the shapes of the histograms are similar but not exactly the same. This occurs because the binning is slightly different between the two sets of values.  However, if we plot them against one another in a scatterplot, we will see that there is a direct linear relation between the two sets of values:

# ```{r, fig.width=4, fig.height=4}
# ggplot(height_df, aes(orig_height, z_height)) + 
#   geom_point()
# ```





# %%
