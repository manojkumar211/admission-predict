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
