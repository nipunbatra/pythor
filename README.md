## PyThor- Python meets R

Python is fanstastc! So, is R. R contains so many awesome packages that aren't available in Python. Can we get the best of both the worlds? This repository contains recipes for using RPY2 and writing your own wrapper around R packages, so that you can use them conveniently within your Python environment. Read the introductory blog post [here](http://nipunbatra.github.io/2016/01/pythor/).

Here is a sample `R` code you'd write for fitting a linear model.
```R
fit <- lm('eruptions ~ waiting', data=faithful_geyser)
predicted <- predict(fit, newdata=tail(faithful_geyser))
```

Here is the Python code you'll now have to write with the Pythor recipe in place.
```python
pylm = PYLM()
relationship='eruptions~waiting'
pylm.fit(relationship, faithful_pandas_df)
pylm.predict(faithful_pandas_df.tail(5))
```

As simple as it gets. Obviously, there are many awesome packages in Python which provide linear fitting methods. But, this was just an illustration. 

### Current list of R packages interfaced (maybe partially) in PyThor
1. [Linear Model (lm)](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html)
2. [Seasonal decomposition of time series by LOESS (stl)](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/stl.html)

