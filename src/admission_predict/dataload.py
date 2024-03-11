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

ds=ds.rename(columns={'GRE Score':'GRE_Score','TOEFL Score':'TOEFL_Score','University Rating':'University_Rating','LOR ':'LOR','Chance of Admit ':'Chance_of_Admit'})

ds.head()
ds.columns.to_list()
ds.count()
ds.corr()
ds[['GRE_Score','TOEFL Score']].corr()
ds[['GRE_Score','University Rating']].corr()
ds[['GRE_Score','SOP']].corr()
ds[['GRE_Score','LOR']].corr()
ds[['GRE_Score','CGPA']].corr()
ds[['GRE_Score','Research']].corr()
ds[['GRE_Score','Chance_of_Admit']].corr()
ds[['TOEFL_Score','University_Rating']].corr()
ds[['TOEFL_Score','SOP']].corr()
ds[['TOEFL_Score','LOR']].corr()
ds[['TOEFL_Score','CGPA']].corr()
ds[['TOEFL_Score','Research']].corr()
ds[['TOEFL_Score','Chance_of_Admit']].corr()







