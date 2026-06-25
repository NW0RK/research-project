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
2. Remove rows where `consent` is not "Yes."
3. Standardize Yes/No values.
4. Convert Likert-scale columns to numeric values.
5. Check for missing values in key variables.
6. Create `satisfaction_score` only for support users.
7. Create `readiness_score` from the four neutral readiness items.
8. Save a cleaned copy of the dataset.

## Descriptive Analysis

Report frequencies and percentages for:

- Year of study
- School
- Internship search status
- Internship completion status
- Support service usage
- Reason for non-use among non-users
- Top improvement priority

Report means for:

- Awareness score
- Each service evaluation item among support users
- Overall satisfaction among support users
- Satisfaction score among support users
- Each readiness item among all consenting respondents
- Readiness score among all consenting respondents
- Support readiness impact among support users

## Reliability Checks

If enough complete responses are available, calculate Cronbach's alpha for:

- Readiness items
- Service evaluation items among support users

Report reliability as a descriptive check only. Do not overstate it if the sample is small.

## Inferential Analysis

The main hypothesis test compares readiness scores between:

- Students who used KIU internship support services
- Students who did not use KIU internship support services

If both groups have at least two valid responses, run a Welch independent samples t-test. Report:

- Group sample sizes
- Group means and standard deviations
- Mean difference
- t-statistic and p-value
- 95% confidence interval for the mean difference
- Cohen's d

Recommended interpretation:

- If p < 0.05, reject H0 and conclude that the readiness difference is statistically significant in this sample.
- If p >= 0.05, fail to reject H0 and conclude that the data does not show a statistically significant difference.
- In both cases, describe the result as an association rather than proof that support services caused higher readiness.

## Charts

Create simple charts for:

- Support usage counts
- Mean service evaluation scores among support users
- Mean readiness score by support usage group
- Top improvement priorities

If open-ended responses are coded manually, the team may also create a weakness-theme chart using `analysis/open-ended-theme-coding-guide.md`.

## Output Files

The analysis script exports results to `analysis/outputs/`, including:

- `cleaned-survey-data.csv`
- `categorical-frequencies.csv`
- `missing-values.csv`
- `scale-means.csv`
- `readiness-by-support-usage.csv`
- `ttest-results.csv`
- `reliability-results.csv`
- `analysis-summary.md`
- PNG chart files

## Reporting Notes

The final report should connect the statistical results to the research question. Avoid overstating the findings, especially if the final sample is small or based on convenience sampling.
