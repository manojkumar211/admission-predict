import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataload import ds



# GRE_Score and TOEFL_Score plot:-

sns.heatmap(data=ds[['GRE_Score','TOEFL_Score']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between GRE_Score and TOEFL_Score")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_toefl_heatmap.png")


# GRE_Score and University_Rating plot:-

sns.heatmap(data=ds[['GRE_Score','University_Rating']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between GRE_Score and University_Rating")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_univ_heatmap.png")


# GRE_Score and SOP plot:-

sns.heatmap(data=ds[['GRE_Score','SOP']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between GRE_Score and SOP")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_sop_heatmap.png")


# GRE_Score and LOR plot:-

sns.heatmap(data=ds[['GRE_Score','LOR']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between GRE_Score and LOR")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_lor_heatmap.png")



# GRE_Score and CGPA plot:-

sns.heatmap(data=ds[['GRE_Score','CGPA']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between GRE_Score and CGPA")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_cgpa_heatmap.png")



# GRE_Score and Research plot:-

sns.heatmap(data=ds[['GRE_Score','Research']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between GRE_Score and Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_res_heatmap.png")



# GRE_Score and Chance_of_Admit plot:-

sns.heatmap(data=ds[['GRE_Score','Chance_of_Admit']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between GRE_Score and Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/GRE_score/gre_coa_heatmap.png")


'''#####################################################################################################'''



# TOEFL_Score and University_Rating plot:-

sns.heatmap(data=ds[['TOEFL_Score','University_Rating']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between TOEFL_Score and University_Rating")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_univ_heatmap.png")



# TOEFL_Score and SOP plot:-

sns.heatmap(data=ds[['TOEFL_Score','SOP']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between TOEFL_Score and SOP")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_sop_heatmap.png")


# TOEFL_Score and LOR plot:-

sns.heatmap(data=ds[['TOEFL_Score','LOR']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between TOEFL_Score and LOR")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_lor_heatmap.png")



# TOEFL_Score and CGPA plot:-

sns.heatmap(data=ds[['TOEFL_Score','CGPA']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between TOEFL_Score and CGPA")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_cgpa_heatmap.png")



# TOEFL_Score and Research plot:-

sns.heatmap(data=ds[['TOEFL_Score','Research']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between TOEFL_Score and Research")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_res_heatmap.png")



# TOEFL_Score and Chance_of_Admit plot:-

sns.heatmap(data=ds[['TOEFL_Score','Chance_of_Admit']].corr(),cmap='tab20',annot=True)
plt.title("Correlation between TOEFL_Score and Chance_of_Admit")
plt.savefig("E:/NareshiTech/admission_predict/visual_plot/TOELF_score/toefl_coa_heatmap.png")


'''#####################################################################################################'''




