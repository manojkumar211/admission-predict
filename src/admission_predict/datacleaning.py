import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataload import ds
from iqr import lor_outliers,coa_outliers
import statsmodels.formula.api as smf




df=ds.copy()

df[(df['LOR']<lor_outliers.lor_lower_bound) | (df['LOR']>lor_outliers.lor_upper_bound)] # type: ignore

df.drop(index=347)

df['LOR']=df['LOR'].clip(lower=lor_outliers.lor_lower_bound,upper=lor_outliers.lor_upper_bound) # type: ignore


df[(df['Chance_of_Admit']<coa_outliers.coa_lower_bound) | (df['Chance_of_Admit']>coa_outliers.coa_upper_bound)] # type: ignore

df.drop(index=[92,376])

df['Chance_of_Admit']=df['Chance_of_Admit'].clip(lower=coa_outliers.coa_lower_bound,upper=coa_outliers.coa_upper_bound) # type: ignore


X=df.drop(columns=['Serial No.','Chance_of_Admit','SOP'])
y=df['Chance_of_Admit']

ols_method=smf.ols(formula='y~X',data=ds).fit()


