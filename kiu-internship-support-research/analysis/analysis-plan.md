# Analysis Plan

## Purpose

The analysis will describe student perceptions of KIU internship support services and test whether students who used support services report higher perceived internship readiness than students who did not.

## Data Source

Primary data will come from a Google Forms questionnaire exported as a CSV file and saved in:

```text
data/raw/google-forms-export-placeholder.csv
```

The dummy dataset currently contains 30 fake respondents so the team can test the analysis workflow before collecting real data.

## Data Cleaning Steps

1. Confirm all expected columns are present.
2. Remove rows without consent if the consent column is included in the final Google Forms export.
3. Standardize Yes/No values.
4. Convert Likert-scale columns to numeric values.
5. Check for missing values in key variables.
6. Create composite satisfaction and readiness scores.
7. Save a cleaned copy of the dataset.

## Descriptive Analysis

Report frequencies and percentages for:

- Year of study
- School
- Internship search status
- Internship completion status
- Awareness levels
- Support service usage

Report means for:

- Each service evaluation item
- Overall satisfaction
- Satisfaction score
- Each readiness item
- Readiness score

## Inferential Analysis

The main hypothesis test compares readiness scores between:

- Students who used KIU internship support services
- Students who did not use KIU internship support services

If both groups have at least two valid responses, run an independent samples t-test.

Recommended interpretation:

- If p < 0.05, reject H0 and conclude that the readiness difference is statistically significant.
- If p >= 0.05, fail to reject H0 and conclude that the data does not show a statistically significant difference.

## Charts

Create simple charts for:

- Support usage counts
- Mean service evaluation scores
- Mean readiness score by support usage group
- Top weakness themes, if coded manually

## Output Files

The analysis script exports results to `analysis/outputs/`, including:

- `cleaned-survey-data.csv`
- `categorical-frequencies.csv`
- `scale-means.csv`
- `readiness-by-support-usage.csv`
- `ttest-results.csv`
- PNG chart files

## Reporting Notes

The final report should connect the statistical results to the research question. Avoid overstating the findings, especially if the final sample is small or based on convenience sampling.

