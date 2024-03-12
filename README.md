# About Data:-
```
In this data set, We are having total 9 features including serial number and 500 rows.
```

# Columns:-
```
- **Serial No.:** Its jest serial number only. So, we can igone this column.

- **GRE Score:** Graduate Record Examination, which means GRE, is an important step in the graduate school or business school application process.

- **TOEFL Score:** Test of English as a Foreign Language, which means TOEFL, is an important step in the test for communications language of the applicants.

- **University Rating:** Every University has a its own rating based on pass percentage of the students rating.

- **SOP:** Statement of Purpose, (SOP) is a document that students prepare to demonstrate why they are applying to a specific course at a specific university. SOP aims to comprehend a candidate's background, reasons for choosing a particular career route, and objectives.

- **LOR:** Letter of Recommendation or LOR is a document that provides the admission officers with a comprehensive insight into your suitable candidature, for admission into the concerned University.  It aims to provide a favourable picture of your academic performance, strengths, experiences, achievements, contributions, and skills.

- **CGPA:** Cumulative Grade Point Average, For schools and colleges, CGPA is used to measure the overall academic achievement of a student by awarding A, B, C, D or F grades. CGPA is a calculation of the average grade point obtained in all subjects except in additional subjects as per the study scheme.

- **Research:** The Research column is shown whether person has done the any kind of research or not.

- **Chance of Admit:** This Chance of Admit column is shown whether person will get the admission or not based on above parameters.

```


# Observations:-

## Correlation between columns:-
### GRE_Score (Graduate Record Examination):-
```
- columns are not having any null values. so, we can good to go.

- GRE & TOEFL scores are having 0.8272% of correlation between them.
- GRE scores & University Rating are having 0.635376% of correlation between them.
- GRE scores & SOP are having **0.613498%** of correlation between them.
- GRE scores & LOR are having **0.524679%** of correlation between them.
- GRE scores & CGPA are having **0.825878%** of correlation between them.
- GRE scores & CGPA are having **0.563398%** of correlation between them.
- GRE scores & Chance_of_Admit are having **0.810351%** of correlation between them.

- (GRE score & TOEFL score), (GRE score & CGPA score) and (GRE scores & Chance_of_Admit) are having high correlation with respect to the **0.827% and 0.825% and 0.810351%**.
- GRE scores & LOR are having less correlation with respect **0.524679%**.
```
### TOEFL_Score (Test of English as a Foreign Language):-
```
- TOEFL_Score & University_Rating columns are having **0.649799%** of correlation between them.
- TOEFL_Score & SOP columns are having **0.64441%** of correlation between them.
- TOEFL_Score & LOR columns are having **0.541563%** of correlation between them.
- TOEFL_Score & CGPA columns are having **0.810574%** of correlation between them.
- TOEFL_Score & Research columns are having **0.467012%** of correlation between them.
- TOEFL_Score & Chance_of_Admit columns are having **0.792228%** of correlation between them.

- (TOEFL_Score & CGPA) and (TOEFL_Score & Chance_of_Admit) are having high correlation with respect to the **0.810574% and 0.792228%**.
- TOEFL_Score & Research are having less correlation with respect to the **0.467012%**.
```
### University_Rating:-
```
- University_Rating & SOP columns are having **0.728024%** of correlation between them.
- University_Rating & LOR columns are having **0.608651%** of correlation between them.
- University_Rating & CGPA columns are having **0.705254%** of correlation between them.
- University_Rating & Research columns are having **0.427047%** of correlation between them.
- University_Rating & Chance_of_Admit columns are having **0.690132%** of correlation between them.

- (University_Rating & SOP) and (University_Rating & CGPA) are having high correlation with respect to the **0.728024% and 0.705254%**.
- University_Rating & Research are having less correlation with respect to the **0.427047%**.
```
### SOP (Statement of Purpose):-
```
- SOP & LOR columns are having **0.663707%** of correlation between them.
- SOP & CGPA columns are having **0.712154%** of correlation between them.
- SOP & Research columns are having **0.408116%** of correlation between them.
- SOP & Chance_of_Admit columns are having **0.684137%** of correlation between them.

- SOP & CGPA are having high correlation with respect to the **0.712154%**.
- SOP & Research are having less correlation with respect to the **0.408116%**.

```
### LOR (Letter of Recommendation):-
```
- LOR & CGPA columns are having **0.637469%** of correlation between them.
- LOR & Research columns are having **0.372526%** of correlation between them.
- LOR & Chance_of_Admit columns are having **0.645365%** of correlation between them.

- LOR & Chance_of_Admit are having high correlation with respect to the **0.645365%**.
- LOR & Research are having less correlation with respect to the **0.372526%**.
```
### CGPA (Cumulative Grade Point Average):-
```
- CGPA & Research columns are having **0.501311%** of correlation between them.
- CGPA & Chance_of_Admit columns are having **0.882413%** of correlation between them.

- CGPA & Chance_of_Admit are having high correlation with respect to the **0.882413%**.
- CGPA & Research are having less correlation with respect to the **0.501311%**.
```

### Research:-
```
- Research & Chance_of_Admit columns are having **0.545871%** of correlation between them.
```

# EDA:-
```
- All columns are having simular values for mean & 50% percentile of the except Research column. might there is a chance of having skewed data in Reseach column.

- **GRE_Score,TOEFL_Score,University_Rating,Research** This are columns are having with discrete count values.
- **SOP,LOR,CGPA,Chance_of_Admit** This are columns are having with discrete continuous values.

- There is no any duplicated values are presents in this data set.

- In ths data set, we have total 500 row and 9 columns. But we are not going to include serial number column. so, after ignoring serial number column we get 8 columns in this data set.

- Non of the column having null values.

# STD:-

- **Standard deviation is a number that describes how spread out the values are.**
- **A low standard deviation means that most of the numbers are close to the mean (average) value.**
- **A high standard deviation means that the values are spread out over a wider range.**

- GRE_Score column std values are within the range of 11.295148 from the mean, which mean - 316.472000.	
- TOEFL_Score column std values are within the range of 6.081868 from the mean, which mean - 107.192000.
- University_Rating column std values are within the range of 1.143512 from the mean, which mean - 3.114000.
- SOP column std values are within the range of 0.991004 from the mean, which mean - 3.374000.
- LOR column std values are within the range of 0.925450 from the mean, which mean - 3.48400.
- CGPA column std values are within the range of 0.604813 from the mean, which mean - 8.576440.
- Research column std values are within the range of 0.496884 from the mean, which mean - 0.560000.
- Chance_of_Admit column std values are within the range of 0.141140 from the mean, which mean - 0.72174.

# skew():-

- Skewness seems, for every column elements are symmetrically distributed. 

```
## Density plot:-
```
- The Density plot for GRE_Score seems to be symmetric distribution.
- The Density plot for TOEFL_Score seems to be symmetric distribution.
- The Density plot for University_Rating seems to be symmetric distribution.
- The Density plot for SOP seems to be symmetric distribution.
- The Density plot for LOR seems to be symmetric distribution.
- The Density plot for CGPA seems to be symmetric distribution.
- The Density plot for Research seems to be symmetric distribution.
- The Density plot for Chance_of_Admit seems to be small skewed distribution.
```
## Box Plotting:-
```
- There is no any outliers in the GRE_Score column.
- There is no any outliers in the TOEFL_Score column.
- There is no any outliers in the University_Rating column.
- There is no any outliers in the SOP column.
- There is one outliers in the LOR column and it presents in the lower boundary.
- There is no any outliers in the CGPA column.
- There is no any outliers in the Research column.
- There is one outliers in the Chance_of_Admit column and it presents in the lower boundary.
```
## Scatter Plotting:-
```
- Relationship between GRE_Score & Chance_of_Admit having passitive correlation.
- Relationship between TOEFL_Score & Chance_of_Admit having passitive correlation.
- There is no relationship between University_Rating & Chance_of_Admit.
- There is no relationship between SOP & Chance_of_Admit.
- There is no relationship between LOR & Chance_of_Admit.
- Relationship between CGPA & Chance_of_Admit having passitive correlation.
- There is no relationship between Research & Chance_of_Admit.
```
# Filtering:-
```
# Unique Values:- 

- In SOP column, we are having 9 unique values.
- In LOR column, we are having 9 unique values.
- In CGPA column, we are having 184 unique values. so, we can't able apply the filter method.
- In Chance_of_Admit column, we are having 61 unique values. so, we can't able apply the filter method.
- In GRE_Score column, we are having 49 unique values. so, we can't able apply the filter method.
- In TOEFL_Score column, we are having 29 unique values. so, we can't able apply the filter method.
- In University_Rating column, we are having 5 unique values.
- In Research column, we are having 2 unique values.

# SOP==1:-
- In SOP==1, **(GRE_Score-299 to 312, TOEFL_Score-94 to 105, University_Rating-1 & 2, LOR-1 to 2, CGPA-7.34 to 8.01, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.42 to 0.58 only and in this parameter 6 record are there.

# SOP==1.5:-
- In SOP==1, **(GRE_Score-290 to 332, TOEFL_Score-93 to 112, University_Rating-1 & 4, LOR-1.50 to 4, CGPA-7.23 to 8.66, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.42 to 0.79 only and in this parameter 25 record are there.

# SOP==2:-
- In SOP==2, **(GRE_Score-290 to 329 TOEFL_Score-92 to 114, University_Rating-1 to 4, LOR-1.50 to 4.50, CGPA-7.20 to 8.74, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.36 to 0.81 only and in this parameter 43 record are there.

# SOP==2.5:-
- In SOP==2.5, **(GRE_Score-5 to 324 TOEFL_Score-94 to 112, University_Rating-1 to 4, LOR-1.50 to 4.50, CGPA-7.43 to 9.02, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.34 to 0.80 only and in this parameter 64 record are there.

# SOP==3:-
- In SOP==3, **(GRE_Score-296 to 338 TOEFL_Score-95 to 118, University_Rating-1 to 5, LOR-1.50 to 5, CGPA-6.80 to 9.40, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.36 to 0.91 only and in this parameter 80 record are there.

# SOP==3.5:-
- In SOP==3.5, **(GRE_Score-298 to 338 TOEFL_Score-98 to 117, University_Rating-1 to 5, LOR-2 to 5, CGPA-7.68 to 9.46, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.45 to 0.91 only and in this parameter 88 record are there.

# SOP==4:-
- In SOP==4, **(GRE_Score-298 to 340 TOEFL_Score-98 to 120, University_Rating-2 to 5, LOR-2.50 to 5, CGPA-7.60 to 9.87, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.34 to 0.97 only and in this parameter 89 record are there.

# SOP==4.5:-
- In SOP==4.5, **(GRE_Score-308 to 340 TOEFL_Score-102 to 120, University_Rating-2 to 5, LOR-3 to 5, CGPA-8.14 to 9.92, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.57 to 0.97 only and in this parameter 63 record are there.

# SOP==5:-
- In SOP==5, **(GRE_Score-299 to 340 TOEFL_Score-97 to 120, University_Rating-3 to 5, LOR-3.00 to 5, CGPA-7.66 to 9.87, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.38 to 0.96 only and in this parameter 42 record are there.

# LOR==1:-
- In LOR==1, **(GRE_Score-299 TOEFL_Score-94, University_Rating-1, SOP-1.0, CGPA-7.34, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.42 only and in this parameter 1 record are there.

# LOR==1.5:-
- In LOR==1.5, **(GRE_Score-294 to 324 TOEFL_Score-94 to 111, University_Rating-1 to 3, SOP-1.00 to 3, CGPA-7.50 to 8.79, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.37 to 0.81 only and in this parameter 11 record are there.

# LOR==2:-
- In LOR==2, **(GRE_Score-290 to 325 TOEFL_Score-92 to 114, University_Rating-1 to 4, SOP-1.00 to 4, CGPA-6.80 to 8.780, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.34 to 0.79 only and in this parameter 46 record are there.

# LOR==2.5:-
- In LOR==2.5, **(GRE_Score-290 to 328 TOEFL_Score-98 to 113, University_Rating-1 to 4, SOP-1.00 to 4, CGPA-7.46 to 9.02, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.36 to 0.83 only and in this parameter 50 record are there.

# LOR==3:-
- In LOR==3, **(GRE_Score-295 to 334 TOEFL_Score-97 to 116, University_Rating-1 to 5, SOP-1.50 to 5, CGPA-7.21 to 9.34, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.34 to 0.90 only and in this parameter 99 record are there.

# LOR==3.5:-
- In LOR==3.5, **(GRE_Score-296 to 339 TOEFL_Score-97 to 119, University_Rating-1 to 5, SOP-1.50 to 5, CGPA-7.28 to 9.80, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.38 to 0.97 only and in this parameter 86 record are there.

# LOR==4:-
- In LOR==4, **(GRE_Score-293 to 340 TOEFL_Score-96 to 120, University_Rating-1 to 5, SOP-1.50 to 5, CGPA-7.23 to 9.92, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.52 to 0.97 only and in this parameter 94 record are there.

# LOR==4.5:-
- In LOR==4.5, **(GRE_Score-298 to 340 TOEFL_Score-96 to 120, University_Rating-2 to 5, SOP-2 to 5, CGPA-7.69 to 9.91, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.53 to 0.97 only and in this parameter 63 record are there.

# LOR==5:-
- In LOR==5, **(GRE_Score-302 to 340 TOEFL_Score-100 to 120, University_Rating-3 to 5, SOP-3 to 5, CGPA-8.33 to 9.87, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.65 to 0.97 only and in this parameter 50 record are there.

# University_Rating:-
- In University_Rating==1, **(GRE_Score-290 to 332 TOEFL_Score-92 to 112, SOP-1 to 3.50, LOR-1 to 4, CGPA-6.80 to 9.12, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.36 to 0.79 only and in this parameter 34 record are there.

# University_Rating:-
- In University_Rating==2, **(GRE_Score-293 to 332 TOEFL_Score-94 to 118, SOP-1 to 4.50, LOR-1.50 to 4.50, CGPA-7.21 to 9.36, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.34 to 0.90 only and in this parameter 126 record are there.

# University_Rating:-
- In University_Rating==3, **(GRE_Score-297 to 331 TOEFL_Score-97 to 120, SOP-2 to 5, LOR-1.50 to 5, CGPA-7.40 to 9.32, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.36 to 0.90 only and in this parameter 162 record are there.

# University_Rating:-
- In University_Rating==4, **(GRE_Score-290 to 340 TOEFL_Score-96 to 120, SOP-1.50 to 5, LOR-2 to 5, CGPA-7.46 to 9.92, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.42 to 0.97 only and in this parameter 105 record are there.

# University_Rating:-
- In University_Rating==5, **(GRE_Score-303 to 340 TOEFL_Score-101 to 120, SOP-3 to 5, LOR-3 to 5, CGPA-7.92 to 9.91, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.61 to 0.97 only and in this parameter 73 record are there.

# Research:-
- In Research==0, **(GRE_Score-290 to 339 TOEFL_Score-92 to 120, University_Rating-1 to 5 , SOP-1 to 5, LOR-1 to 5, CGPA-7.20 to 9.70, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.34 to 0.89 only and in this parameter 220 record are there.

# Research:-
- In Research==1, **(GRE_Score-293 to 340 TOEFL_Score-95 to 120, University_Rating-1 to 5 , SOP-1 to 5, LOR-1.50 to 5, CGPA-6.80 to 9.92, Research-0 & 1)**, for this parameters we can get Chance_of_Admit from - 0.36 to 0.97 only and in this parameter 280 record are there.
```

# Data Cleaning:-
```
- Removed and replaced the outlies.
```
## X and y:
```
X=ds.drop(columns=['Serial No.','Chance_of_Admit','SOP'])
y=ds['Chance_of_Admit']
- instead of 8 independent columns, we consider only 7 independent columns. why beacause SOP column having high significance value.
```

# Linear Regression model:-
```
Train Accuracy - 0.8213508151961643
Test Accuracy - 0.8212861443145779
Cross-validation Accuracy - 0.8137016376587068
```

# Polynomial Regression model:-
```
Train Accuracy - 0.8214313062718266
Test Accuracy - 0.8220836352928902
Cross-validation Accuracy - 0.813878077674634
```