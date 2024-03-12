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


class Poly_Regression:

    Xp_train,Xp_test,yp_train,yp_test=train_test_split(X,y,test_size=0.2,random_state=True)

    poly_regression=PolynomialFeatures(degree=7)
    train_poly=pd.DataFrame(poly_regression.fit_transform(Xp_train))
    test_poly=pd.DataFrame(poly_regression.transform(Xp_test)) # type: ignore

    lr_poly=LinearRegression()
    lr_poly.fit(train_poly,yp_train)
    lr_poly_intercept=lr_poly.intercept_
    lr_poly_coefficient=lr_poly.coef_
    train_pred_poly=lr_poly.predict(train_poly)
    train_score_poly=lr_poly.score(train_poly,yp_train)
    R2_train_score_poly=r2_score(yp_train,train_pred_poly)
    test_pred_poly=lr_poly.predict(test_poly)
    test_score_poly=lr_poly.score(test_poly,yp_test)
    R2_test_score_poly=r2_score(yp_test,test_pred_poly)
    cross_score_poly=cross_val_score(lr_poly,X,y,cv=5)
    train_residual_poly=yp_train-train_pred_poly
    test_residual_poly=yp_test-test_pred_poly
    

    def __init__(self,lr_poly,lr_poly_intercept,lr_poly_coefficient,train_pred_poly,train_score_poly,R2_train_score_poly,test_pred_poly,test_score_poly,R2_test_score_poly,
                 cross_score_poly,train_residual_poly,test_residual_poly):
        
        self.lr_poly=lr_poly
        self.lr_poly_intercept=lr_poly_intercept
        self.lr_poly_coefficient=lr_poly_coefficient
        self.train_pred_poly=train_pred_poly
        self.train_score_poly=train_score_poly
        self.R2_train_score_poly=R2_train_score_poly
        self.test_pred_poly=test_pred_poly
        self.test_score_poly=test_score_poly
        self.R2_test_score_poly=R2_test_score_poly
        self.cross_score_poly=cross_score_poly
        self.train_residual_poly=train_residual_poly
        self.test_residual_poly=test_residual_poly

    def linear_model_poly(self):
        return self.lr_poly
    
    def linear_intercept_poly(self):
        return self.lr_poly_intercept
    
    def linear_coefficient_poly(self):
        return self.lr_poly_coefficient
    
    def train_prediction_poly(self):
        return self.train_pred_poly
    
    def train_scoring_poly(self):
        return self.train_score_poly
    
    def R2_training_scoring_poly(self):
        return self.R2_train_score_poly
    
    def test_prediction_poly(self):
        return self.test_pred_poly
    
    def test_scoring_poly(self):
        return self.test_score_poly
    
    def R2_testing_scoring_poly(self):
        return self.R2_test_score_poly
    
    def cross_validation_scoring_poly(self):
        return self.cross_score_poly
    
    def training_residual_values_poly(self):
        return self.train_residual_poly
    
    def testing_residual_values_poly(self):
        return self.test_residual_poly