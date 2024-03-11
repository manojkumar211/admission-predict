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

```


