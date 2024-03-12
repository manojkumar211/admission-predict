import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataload import ds



ds.describe()
ds.dtypes
ds.duplicated().sum()
ds.info()
ds.isnull().sum()
ds.std()
ds.skew()



# Density plot for GRE_Score:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['GRE_Score'],ax=ax)
plt.title("Density plot for GRE_Score")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/gre_dens.png")


# Density plot for TOEFL_Score:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['TOEFL_Score'],ax=ax)
plt.title("Density plot for TOEFL_Score")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/toefl_dens.png")


# Density plot for University_Rating:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['University_Rating'],ax=ax)
plt.title("Density plot for University_Rating")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/univ_dens.png")



# Density plot for SOP:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['SOP'],ax=ax)
plt.title("Density plot for SOP")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/sop_dens.png")


# Density plot for LOR:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['LOR'],ax=ax)
plt.title("Density plot for LOR")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/lor_dens.png")


# Density plot for CGPA:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['CGPA'],ax=ax)
plt.title("Density plot for CGPA")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/cgpa_dens.png")



# Density plot for Research:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['Research'],ax=ax)
plt.title("Density plot for Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/res_dens.png")



# Density plot for Chance_of_Admit:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['Chance_of_Admit'],ax=ax)
plt.title("Density plot for Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/coa_dens.png")


'''#############################################################################################'''




