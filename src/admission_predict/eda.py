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

continuous_values=['SOP','LOR','CGPA','Chance_of_Admit']
discrete_count=['GRE_Score','TOEFL_Score','University_Rating','Research']

ds[continuous_values].describe()
ds[discrete_count].describe()

ds['SOP'].unique().tolist()
ds['LOR'].unique().tolist()
ds['CGPA'].value_counts().count()
ds['Chance_of_Admit'].value_counts().count()
ds['GRE_Score'].value_counts().count()
ds['TOEFL_Score'].value_counts().count()
ds['University_Rating'].unique().tolist()
ds['Research'].unique().tolist()


ds[ds['SOP']==1][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']]
ds[ds['SOP']==1][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].count()
ds[ds['SOP']==1][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].min()
ds[ds['SOP']==1][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].max()
ds[ds['SOP']==1.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']]
ds[ds['SOP']==1.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].count()
ds[ds['SOP']==1.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].min()
ds[ds['SOP']==1.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].max()
ds[ds['SOP']==2][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']]
ds[ds['SOP']==2][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].count()
ds[ds['SOP']==2][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].min()
ds[ds['SOP']==2][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].max()
ds[ds['SOP']==2.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']]
ds[ds['SOP']==2.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].count()
ds[ds['SOP']==2.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].min()
ds[ds['SOP']==2.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].max()
ds[ds['SOP']==3][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']]
ds[ds['SOP']==3][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].count()
ds[ds['SOP']==3][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].min()
ds[ds['SOP']==3][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].max()
ds[ds['SOP']==3.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']]
ds[ds['SOP']==3.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].count()
ds[ds['SOP']==3.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].min()
ds[ds['SOP']==3.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].max()
ds[ds['SOP']==4][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']]
ds[ds['SOP']==4][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].count()
ds[ds['SOP']==4][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].min()
ds[ds['SOP']==4][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].max()
ds[ds['SOP']==4.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']]
ds[ds['SOP']==4.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].count()
ds[ds['SOP']==4.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].min()
ds[ds['SOP']==4.5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].max()
ds[ds['SOP']==5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']]
ds[ds['SOP']==5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].count()
ds[ds['SOP']==5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].min()
ds[ds['SOP']==5][['GRE_Score','TOEFL_Score','University_Rating','LOR','CGPA','Research','Chance_of_Admit']].max()




ds[ds['LOR']==1][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']]
ds[ds['LOR']==1.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']]
ds[ds['LOR']==1.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].count()
ds[ds['LOR']==1.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].min()
ds[ds['LOR']==1.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].max()
ds[ds['LOR']==2][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']]
ds[ds['LOR']==2][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].count()
ds[ds['LOR']==2][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].min()
ds[ds['LOR']==2][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].max()
ds[ds['LOR']==2.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']]
ds[ds['LOR']==2.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].count()
ds[ds['LOR']==2.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].min()
ds[ds['LOR']==2.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].max()
ds[ds['LOR']==3][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']]
ds[ds['LOR']==3][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].count()
ds[ds['LOR']==3][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].min()
ds[ds['LOR']==3][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].max()
ds[ds['LOR']==3.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']]
ds[ds['LOR']==3.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].count()
ds[ds['LOR']==3.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].min()
ds[ds['LOR']==3.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].max()
ds[ds['LOR']==4][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']]
ds[ds['LOR']==4][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].count()
ds[ds['LOR']==4][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].min()
ds[ds['LOR']==4][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].max()
ds[ds['LOR']==4.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']]
ds[ds['LOR']==4.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].count()
ds[ds['LOR']==4.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].min()
ds[ds['LOR']==4.5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].max()
ds[ds['LOR']==5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']]
ds[ds['LOR']==5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].count()
ds[ds['LOR']==5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].min()
ds[ds['LOR']==5][['GRE_Score','TOEFL_Score','University_Rating','SOP','CGPA','Research','Chance_of_Admit']].max()










# Density plot for GRE_Score:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['GRE_Score'],ax=ax) # type: ignore
plt.title("Density plot for GRE_Score")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/gre_dens.png")


# Density plot for TOEFL_Score:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['TOEFL_Score'],ax=ax) # type: ignore
plt.title("Density plot for TOEFL_Score")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/toefl_dens.png")


# Density plot for University_Rating:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['University_Rating'],ax=ax) # type: ignore
plt.title("Density plot for University_Rating")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/univ_dens.png")



# Density plot for SOP:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['SOP'],ax=ax) # type: ignore
plt.title("Density plot for SOP")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/sop_dens.png")


# Density plot for LOR:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['LOR'],ax=ax) # type: ignore
plt.title("Density plot for LOR")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/lor_dens.png")


# Density plot for CGPA:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['CGPA'],ax=ax) # type: ignore
plt.title("Density plot for CGPA")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/cgpa_dens.png")



# Density plot for Research:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['Research'],ax=ax) # type: ignore
plt.title("Density plot for Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/res_dens.png")



# Density plot for Chance_of_Admit:-

fir,ax=plt.subplots(figsize=(10,5))
sns.distplot(ds['Chance_of_Admit'],ax=ax) # type: ignore
plt.title("Density plot for Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Density_plots/coa_dens.png")


'''#############################################################################################'''

# Box plot for GRE_Score:-

fir,ax=plt.subplots(figsize=(10,5))
sns.boxplot(data=ds['GRE_Score'],ax=ax,color='plum') # type: ignore
plt.title("Box plot for GRE_Score")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Box_plots/gre_box.png")


# Box plot for TOEFL_Score:-

fir,ax=plt.subplots(figsize=(10,5))
sns.boxplot(data=ds['TOEFL_Score'],ax=ax,color='peru') # type: ignore
plt.title("Box plot for TOEFL_Score")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Box_plots/toefl_box.png")



# Box plot for University_Rating:-

fir,ax=plt.subplots(figsize=(10,5))
sns.boxplot(data=ds['University_Rating'],ax=ax,color='crimson') # type: ignore
plt.title("Box plot for University_Rating")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Box_plots/univ_box.png")



# Box plot for SOP:-

fir,ax=plt.subplots(figsize=(10,5))
sns.boxplot(data=ds['SOP'],ax=ax,color='navy') # type: ignore
plt.title("Box plot for SOP")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Box_plots/sop_box.png")



# Box plot for LOR:-

fir,ax=plt.subplots(figsize=(10,5))
sns.boxplot(data=ds['LOR'],ax=ax,color='seagreen') # type: ignore
plt.title("Box plot for LOR")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Box_plots/lor_box.png")



# Box plot for CGPA:-

fir,ax=plt.subplots(figsize=(10,5))
sns.boxplot(data=ds['CGPA'],ax=ax,color='cyan') # type: ignore
plt.title("Box plot for CGPA")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Box_plots/cgpa_box.png")



# Box plot for Research:-

fir,ax=plt.subplots(figsize=(10,5))
sns.boxplot(data=ds['Research'],ax=ax,color='olive') # type: ignore
plt.title("Box plot for Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Box_plots/res_box.png")



# Box plot for Chance_of_Admit:-

fir,ax=plt.subplots(figsize=(10,5))
sns.boxplot(data=ds['Chance_of_Admit'],ax=ax,color='pink') # type: ignore
plt.title("Box plot for Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Box_plots/coa_box.png")


'''######################################################################################'''

# Scatter plot for GRE_Score:-

fir,ax=plt.subplots(figsize=(10,5))
sns.scatterplot(data=ds,x='GRE_Score',y='Chance_of_Admit')
plt.title("scatterplot plot for GRE_Score")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Scatter_plots/gre_box.png")



# Scatter plot for TOEFL_Score:-

fir,ax=plt.subplots(figsize=(10,5))
sns.scatterplot(data=ds,x='TOEFL_Score',y='Chance_of_Admit')
plt.title("scatterplot plot for TOEFL_Score")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Scatter_plots/toelf_box.png")



# Scatter plot for University_Rating:-

fir,ax=plt.subplots(figsize=(10,5))
sns.scatterplot(data=ds,x='University_Rating',y='Chance_of_Admit')
plt.title("scatterplot plot for University_Rating")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Scatter_plots/univ_box.png")



# Scatter plot for SOP:-

fir,ax=plt.subplots(figsize=(10,5))
sns.scatterplot(data=ds,x='SOP',y='Chance_of_Admit')
plt.title("scatterplot plot for SOP")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Scatter_plots/sop_box.png")



# Scatter plot for LOR:-

fir,ax=plt.subplots(figsize=(10,5))
sns.scatterplot(data=ds,x='LOR',y='Chance_of_Admit')
plt.title("scatterplot plot for LOR")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Scatter_plots/lor_box.png")



# Scatter plot for CGPA:-

fir,ax=plt.subplots(figsize=(10,5))
sns.scatterplot(data=ds,x='CGPA',y='Chance_of_Admit')
plt.title("scatterplot plot for CGPA")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Scatter_plots/cgpa_box.png")



# Scatter plot for Research:-

fir,ax=plt.subplots(figsize=(10,5))
sns.scatterplot(data=ds,x='Research',y='Chance_of_Admit')
plt.title("scatterplot plot for Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Scatter_plots/res_box.png")



# Scatter plot for GRE_Score:-

fir,ax=plt.subplots(figsize=(10,5))
sns.scatterplot(data=ds,x='GRE_Score',y='Chance_of_Admit')
plt.title("scatterplot plot for GRE_Score")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Scatter_plots/gre_box.png")




