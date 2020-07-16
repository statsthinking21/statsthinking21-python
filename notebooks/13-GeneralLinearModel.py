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
# # The General Linear Model in R
# In this chapter we will explore how to fit general linear models in Python.  We will focus on the tools provided by the `statsmodels` package.

# %%
from nhanes.load import load_NHANES_data
nhanes_data = load_NHANES_data()
adult_nhanes_data = nhanes_data.query('AgeInYearsAtScreening > 17')


# %% [markdown]
# ## Linear regression
# To perform linear regression in Python, we use the `OLS()` function (which stands for *ordinary least squares*) from the `statsmodels` package.  Let's generate some simulated data and use this function to compute the linear regression solution.

# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_linear_data(slope, intercept,
                         noise_sd=1, x = None, 
                         npoints=100, seed=None):
    """
    generate data with a given slope and intercept
    and add normally distributed noise

    if x is passed as an argument then a given x will be used,
    otherwise it will be generated randomly

    Returns:
    --------
    a pandas data frame with variables x and y
    """
    if seed is not None:
        np.random.seed(seed)
    if x is None:
        x = np.random.randn(npoints)
    
    y = x * slope + intercept + np.random.randn(x.shape[0]) * noise_sd
    return(pd.DataFrame({'x': x, 'y': y}))

slope = 1
intercept = 10
noise_sd = 1
simulated_data = generate_linear_data(slope, intercept, noise_sd, seed=1)

plt.scatter(simulated_data['x'], simulated_data['y'])


# %% [markdown]
# We can then perform linear regression on these data using the `ols` function.  This function doesn't automatically include an intercept in its model, so we need to add one to the design.  Fitting the model using this function is a two-step process.  First, we set up the model and store it to a variable (which we will call `ols_model`).  Then, we actually fit the model, which generates the results that we store to a different variable called `ols_results`, and view a summary using the `.summary()` method of the results variable.
#
# from statsmodels.formula.api import ols
#
# ols_model = ols(formula='y ~ x + 1', data=simulated_data)
# ols_result = ols_model.fit()
# ols_result.summary()

# %% [markdown]
#  We should see three things in these results:
#
# * The estimate of the Intercept in the model should be very close to the intercept that we specified
# * The estimate for the x parameter should be very close to the slope that we specified
# * The residual standard deviation should be roughly similar to the noise standard deviation that we specified.  The summary doesn't report the residual standard deviation directly but we can compute it using the residuals that are stored in the `.resid` element in the result output:

# %%
ols_result.resid.std()


# %% [markdown]
# ## Model criticism and diagnostics
# Once we have fitted the model, we want to look at some diagnostics to determine whether the model is actually fitting properly.  
# The first thing to examine is to make sure that the residuals are (at least roughly) normally distributed.  We can do this using a Q-Q plot:

# %%
import seaborn as sns
import scipy.stats

scipy.stats.probplot(ols_result.resid, plot=sns.mpl.pyplot)

# %% [markdown]
# This looks pretty good, in the sense that the residual data points fall very close to the unit line.  This is not surprising, since we generated the data with normally distributed noise.  We should also plot the predicted (or *fitted*) values against the residuals, to make sure that the model does work systematically better for some predicted values versus others.

# %%

plt.scatter(ols_result.fittedvalues, ols_result.resid)
plt.xlabel('Fitted value')
plt.ylabel('Residual')

# %% [markdown]
# As expected, we see no clear relationship.
#
# ## Examples of problematic model fit
# Let's say that there was another variable at play in this dataset, which we were not aware of. This variable causes some of the cases to have much larger values than others, in a way that is unrelated to the X variable.  We play a trick here using the `seq()` function to create a sequence from zero to one, and then threshold those 0.5 (in order to obtain half of the values as zero and the other half as one) and then multiply by the desired effect size:

# %%
simulated_data.loc[:, 'x2'] = (simulated_data.index < (simulated_data.shape[0]/2)).astype('int')
hidden_effect_size = 10
simulated_data.loc[:, 'y2'] = simulated_data['y'] + simulated_data['x2'] * hidden_effect_size

# %% [markdown]
# Now we fit the model again, and examine the residuals:
#
# ols_model2 = ols(formula='y2 ~ x + 1', data=simulated_data)
# ols_result2 = ols_model.fit()
#
# plt.figure(figsize=(12,6))
# plt.subplot(1, 2, 1)
# scipy.stats.probplot(ols_result2.resid, plot=sns.mpl.pyplot)
#
# plt.subplot(1, 2, 2)
# plt.scatter(ols_result2.fittedvalues, ols_result2.resid)
# plt.xlabel('Fitted value')
# plt.ylabel('Residual')

# %% [markdown]
# The lack of normality is clear from the Q-Q plot, and we can also see that there is obvious structure in the residuals.  
#
# Let's look at another potential problem, in which the y variable is nonlinearly related to the X variable.  We can create these data by squaring the X variable when we generate the Y variable:

# %%

# ```{r}
# effsize=2
# regression_data <- regression_data %>%
#   mutate(y3 = (x**2)*slope + rnorm(npoints)*noise_sd + intercept)

# lm_result3 <- lm(y3 ~ x, data=regression_data)
# summary(lm_result3)

# ```

# Now we see that there is no significant linear relationship between $X^2$ and Y/ But if we look at the residuals the problem with the model becomes clear:

# ```{r fig.width=8, fig.height=4, out.width="80%"}
# autoplot(lm_result3,which=1:2)

# ```

# In this case we can see the clearly nonlinear relationship between the predicted and residual values, as well as the clear lack of normality in the residuals.  

# As we noted in the previous chapter, the "linear" in the general linear model doesn't refer to the shape of the response, but instead refers to the fact that model is linear in its parameters --- that is, the predictors in the model only get multiplied the parameters (e.g., rather than being raised to a power of the parameter).  Here is how we would build a model that could account for the nonlinear relationship:

# ```{r}
# # create x^2 variable
# regression_data <- regression_data %>%
#   mutate(x_squared = x**2)

# lm_result4 <- lm(y3 ~ x + x_squared, data=regression_data)
# summary(lm_result4)

# ```

# Now we see that the effect of $X^2$ is significant, and if we look at the residual plot we should see that things look much better:

# ```{r fig.width=8, fig.height=4, out.width="80%"}
# autoplot(lm_result4,which=1:2)

# ```
# Not perfect, but much better than before!

# ## Extending regression to binary outcomes.

# Let's say that we have a blood test (which is often referred to as a *biomarker*) and we want to know whether it predicts who is going to have a heart attack within the next year.  We will generate a synthetic dataset for a population that is at very high risk for a heart attack in the next year.

# ```{r}
# # sample size
# npatients=1000

# # probability of heart attack
# p_heartattack = 0.5

# # true relation to biomarker
# true_effect <- 0.6

# # assume biomarker is normally distributed
# disease_df <- tibble(biomarker=rnorm(npatients))

# # generate another variable that reflects risk for 
# # heart attack, which is related to the biomarker
# disease_df <- disease_df %>%
#   mutate(risk = biomarker*true_effect + rnorm(npatients))

# # create another variable that shows who has a 
# # heart attack, based on the risk variable
# disease_df <- disease_df %>%
#   mutate(
#     heartattack = risk > quantile(disease_df$risk,
#                                        1-p_heartattack))

# glimpse(disease_df)
# ```

# Now we would like to build a model that allows us to predict who will have a heart attack from these data. However, you may have noticed that the heartattack variable is a binary variable; because linear regression assumes that the residuals from the model will be normally distributed, and the binary nature of the data will violate this, we instead need to use a different kind of model, known as a *logistic regression* model, which is built to deal with binary outcomes.  We can fit this model using the `glm()` function:

# ```{r}
# glm_result <- glm(heartattack ~ biomarker, data=disease_df,
#                   family=binomial())
# summary(glm_result)
# ```

# This looks very similar to the output from the `lm()` function, and it shows us that there is a significant relationship between the biomarker and heart attacks. The model provides us with a predicted probability that each individual will have a heart attack; if this is greater than 0.5, then that means that the model predicts that the individual is more likely than not to have a heart attack.  
# We can start by simply comparing those predictions to the actual outcomes. 

# ```{r}
# # add predictions to data frame
# disease_df <- disease_df %>%
#   mutate(prediction = glm_result$fitted.values>0.5,
#          heartattack = heartattack)

# # create table comparing predicted to actual outcomes
# CrossTable(disease_df$prediction,
#            disease_df$heartattack,
#            prop.t=FALSE,
#            prop.r=FALSE,
#            prop.chisq=FALSE)

# ```

# This shows us that of the 500 people who had heart attacks, the model corrected predicted a heart attack for 343 of them.  It also predicted heart attacks for 168 people who didn't have them, and it failed to predict a heart attack for 157 people who had them. This highlights the distinction that we mentioned before between statistical and practical significance; even though the biomarker shows a highly significant relationship to heart attacks, it's ability to predict them is still relatively poor.  As we will see below, it gets even worse when we try to generalize this to a new group of people.

# ## Cross-validation (Section \@ref(cross-validation))

# Cross-validation is a powerful technique that allows us to estimate how well our results will generalize to a new dataset. Here we will build our own crossvalidation code to see how it works, continuing the logistic regression example from the previous section.

# In cross-validation, we want to split the data into several subsets and then iteratively train the model while leaving out each subset (which we usually call *folds*) and then test the model on that held-out fold  Let's write our own code to do this splitting; one relatively easy way to this is to create a vector that contains the fold numbers, and then randomly shuffle it to create the fold assigments for each data point.  

# ```{r}
# nfolds <- 4 # number of folds

# # we use the kronecker() function to repeat the folds
# fold <-  kronecker(seq(nfolds),rep(1,npatients/nfolds))
# # randomly shuffle using the sample() function
# fold <- sample(fold)

# # add variable to store CV predictions
# disease_df <- disease_df %>%
#   mutate(CVpred=NA)

# # now loop through folds and separate training and test data
# for (f in seq(nfolds)){
#   # get training and test data
#   train_df <- disease_df[fold!=f,]
#   test_df <- disease_df[fold==f,]
#   # fit model to training data
#   glm_result_cv <- glm(heartattack ~ biomarker, data=train_df,
#                   family=binomial())
#   # get probability of heart attack on test data
#   pred <- predict(glm_result_cv,newdata = test_df)
#   # convert to prediction and put into data frame
#   disease_df$CVpred[fold==f] = (pred>0.5)

# }
# ```

# Now let's look at the performance of the model:

# ```{r}
# # create table comparing predicted to actual outcomes
# CrossTable(disease_df$CVpred,
#            disease_df$heartattack,
#            prop.t=FALSE,
#            prop.r=FALSE,
#            prop.chisq=FALSE)

# ```

# Now we see that the model only accurately predicts less than half of the heart attacks that occurred when it is predicting to a new sample.  This tells us that this is the level of prediction that we could expect if were to apply the model to a new sample of patients from the same population.





# %%
