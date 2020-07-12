# -*- coding: utf-8 -*-
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

# # Introduction to Python
# *Contributors*: John Butler, Russell Poldrack
#
# In this chapter we will give you an overview of the basic features of the Python programming language.  This introduction won't make you an ace programmer --- only practice will do that. However, it will give you an introduction to some of the most important features of the language.
#
# ## Why programming is hard to learn
#
# Programming a computer is a skill, just like playing a musical instrument or speaking a second language. And just like those skills, it takes a lot of work to get good at it --- the only way to acquire a skill is through practice.  There is nothing special or magical about people who are experts, other than the quality and quantity of their experience! However, not all practice is equally effective.  A large amount of psychological research has shown that practice needs to be *deliberate*, meaning that it focuses on developing the specific skills that one needs to perform the skill, at a level that is always pushing one's ability.
#
# If you have never programmed before, then it's going to seem hard, just as it would seem hard for a native English speaker to start speaking Mandarin.  However, just as a beginning guitarist needs to learn to play their scales, we will teach you how to perform the basics of programming, which you can then use to do more powerful things.
#
# One of the most important aspects of computer programming is that you can try things to your heart's content; the worst thing that can happen is that the program will crash.  Trying new things and making mistakes is one of the keys to learning.
#
# The hardest part of programming is figuring out why something didn't work, which we call *debugging*.  In programming, things are going to go wrong in ways that are often confusing and opaque. Every programmer has a story about spending hours trying to figure out why something didn't work, only to realize that the problem was completely obvious in hindsight.  The more practice you get, the better you will get at figuring out how to fix these errors.  But there are a few strategies that can be helpful.
#
# ### Use the web
#
# In particular, you should take advantage of the fact that there are millions of people programming in Python around the world, so nearly any error message you see has already been seen by someone else.  Whenever I experience an error that I don't understand, the first thing that I do is to copy and paste the error message into a search engine. Often this will provide several pages discussing the problem and the ways that people have solved it.
#
# ### Rubber duck debugging
#
# The idea behind *rubber duck debugging* is to pretend that you are trying to explain what your code is doing to an inanimate object, like a rubber duck.  Often, the process of explaning it aloud is enough to help you find the problem.
#
# ## Getting access to Python
#
# If you want to try out Python without having to install it on your own computer (or if you have a computer that doesn't support it, such as a Chromebook), the best way to try it out is using a web platform that supports *notebooks*, which are documents that allow you to combine text and code; this book was actually written using such notebooks.  Two good options are [Google Colab](https://colab.research.google.com/) and [Kaggle Kernels](https://www.kaggle.com/kernels).  **TBD: MAKE ALL CHAPTERS AVAILABLE ON BOTH**
#
# If you do want to install it on your own computer, we recommend installing the [Anaconda](https://www.anaconda.com/products/individual) software package, which will provide you with Python as well as many related packages. 
#
#

# ## Getting started with Python
#
# When we work with Python, we can do this at the command line in a terminal or (as we will do) using a *Jupyter notebook*.
# Notebooks are composed of *cells*, each of which can contain either Python code or text.  
#
# Jupyter notebooks use a special kind of text known as [Markdown](https://daringfireball.net/projects/markdown/syntax), which allows formatting (such as headings or text styles like bold and italics).  If you were to double-click on this cell in Jupyter, you would be able to edit the text. Once you are done editing, hit the **Run** button (the triangular arrow button above), or press Shift+Enter, and the text will be shown normally.
#
# The following cell is a **code** cell, which we use for Python code. Code cells are denoted in Jupyter by shading in gray.  In a code cell, we type Python commands. When we hit the **Run** button (the triangular arrow button above), or press Shift+Enter, our commands will run and a result will print out in an output cell. 
#
# One difference between a code cell and a Markdown cell is that the code cell has a number to its left surrounded by square brackets. If you type a command into the cell and then run it, the result will appear below, with the same number to its left.
#
# In the simplest case, if we just type in a number, the cell will simply respond with that number. In the code cell below, we have typed the number 3. Click on the cell to edit or run the code again (Shift+Enter).

3

# Let’s try something a bit more complicated:

3 + 4

# Python spits out the answer to whatever you type in, as long as it can figure it out. 
#
# Now let’s try typing in a word:
#
# ```hello```
#
# This would result in the following output:
#
# ```
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
#  in 
# ----> 1 hello
#
# NameError: name 'hello' is not defined
# ```
#

# What? Why did this happen? When Python encounters a letter or word, it assumes that it is referring to the *name of a variable* — think of X from high school algebra. We will return to variables in a little while, but if we want Python to print out the word hello then we need to contain it in quotation marks (single or double, it doesn't matter), telling Python that it is a character string.

"hello"

# There are many types of variables in Python. You have already seen two examples: integers (like the number 3) and character strings (like the word “hello”). Another important one is real numbers, which are the most common kind of numbers that we will deal with in statistics, which span the entire number line including the spaces in between the integers. For example:

1 / 6


# By default, Python uses floating-point numbers, which provide a high level of precision. In many cases, however, you may want to round floating-point outputs to two or three decimal places, which can be done with the ``round()`` function.

round(1 / 6, 3)

# Another kind of variable is known as a logical variable, because it is based on the idea from logic that a statement can be either True or False.
#
# To determine whether a statement is true or not, we use logical operators. You are already familiar with some of these, like the greater-than (`>`) and less-than (`<`) operators.

1 < 3

2 > 4

# Often we want to know whether two numbers are equal or not equal to one another. There are special operators in python to do this: `==` for equals, and `!=` for not-equals:

3 == 3

4 != 4

# One very important thing to know is that Python treats *True* the same as the number one, and *False* the same as the number zero.  To see this, let's test whether ``True`` is equal to the number one:

True == 1

# This will become important later on, when we work with probabilities.

# ## Variables
#
# A variable is a symbol that stands for another value (just like “X” in algebra). We can create a variable by assigning a value to it using the `=` operator. If we then type the name of the variable, Python will print out its value --- as long as that variable name is the last entry in the cell.

x = 4
x

# The variable now stands for the value that it contains, so we can perform operations on it and get the same answer as if we used the value itself.

x + 3

x == 5

# We can change the value of a variable by simply assigning a new value to it.

x = x + 1

x

# ## Libraries
#
# Although Python has many useful features, many of the features we will need are not contained in the primary Python library but instead come from open source libraries that have been developed by various members of the python community.
#
# Two packages that we will use extensively are [NumPy](https://numpy.org/) and [Pandas](https://pandas.pydata.org/). These libraries are part of the [SciPy](https://www.scipy.org/) stack, a group of Python libraries used for scientific computing.
#
# In Python, to work with a library, we first have to *import* it and specify how we are going to call on the functions of that library (functions will be explained in more detail below).
#
# Here is how we will import NumPy:

import numpy as np

# Now, when we call on a NumPy function, we will use the prefix ``np```. This will be made clearer below.
#
# We also import pandas, specifying ``pd``` as the prefix:

import pandas as pd  ## RP: pd is more common abbreviation

# After importing a library, you can now access all of its features using the specified prefix. If you want to learn more about a library's features, you can find them using the ``help()`` function:

# + tags=[]
help(np.zeros)
# -

# ## Functions
#
# A function is an operator that takes some input and gives an output based on the input. For example, let’s say that we have a number, and we want to determine its absolute value. NumPy has a function called ``abs()`` that takes in a number and outputs its absolute value:

x = -3
np.abs(x)

# Most functions take an input like the ``np.abs()`` function (which we call an argument), but some also have special keywords that can be used to change how the function works. For example, the ``np.random.normal()`` function generates random numbers from a normal distribution (which we will learn more about later). Have a look at the help page for this function by typing ``help(np.random.normal)`` in the console, which will cause a help page to appear below. The first section of the help page for the ``np.random.normal()`` function shows the following:

#     normal(...) method of numpy.random.mtrand.RandomState instance
#     normal(loc=0.0, scale=1.0, size=None)
#     
#     Draw random samples from a normal (Gaussian) distribution.
#     
#     The probability density function of the normal distribution, first
#     derived by De Moivre and 200 years later by both Gauss and Laplace
#     independently [2]_, is often called the bell curve because of
#     its characteristic shape (see the example below).
#     
#     The normal distributions occurs often in nature.  For example, it
#     describes the commonly occurring distribution of samples influenced
#     by a large number of tiny, random disturbances, each with its own
#     unique distribution [2]_.
#     
#     Parameters
#     ----------
#     loc : float or array_like of floats
#         Mean ("centre") of the distribution.
#     scale : float or array_like of floats
#         Standard deviation (spread or "width") of the distribution. Must be
#         non-negative.
#     size : int or tuple of ints, optional
#         Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
#         ``m * n * k`` samples are drawn.  If size is ``None`` (default),
#         a single value is returned if ``loc`` and ``scale`` are both scalars.
#         Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
#     
#     Returns
#     -------
#     out : ndarray or scalar
#         Drawn samples from the parameterized normal distribution.

# You can also see some examples of how the function is used by looking further down in the help output. For example, you will find the text:
#
#     Draw samples from the distribution:
#     
#     >>> mu, sigma = 0, 0.1 # mean and standard deviation
#     >>> s = np.random.normal(mu, sigma, 1000)
#
# We can see from the help output (above) that the np.random.normal function has three arguments, loc or mean, scale or standard deviation, and size. These are shown to be equal to specific values. 
#
#     normal(loc=0.0, scale=1.0, size=None)
#     
# This means that those values are the default settings, so that if you don’t do anything, then the function will return a single random number with a mean of 0 and a standard deviation of 1. 
#
#
#

np.random.normal()

# If we wanted to create random numbers with a different mean and standard deviation (say mean == 100 and standard deviation == 15), then we could simply set those values in the function call. Let’s say that we would like 5 random numbers from this distribution:
#

my_random_numbers = np.random.normal(100, 15, 5)
my_random_numbers

# You will see that I set the variable to the name ``my_random_numbers``. In general, it’s always good to be as descriptive as possible when creating variables; rather than calling them x or y, use names that describe the actual contents. This will make it much easier to understand what’s going on once things get more complicated.

# ## Arrays
# You may have noticed that the my_random_numbers created above wasn’t like the variables that we had seen before — it contained several values in it. We refer to this kind of variable as an *array*.
#
# If you want to create your own new array, you can do that using the ``np.array()`` function:

my_array = np.array([4, 5, 6])
my_array

# This kind of array is also known as a vector. It is an array of numbers that only has a single dimension - and can be any number of elements long in that single dimension. It can be a row vector (like ``my_array`` above) or a column vector.
#
# You can access the individual elements within a vector by using square brackets along with a number that refers to the location within the vector. These index values start at 0, a convention of many programming languages that can take a little getting used to. 
#
# Let’s say we want to see the value in the second place of the vector:

my_array[1]

# You can also look at a range of positions, by putting the start and end+1 locations with a colon in between. For example, to see the values in second and third place:

my_array[1:3]

# You can also change the values of specific locations using the same indexing:

my_array[2] = 7
my_array

# ## Math with vectors and matrices
#
# You can apply mathematical operations to the elements of an array in the same way that you apply them to regular variables. 
# Let's say that we want to multiply each element in the array by the number 5:
#

my_array = np.array([4, 5, 6])
my_array_times_five = my_array * 5
my_array_times_five

# You can also apply mathematical operations on pairs of vectors. In this case, each matching element is used for the operation.

my_first_array = np.array([1, 2, 3])
my_second_array = np.array([10, 20, 20])
my_first_array + my_second_array

# We can also apply logical operations across vectors; again, this will return a vector with the operation applied to the pairs of values at each position.

array_a = np.array([1, 2, 3])
array_b = np.array([1, 2, 4])
array_a == array_b

# Most functions will work with vectors just as they would with a single number. For example, let’s say we wanted to obtain the trigonometric sine for each of a set of values. We could create a vector and pass it to the ``np.sin()`` function, which will return as many sine values as there are input values:

my_angle_values = np.array([0, 1, 2])
my_sin_values = np.sin(my_angle_values)
my_sin_values

# ## Dictionaries
# There is another kind of variable in Python that is very useful, which is known as a *dictionary*.  A dictionary is like a container that 
# stores values that are associated with particular *keys*.  A dictionary is created using squiggly brackets; each entry must include a key and a value (which can be any kind of variable, including another dictionary), separated by a color.  For example, let's say that we wanted to store the ages of three people:

ages = {'Lisa': 23, 'Angela': 25, 'Monique': 27}
ages

# To access the elements, we use the names of each field as an index

ages['Lisa']

# ## Data Frames
# Often in a dataset we will have a number of different variables that we want to work with. Instead of having a different named variable that stores each one, it is often useful to combine all of the separate variables into a single package, which is referred to as a data frame.
#
# If you are familiar with a spreadsheet (say from Microsoft Excel) then you already have a basic understanding of a data frame.
# Let’s say that we have values of price and mileage for three different types of cars. We could start by creating a variable for each one, making sure that the three cars are in the same order for each of the variables:

car_model = ("Ford Fusion", "Hyundai Accent", "Toyota Corolla")
car_price = np.array([25000, 16000, 18000])
car_mileage = np.array([27, 36, 32])

# We can then combine these into a single data frame, using the pd.DataFrame() function. I like to use "_df" in the names of data frames just to make clear that it’s a data frame, so we will call this one “cars_df”:

data = {'Price': car_price,
        'Mileage': car_mileage}
cars_df2 = pd.DataFrame(data, index=car_model)
cars_df2


# Each of the columns in the data frame contains one of the variables, with the name that we gave it when we created the data frame. 
# We can access each of those columns using the same ``[ ]`` indexing we use to access arrays, but we can use the column names we 
# specified for the dataframe. For example, if we wanted to access the mileage variable, we would combine the name of the data frame
# with the name of the variable as follows:

cars_df2['Mileage']

# This is just like any other vector, in that we can refer to its individual values using square brackets as we did with regular vectors. For example, if we want the mileage value for the car in the second place:

cars_df2['Mileage'][1]

# Similarly, you can perform operations on the vector. For example, we might want to square all the values in the "Price" column:

np.square(cars_df2['Price'])

# Let's say we don't know the organisation of the dataframe, but we want to see the price of a Toyota Corolla. We can  use filtering to obtain certain values from dataframe.
#
# Specifing the index that corresponds to "Toyota Corolla" gives you all the values for that row of the dataframe. To do this, we need to use the ``.loc`` operator on the data frame.  The first argument to the ``.loc`` operator refers to the rows in the data frame, whereas the second refers to the columns.

cars_df2.loc["Toyota Corolla"]

# To obtain only the mileage, specify the mileage column.

cars_df2.loc[["Toyota Corolla"], ['Mileage']]

# We can also filter by some characteristics of the car.

cars_df2[(cars_df2['Mileage'] > 30) & (cars_df2['Price'] < 18000)]

# Dataframes are enormously powerful for manipulating ("wrangling") large and complex datasets, which are often what we are dealing with in statistics. For further information on dataframes in pandas, see: https://towardsdatascience.com/my-python-pandas-cheat-sheet-746b11e44368

# ## 1.10 Working with data files
# When we are doing statistics, we often need to load in the data that we will analyze. Those data will live in a file on one’s computer or on the internet. For this example, let’s use a file that is hosted on the internet, which contains the gross domestic product (GDP) values for a number of countries around the world. 
# This file is stored as a *comma-separated value* (or CSV) file, meaning that the values for each of the variables in the dataset are separated by commas. There are three variables: the relative rank of the countries, the name of the country, and its GDP value. Here is what the first few lines of the file look like:
# We can load the file using the ``pd.read_csv()`` function:

data_url = 'https://raw.githubusercontent.com/psych10/psych10/master/notebooks/Session03-IntroToR/gdp.csv'
gdp_data = pd.read_csv(data_url)

# A data frame, like every variable in Python is an *object*.  Later in the book we will discuss object-oriented programming, but the important point for now is that objects can both store information and can do things.  Each object has a set of *methods*, which we denote using a period. For example, the data frame has a method called ``.head()`` which will show us the top 5 rows of the data frame:

gdp_data.head()

# If we want to see the list of all of the methods that are associated with a particular object, we can use the ``dir()`` function:

dir(gdp_data)

# This shows a long list of methods; you will learn more about many of these as we progress through the course.
