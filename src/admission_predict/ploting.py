import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataload import ds



# GRE_Score and TOEFL_Score plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['GRE_Score','TOEFL_Score']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between GRE_Score and TOEFL_Score")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_toefl_heatmap.png")


# GRE_Score and University_Rating plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['GRE_Score','University_Rating']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between GRE_Score and University_Rating")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_univ_heatmap.png")


# GRE_Score and SOP plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['GRE_Score','SOP']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between GRE_Score and SOP")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_sop_heatmap.png")


# GRE_Score and LOR plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['GRE_Score','LOR']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between GRE_Score and LOR")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_lor_heatmap.png")



# GRE_Score and CGPA plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['GRE_Score','CGPA']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between GRE_Score and CGPA")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_cgpa_heatmap.png")



# GRE_Score and Research plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['GRE_Score','Research']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between GRE_Score and Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_res_heatmap.png")



# GRE_Score and Chance_of_Admit plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['GRE_Score','Chance_of_Admit']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between GRE_Score and Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_coa_heatmap.png")


'''#####################################################################################################'''



# TOEFL_Score and University_Rating plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['TOEFL_Score','University_Rating']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between TOEFL_Score and University_Rating")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_univ_heatmap.png")



# TOEFL_Score and SOP plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['TOEFL_Score','SOP']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between TOEFL_Score and SOP")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_sop_heatmap.png")


# TOEFL_Score and LOR plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['TOEFL_Score','LOR']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between TOEFL_Score and LOR")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_lor_heatmap.png")



# TOEFL_Score and CGPA plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['TOEFL_Score','CGPA']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between TOEFL_Score and CGPA")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_cgpa_heatmap.png")



# TOEFL_Score and Research plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['TOEFL_Score','Research']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between TOEFL_Score and Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_res_heatmap.png")



# TOEFL_Score and Chance_of_Admit plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['TOEFL_Score','Chance_of_Admit']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between TOEFL_Score and Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_coa_heatmap.png")


'''#####################################################################################################'''


# University_Rating and SOP plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['University_Rating','SOP']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between University_Rating and SOP")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/University/univ_sop_heatmap.png")


# University_Rating and LOR plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['University_Rating','LOR']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between University_Rating and LOR")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/University/univ_lor_heatmap.png")



# University_Rating and CGPA plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['University_Rating','CGPA']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between University_Rating and CGPA")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/University/univ_cgpa_heatmap.png")



# University_Rating and Research plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['University_Rating','Research']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between University_Rating and Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/University/univ_res_heatmap.png")



# University_Rating and Chance_of_Admit plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['University_Rating','Chance_of_Admit']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between University_Rating and Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/University/univ_coa_heatmap.png")


'''#####################################################################################################'''


# SOP and LOR plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['SOP','LOR']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between SOP and LOR")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/SOP/sop_lor_heatmap.png")


# SOP and CGPA plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['SOP','CGPA']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between SOP and CGPA")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/SOP/sop_cgpa_heatmap.png")


# SOP and Research plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['SOP','Research']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between SOP and Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/SOP/sop_res_heatmap.png")


# SOP and Chance_of_Admit plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['SOP','Chance_of_Admit']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between SOP and Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/SOP/sop_coa_heatmap.png")


'''#####################################################################################################'''


# LOR and CGPA plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['LOR','CGPA']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between LOR and CGPA")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/LOR/lor_cgpa_heatmap.png")


# LOR and Research plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['LOR','Research']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between LOR and Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/LOR/lor_res_heatmap.png")


# LOR and Chance_of_Admit plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['LOR','Chance_of_Admit']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between LOR and Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/LOR/lor_coa_heatmap.png")

'''#####################################################################################################'''

# CGPA and Research plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['CGPA','Research']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between CGPA and Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/CGPA/cgpa_res_heatmap.png")


# CGPA and Chance_of_Admit plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['CGPA','Chance_of_Admit']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between CGPA and Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/CGPA/cgpa_coa_heatmap.png")

'''#####################################################################################################'''

# Research and Chance_of_Admit plot:-

fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=ds[['Research','Chance_of_Admit']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Correlation between Research and Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/Research/res_coa_heatmap.png")


