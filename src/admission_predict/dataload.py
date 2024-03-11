import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import ElasticNet,Lasso,LinearRegression,Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score,train_test_split
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy import stats
from statsmodels.stats.weightstats import ztest
from scipy.stats import ttest_1samp,chi2_contingency,binomtest,f_oneway


# Data Loading:-

ds=pd.read_csv("E:/NareshiTech/admission_predict.csv")
ds.head()

