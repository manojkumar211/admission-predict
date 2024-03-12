import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datacleaning import df, ols_method
from sklearn.preprocessing import StandardScaler
import statsmodels.formula.api as smf
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression,ElasticNet,Lasso,LassoCV,Ridge,RidgeCV
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import cross_val_score, cross_validate,GridSearchCV,train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import PolynomialFeatures
from best_random_degree import BestRandomState, BestDegreeValue
from linear_regression import Linear_Regression
from polynomial import Poly_Regression




print(max(BestRandomState.best_random_state_train))
print(BestRandomState.best_random_state_train.index(max(BestRandomState.best_random_state_train)))
print("##"*20)
print(ols_method.summary())
print("##"*20)
print(Linear_Regression.R2_train_score) #type: ignore
print("--"*20)
print(Linear_Regression.R2_test_score) #type: ignore
print("--"*20)
print(Linear_Regression.cross_score.mean()) #type: ignore
print("##"*20)
print(max(BestDegreeValue.lis_poly_train)) #type: ignore
print(BestDegreeValue.lis_poly_train.index()) #type: ignore
print("--"*20)
print(Poly_Regression.R2_train_score_poly) #type: ignore
print(Poly_Regression.R2_test_score_poly) #type: ignore
print(Poly_Regression.cross_score_poly.mean()) #type: ignore


