import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataload import ds



# Outliers in LOR column:-

class lor_outliers:

    
    lor_q1=ds['LOR'].quantile(q=0.25)
    lor_q2=ds['LOR'].quantile(q=0.50)
    lor_q3=ds['LOR'].quantile(q=0.75)
    

    lor_iqr=lor_q3-lor_q1

    lor_lower_bound=lor_q1-(1.5*lor_iqr)

    lor_upper_bound=lor_q3+(1.5*lor_iqr)


    def __init__(self,lor_q1,lor_q2,lor_q3,lor_iqr,lor_lower_bound,lor_upper_bound,lor_after_list,lor_outlies_list):
        
        self.lor_q1=lor_q1
        self.lor_q2=lor_q2
        self.lor_q3=lor_q3
        self.lor_iqr=lor_iqr
        self.lor_lower_bound=lor_lower_bound
        self.lor_upper_bound=lor_upper_bound
        
        
    def lor_quantile_one(self):
        return self.lor_q1
    def lor_quantile_two(self):
        return self.lor_q2
    def lor_quantile_three(self):
        return self.lor_q3
    def lor_inter_quantile_range(self):
        return self.lor_iqr
    def lor_lower_fen(self):
        return self.lor_lower_bound
    def lor_upper_fen(self):
        return self.lor_upper_bound
   




# Outliers in Chance_of_Admit column:-


class coa_outliers:

    
    coa_q1=ds['Chance_of_Admit'].quantile(q=0.25)
    coa_q2=ds['Chance_of_Admit'].quantile(q=0.50)
    coa_q3=ds['Chance_of_Admit'].quantile(q=0.75)
    

    coa_iqr=coa_q3-coa_q1

    coa_lower_bound=coa_q1-(1.5*coa_iqr)

    coa_upper_bound=coa_q3+(1.5*coa_iqr)

    
    def __init__(self,coa_q1,coa_q2,coa_q3,coa_iqr,coa_lower_bound,coa_upper_bound):
        
        self.coa_q1=coa_q1
        self.coa_q2=coa_q2
        self.coa_q3=coa_q3
        self.coa_iqr=coa_iqr
        self.coa_lower_bound=coa_lower_bound
        self.coa_upper_bound=coa_upper_bound
        
        
        
    def coa_quantile_one(self):
        return self.coa_q1
    def coa_quantile_two(self):
        return self.coa_q2
    def coa_quantile_three(self):
        return self.coa_q3
    def coa_inter_quantile_range(self):
        return self.coa_iqr
    def coa_lower_fen(self):
        return self.coa_lower_bound
    def coa_upper_fen(self):
        return self.coa_upper_bound
    
  

