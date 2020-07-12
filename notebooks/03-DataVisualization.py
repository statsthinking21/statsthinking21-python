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

# # Data Visualization

# There are two main packages that we will use for visualization in Python: [matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/), which is based on matplotlib.  First, let's import these.  It is customary to import the pyplot module from matplotlib, since it contains most of the important plotting functions:

import matplotlib.pyplot as plt
import seaborn as sns
import numpy


# ## Let's think through a visualization

# Principles we want to keep in mind: 

# * Show the data without distortion
# * Use color, shape, and location to encourage comparisons
# * Minimize visual clutter (maximize your information to ink ratio)

# The two questions you want to ask yourself before getting started are:

# * What type of variable(s) am I plotting?
# * What comparison do I want to make salient for the viewer (possibly myself)?

# Figuring out *how* to highlight a comparison and include relevant variables usually benefits from sketching the plot out first.


# # Plotting the distribution of a single variable

# One of the most common uses of plotting is to plot the *distribution* of the data --- which you can think of as the *shape* of the data.  There are various ways to do this, but one of the most common is known as a *histogram*, which plots the number of observations that fall into specific bins. We can plot a histogram using the `plt.hist()` function from matplotlib.  As an example, let's look at the distribution of ages in the NHANES dataset.  First we need to load the data:


from nhanes.load import load_NHANES_data
nhanes_data = load_NHANES_data()

# Then we can plot the histogram:


age_histogram = plt.hist(nhanes_data['AgeInYearsAtScreening'])

# You can see from this plot that the `plt.hist()` function has binned together individuals across several years; That's because we let it automatically determine the size of the bins. Let's say that instead we want to bin each year separately.  We can do this using the `bins` argument to `plt.hist`. Because this argument takes a list of bins, we need to create a list that spans from the youngest to the oldest age.  We can do this using the `np.arange()` function from numpy, which generates a list of numbers that span a particular range. In this case, we need to span from the youngest to the oldest value, which are equivalent to the minimum and maximum values which we can obtain using the `.min()` and `.max()` operators; because Python starts at zero, we need to add one to the maximum in order to get the bins to cover the entire range:

bins = np.arange(nhanes_data['AgeInYearsAtScreening'].min(), nhanes_data['AgeInYearsAtScreening'].max() + 1)
age_histogram_1year_bins = plt.hist(nhanes_data['AgeInYearsAtScreening'], bins=bins)

# Sometimes it's more useful to look at the density rather than the counts, which we can do by setting `density=True` in our call to the histogram function:

age_density_1year_bins = plt.hist(nhanes_data['AgeInYearsAtScreening'], bins=bins, density=True)

# Now we see the proportion of individuals that fall into each age bin.  Why do you think there are so many eighty-year-olds in the dataset?  Have a look at the [documentation for the Age question](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.htm#RIDAGEYR) and see if you can figure it out.

# ### Bar vs. line plots

# The histograms above are an example of *bar plots* where each number is represented by a bar. In some cases we prefer to use a line instead of a bar, particularly when we want to highlight the relationships between different X-axis values, such as when we are plotting data over time.  For example, let's say that we wanted to plot average height as a function of age in the NHANES dataset.  We would first summarize the data to obtain the average height for each age:

mean_height_by_age = nhanes_data.groupby('AgeInYearsAtScreening')['StandingHeightCm'].mean()

# Here we use a method called `.groupby()` along with a builtin in method for computing the average of a variable in a dataframe (`.mean()`).  This returns a single average height value for all of the individuals in each age group, which we can then plot.  While we are at it, we will add descriptive labels to the X and Y axes, which is always a good idea:

plt.plot(mean_height_by_age.index, mean_height_by_age)
plt.xlabel('Age at screening')
plt.ylabel('Standing Height (cm)')

# As expected, people get taller up to about age 18, and then then slowly shrink over time.  Since we know that men and women differ in their height, we can also plot their average heights separately. We could do this using the matplot plotting function, but it's actually easier to do using the `sns.lineplot()` function from the seaborn library that we imported above.  We simply give it the X and Y variables that we want to plot as well as the variable that we want to separate (using different colors), and it does the work for us:

sns.lineplot(x='AgeInYearsAtScreening', y='StandingHeightCm', hue='Gender', data=nhanes_data)


# ## Plots with two variables

# Let's check out mileage by car manufacturer. We'll plot one *continuous* variable by one *nominal* one.

# First, let's make a bar plot by choosing the stat "summary" and picking the "mean" function to summarize the data.

# ```{r fig.width=8, fig.height=4, out.width="80%"}
# ggplot(mpg, aes(manufacturer, hwy)) +
#   geom_bar(stat = "summary", fun.y = "mean")  + 
#   ylab('Highway mileage')
# ```

# One problem with this plot is that it's hard to read some of the labels because they overlap. How could we fix that?  Hint: search the web for "ggplot rotate x axis labels" and add the appropriate command. 

# *TBD: fix*

# ```{r fig.width=8, fig.height=4, out.width="80%"}
# ggplot(mpg, aes(manufacturer, hwy)) +
#   geom_bar(stat = "summary", fun.y = "mean")  + 
#   ylab('Highway mileage')
# ```


# ### Adding on variables

# What if we wanted to add another variable into the mix? Maybe the *year* of the car is also important to consider. We have a few options here. First, you could map the variable to another **aesthetic**.

# ```{r fig.width=8, fig.height=4, out.width="80%"}
# # first, year needs to be converted to a factor
# mpg$year <- factor(mpg$year) 

# ggplot(mpg, aes(manufacturer, hwy, fill = year)) +
#   geom_bar(stat = "summary", fun.y = "mean")
# ```

# By default, the bars are *stacked* on top of one another. If you want to separate them, you can change the `position` argument form its default to "dodge".

# ```{r fig.width=8, fig.height=4, out.width="80%"}
# ggplot(mpg, aes(manufacturer, hwy, fill=year)) +
#   geom_bar(stat = "summary", 
#            fun.y = "mean", 
#            position = "dodge")
# ```

# ```{r fig.width=4, fig.height=4, out.width="50%"}
# ggplot(mpg, aes(year, hwy, 
#                 group=manufacturer,
#                 color=manufacturer)) +
#   geom_line(stat = "summary", fun.y = "mean")

# ```

# For a less visually cluttered plot, let's try **facetting**. This creates *subplots* for each value of the `year` variable.

# ```{r fig.width=8, fig.height=4, out.width="80%"}
# ggplot(mpg, aes(manufacturer, hwy)) +
#   # split up the bar plot into two by year
#   facet_grid(year ~ .) + 
#   geom_bar(stat = "summary", 
#            fun.y = "mean")
# ```

# ### Plotting dispersion

# Instead of looking at just the means, we can get a sense of the entire distribution of mileage values for each manufacturer.

# #### Box plot
# ```{r fig.width=8, fig.height=4, out.width="80%"}
# ggplot(mpg, aes(manufacturer, hwy)) +
#   geom_boxplot()
# ```

# A **box plot** (or box and whiskers plot) uses quartiles to give us a sense of spread. The thickest line, somewhere inside the box, represents the *median*. The upper and lower bounds of the box (the *hinges*) are the first and third quartiles (can you use them to approximate the interquartile range?). The lines extending from the hinges are the remaining data points, excluding **outliers**, which are plotted as individual points.

# #### Error bars

# Now, let's do something a bit more complex, but much more useful -- let's create our own summary of the data, so we can choose which summary statistic to plot and also compute a measure of dispersion of our choosing.

# ```{r fig.width=8, fig.height=4, out.width="80%"}
# # summarise data
# mpg_summary <- mpg %>%
#   group_by(manufacturer) %>% 
#   summarise(n = n(), 
#             mean_hwy = mean(hwy), 
#             sd_hwy = sd(hwy))

# # compute confidence intervals for the error bars
# # (we'll talk about this later in the course!)

# limits <- aes(
#   # compute the lower limit of the error bar
#   ymin = mean_hwy - 1.96 * sd_hwy / sqrt(n), 
#   # compute the upper limit
#   ymax = mean_hwy + 1.96 * sd_hwy / sqrt(n))

# # now we're giving ggplot the mean for each group, 
# # instead of the datapoints themselves

# ggplot(mpg_summary, aes(manufacturer, mean_hwy)) +
#   # we set stat = "identity" on the summary data 
#   geom_bar(stat = "identity") + 
#   # we create error bars using the limits we computed above
#   geom_errorbar(limits, width=0.5) 
# ```

# Error bars don't always mean the same thing -- it's important to determine whether you're looking at e.g. standard error or confidence intervals (which we'll talk more about later in the course).

# ##### Minimizing non-data ink

# The plot we just created is nice and all, but it's tough to look at. The bar plots add a lot of ink that doesn't help us compare engine sizes across manufacturers. Similarly, the width of the error bars doesn't add any information. Let's tweak which *geometry* we use, and tweak the appearance of the error bars.

# ```{r fig.width=8, fig.height=4, out.width="80%"}
# ggplot(mpg_summary, aes(manufacturer, mean_hwy)) +
#   # switch to point instead of bar to minimize ink used
#   geom_point() + 
#   # remove the horizontal parts of the error bars
#   geom_errorbar(limits, width = 0) 
# ```

# Looks a lot cleaner, but our points are all over the place. Let's make a final tweak to make *learning something* from this plot a bit easier.

# ```{r fig.width=8, fig.height=4, out.width="80%"}
# mpg_summary_ordered <- mpg_summary %>%
#   mutate(
#     # we sort manufacturers by mean engine size
#     manufacturer = reorder(manufacturer, -mean_hwy)
#   )

# ggplot(mpg_summary_ordered, aes(manufacturer, mean_hwy)) +
#   geom_point() + 
#   geom_errorbar(limits, width = 0) 

# ```

# ### Scatter plot

# When we have multiple *continuous* variables, we can use points to plot each variable on an axis. This is known as a **scatter plot**. You've seen this example in your reading.

# ```{r fig.width=4, fig.height=4, out.width="50%"}
# ggplot(mpg, aes(displ, hwy)) +
#   geom_point()
# ```

# #### Layers of data

# We can add layers of data onto this graph, like a *line of best fit*. We use a geometry known as a **smooth** to accomplish this.

# ```{r fig.width=4, fig.height=4, out.width="50%"}
# ggplot(mpg, aes(displ, hwy)) +
#   geom_point() +
#   geom_smooth(color = "black")
# ```

# We can add on points and a smooth line for another set of data as well (efficiency in the city instead of on the highway).

# ```{r fig.width=4, fig.height=4, out.width="50%"}
# ggplot(mpg) +
#   geom_point(aes(displ, hwy), color = "grey") +
#   geom_smooth(aes(displ, hwy), color = "grey") +
#   geom_point(aes(displ, cty), color = "limegreen") +
#   geom_smooth(aes(displ, cty), color = "limegreen")
# ```


# ## Creating a more complex plot

# In this section we will recreate Figure \@ref(fig:challengerTemps) from Chapter \@ref{data-visualization}.  Here is the code to generate the figure; we will go through each of its sections below.

# ```{r fig.width=8,fig.height=4,out.height='50%'}
# oringDf <- read.table("data/orings.csv", sep = ",",
#                       header = TRUE)

# oringDf %>%
#   ggplot(aes(x = Temperature, y = DamageIndex)) +
#   geom_point() +
#   geom_smooth(method = "loess",
#               se = FALSE, span = 1) + 
#   ylim(0, 12) +
#   geom_vline(xintercept = 27.5, size =8, 
#              alpha = 0.3, color = "red") +
#   labs(
#     y = "Damage Index",
#     x = "Temperature at time of launch"
#   ) +
#   scale_x_continuous(breaks = seq.int(25, 85, 5)) +
#   annotate(
#     "text",
#     angle=90,
#     x = 27.5,
#     y = 6,
#     label = "Forecasted temperature on Jan 28",
#     size = 5
#   )
# ```
