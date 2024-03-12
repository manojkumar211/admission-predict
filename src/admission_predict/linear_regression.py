from re import T
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datacleaning import df
from sklearn.preprocessing import StandardScaler
import statsmodels.formula.api as smf
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression,ElasticNet,Lasso,LassoCV,Ridge,RidgeCV
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import cross_val_score, cross_validate,GridSearchCV,train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import PolynomialFeatures



X=df.drop(columns=['Serial No.','Chance_of_Admit','SOP'])
y=df['Chance_of_Admit']


class Linear_Regression:

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=True)

    lr=LinearRegression()
    lr.fit(X_train,y_train)
    lr_intercept=lr.intercept_
    lr_coefficient=lr.coef_
    train_pred=lr.predict(X_train)
    train_score=lr.score(X_train,y_train)
    R2_train_score=r2_score(y_train,train_pred)
    test_pred=lr.predict(X_test)
    test_score=lr.score(X_test,y_test)
    R2_test_score=r2_score(y_test,test_pred)
    cross_score=cross_val_score(lr,X,y,cv=5)
    train_residual=y_train-train_pred
    test_residual=y_test-test_pred
    
    def __init__(self,lr,lr_intercept,lr_coefficient,train_pred,train_score,R2_train_score,test_pred,test_score,R2_test_score,
                 cross_score,train_residual,test_residual):
        
        self.lr=lr
        self.lr_intercept=lr_intercept
        self.lr_coefficient=lr_coefficient
        self.train_pred=train_pred
        self.train_score=train_score
        self.R2_train_score=R2_train_score
        self.test_pred=test_pred
        self.test_score=test_score
        self.R2_test_score=R2_test_score
        self.cross_score=cross_score
        self.train_residual=train_residual
        self.test_residual=test_residual

    def linear_model(self):
        return self.lr
    
    def linear_intercept(self):
        return self.lr_intercept
    
    def linear_coefficient(self):
        return self.lr_coefficient
    
    def train_prediction(self):
        return self.train_pred
    
    def train_scoring(self):
        return self.train_score
    
    def R2_training_scoring(self):
        return self.R2_train_score
    
    def test_prediction(self):
        return self.test_pred
    
    def test_scoring(self):
        return self.test_score
    
    def R2_testing_scoring(self):
        return self.R2_test_score
    
    def cross_validation_scoring(self):
        return self.cross_score
    
    def training_residual_values(self):
        return self.train_residual
    
    def testing_residual_values(self):
        return self.test_residual
    
