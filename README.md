# Quantamentals Factor Investing with K-Means Clustering

In this research, we explore factor investing in a Quantamentals framework. We combine technical and fundamentals factors together
to create a new investment strategy under Quantamentals, moving away from idiosyncractic factor investing. We apply K-means clustering
to partition assets according to famous factors. Our goal is to analyze which cluster would allow one to enjoy abnormal returns without
too much risk. We provide 

## Data Source

Our research requires Norgate Data and Sharadar Data. We use Norgate for total return adjusted stock prices and also for historical
constieunts. We use Sharadar for fundamental data. 

To acquire Norgate Data, it is required that you have to subsribe to atleast the Platinum package that includes the daily prices and
active/delisted data. More information can be found here: https://norgatedata.com/prices.php. Norgate Data comes with their software
called the NDU that manages our data on local servers and allows us to use an api to query data: https://pypi.org/project/norgatedata/
For more information on all the contents from Norgate see https://norgatedata.com/data-content-tables.php.

To acquire Sharadar, you can subscribe from their website or you can also subsribe via Quandl. For us, we use Sharadar's Core US
Fundamentals Data: https://www.quandl.com/databases/SF1/data. We download CSV files from Quandl and import the files via the Jupyter
Notebook. On the Quandl website, Sharadar provides a neat documentation that can be referenced here https://www.quandl.com/databases/SF1/documentation. 

## Development on Jupyter Notebooks

For our devopment, we use Jupyter Notebooks. Below is the list of all Jupyter Notebooks that we implemented and we order them so that
you can follow the pipeline in steps. 

### Importing Data

#### Importing_PriceVolumeConstieunts.ipynb

Here, we start off by constructing price, volume, and constituents from Norgate Data. 

#### Importing_QualityValue.ipynb

We explore the nomenclature of Norgate and Sharadar in this notebook. We implemented a communications gateway to reference symbols names 
from Norgate and Sharadar. We also import fundamental data from Sharadar. 

### Feature Engineering

#### Feature_Eng_Momentum_Volatility.ipynb

We tranform our price series to cross-sectional momentum and volatility factors. Addtionally, we also compute the average 200 day volume. 

#### Feature_Eng_Sharadar.ipynb

We rename our fundamental dataframes according to Norgate's. 

#### Combining Factors.ipynb

We construct an all factors dataframe from 2002-01-01 til 2020-09-29 with all historical constituents of Russell 3000.

### Implementing K-Means

#### K-Means_Factor_Clustering_Final.ipynb

We construct our K-means algorithm and apply it on monthly observations of factors dataframe. 

### Backtesting

#### QVV_cluster_backtest_Final.ipynb

Here, we backtest the clusters analyzing quality, volatility, and value factors

#### QVV_plusMOM_backtest_Final.ipynb

We add on to the previous backtest, incorporating cross-sectional momentum and time-series momentum. 

## Libraries and Dependencies

1. norgate.py - module for pulling historical price
2. numpy-1.18.5
3. pandas-1.0.4
4. norgatedata-1.0.31 - library for handling Norgate Data
5. datetime 
6. pickle
7. matplotlib-3.0.1
8. scipy-1.2.1
9. sklearn-0.23.2
10. random 
11. plotly-4.11.0




