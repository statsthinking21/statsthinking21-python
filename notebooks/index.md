# Preface

**NOTE**: This book is a work in progress!  Please check back regularly for updates.

This book is a companion to [Statistical Thinking for the 21st Century](https://statsthinking21.org/), an open source statistical textbook. It focuses on the use of the Python statistical programming language for statistics and data analysis.   


## Why Python?

The original companion to *Statistical Thinking for the 21st Century* was written using the R programming language. R is very popular for statistical data analysis --- so why would we go to the trouble of creating a whole new guide for the Python language?  The main reason is that Python is a serious *general-purpose* programming language, whereas R is much more tailored for data analysis and statistics.  This means that if you learn to program in Python, you can do much more than you can using R.  

Most serious software engineers would agree with me that Python is a much better language for programming in general compared to R. One of the main reasons that I prefer Python is that it is much pickier than R; in some cases R will allow the programmer to do something wrong and quietly return a nonsensical result, whereas Python would alert the programmer that something is wrong by raising an error.

Finally, one important benefit of using Python is that it doesn't prevent you from using R when you need it!  There is a Python library called [rpy2](https://rpy2.github.io/) that allows one to call R functions directly from within Python.  Thus, if there is a tool that is only available in R, you can use it from within Python.

## The golden age of data

Throughout this book I have tried when possible to use examples from real data.  This is now very easy because we are swimming in open datasets, as governments, scientists, and companies are increasingly making data freely available.  I think that using real datasets is important because it prepares students to work with real data rather than toy datasets, which I think should be one of the major goals of statistical training. It also helps us realize (as we will see at various points throughout the book) that data don't always come to us ready to analyze, and often need *wrangling* to help get them into shape.  Using real data also shows that the idealized statistical distributions often assumed in statistical methods don't always hold in the real world -- for example, as we will see in Chapter \@ref(summarizing-data), distributions of some real-world quantities (like the number of friends on Facebook) can have very long tails that can break many standard assumptions.  

I apologize up front that the datasets are heavily US-centric.  This is primarily because the best dataset for many of the demonstrations is the National Health and Nutrition Examination Surveys (NHANES) dataset that is available as an R package, and because many of the other complex datasets included in R (such as those in the `fivethirtyeight` package) are also based in the US.  If you have suggestions for datasets from other regions, please pass them along to me!

## An open source book

This book is meant to be a living document, which is why its source is available online at [https://github.com/statsthinking21/statsthinking21-python](https://github.com/statsthinking21/statsthinking21-python).  If you find any errors in the book or want to make a suggestion for how to improve it, please open an issue on the Github site. Even better, submit a pull request with your suggested change.  

The book is licensed according to the [Creative Commons Attribution 2.0 Generic (CC BY 2.0) License](https://creativecommons.org/licenses/by/2.0/).  Please see the terms of that license for more details. 

## Acknowledgements

Thanks to everyone who has contributed to this project: John Butler, ...

