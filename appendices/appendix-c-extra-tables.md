# Appendix C: Extra Tables

All values below are produced by `analysis/analysis-script.py` and correspond to the files in `analysis/outputs/`. Final analytic sample: **N = 122** (all consenting; no exclusions required).

## Table C1: Sample Characteristics and Categorical Frequencies

Source: `categorical-frequencies.csv`

| Variable | Category | Frequency | Percentage |
|---|---|---:|---:|
| Year of study | 2nd year | 18 | 14.8 |
| Year of study | 3rd year | 83 | 68.0 |
| Year of study | 4th year | 21 | 17.2 |
| School | Computer Science | 76 | 62.3 |
| School | Management | 34 | 27.9 |
| School | Mathematics | 12 | 9.8 |
| Searched for internship | Yes | 96 | 78.7 |
| Searched for internship | No | 26 | 21.3 |
| Completed internship | Yes | 41 | 33.6 |
| Completed internship | No | 81 | 66.4 |
| Used support | Yes | 38 | 31.1 |
| Used support | No | 84 | 68.9 |

## Table C2: Service Evaluation Means Among Support Users

Source: `scale-means.csv` — support users only (n = 38)

| Item | Mean | Standard Deviation | n |
|---|---:|---:|---:|
| Industry connections | 3.26 | 0.92 | 38 |
| Communication quality | 3.03 | 1.13 | 38 |
| Accessibility | 3.00 | 0.81 | 38 |
| Application support | 2.97 | 0.88 | 38 |
| Information availability | 2.87 | 0.84 | 38 |
| Overall satisfaction | 2.82 | 0.98 | 38 |
| CV support | 1.92 | 0.91 | 38 |
| Interview support | 1.55 | 0.80 | 38 |
| **Composite satisfaction score** | **2.68** | **0.56** | **38** |
| Support readiness impact *(analysed separately)* | 2.95 | 0.93 | 38 |

## Table C3: Specific Services Used

Source: `analysis-summary.md` — support users only (n = 38; multiple selections allowed)

| Service | n | % of users |
|---|---:|---:|
| Internship information or announcements | 36 | 94.7 |
| One-to-one advising | 5 | 13.2 |
| Employer or alumni events | 4 | 10.5 |
| CV or resume support | 3 | 7.9 |
| Application support | 3 | 7.9 |
| Interview preparation | 2 | 5.3 |
| Other | 4 | 10.5 |

## Table C4: Reasons for Non-Use

Source: `categorical-frequencies.csv` — non-users only (n = 84)

| Reason | n | % of non-users |
|---|---:|---:|
| I did not know the services existed | 27 | 32.1 |
| The available services did not seem relevant to my field | 18 | 21.4 |
| I did not know how to access them | 16 | 19.0 |
| I planned to use them later | 13 | 15.5 |
| I knew about them but did not need them | 8 | 9.5 |
| Other | 2 | 2.4 |

## Table C5: Improvement Priority

Source: `categorical-frequencies.csv` (N = 122)

| Improvement | n | % |
|---|---:|---:|
| Earlier communication about internship opportunities | 47 | 38.5 |
| One central internship information platform | 26 | 21.3 |
| More employer and alumni networking events | 18 | 14.8 |
| More school-specific internship guidance | 15 | 12.3 |
| More mock interview practice | 7 | 5.7 |
| More CV or resume support | 7 | 5.7 |
| Other | 2 | 1.6 |

## Table C6: Readiness Items

Source: `scale-means.csv` (N = 122)

| Item | Mean | Standard Deviation | n |
|---|---:|---:|---:|
| CV confidence | 3.20 | 1.11 | 122 |
| Interview confidence | 3.00 | 1.19 | 122 |
| Employer expectations | 2.76 | 1.06 | 122 |
| Finding confidence | 2.60 | 1.04 | 122 |
| **Composite readiness score** | **2.89** | **0.85** | **122** |
| Awareness score *(single item)* | 2.92 | 1.32 | 122 |

## Table C7: Welch t-test Result

Source: `readiness-by-support-usage.csv` and `ttest-results.csv`

| Group | n | Mean Readiness | Standard Deviation |
|---|---:|---:|---:|
| Used support services | 38 | 3.23 | 0.70 |
| Did not use support services | 84 | 2.74 | 0.87 |

**Test result:**

- Mean difference: 0.50
- 95% CI: [0.20, 0.79]
- Degrees of freedom: 88.06
- t-statistic: 3.3585
- p-value: .0012
- Cohen's d: 0.604 (medium effect)
- **Decision: Reject H₀** at the .05 significance level

## Table C8: Normality Check

Source: `normality-results.csv`

| Variable | Test | n | W | p-value | Normal at .05 |
|---|---|---:|---:|---:|---|
| Readiness score | Shapiro–Wilk | 122 | .983 | .130 | Yes |

## Table C9: Correlations

Source: `correlation-results.csv`

| X | Y | n | Pearson r | p | Spearman ρ | p |
|---|---|---:|---:|---:|---:|---:|
| Awareness score | Readiness score | 122 | .429 | < .001 | .436 | < .001 |
| Year of study | Readiness score | 122 | .272 | .002 | .263 | .003 |

## Table C10: Reliability Checks

Source: `reliability-results.csv`

| Scale | Items | Complete Responses | Cronbach's Alpha |
|---|---:|---:|---:|
| Readiness items | 4 | 122 | .771 |
| Service evaluation items | 8 | 38 | .767 |

## Reporting Caution

Because this project used a cross-sectional convenience sample, the readiness comparison must be described as an **association** in the surveyed sample. Do not claim that support-service usage caused higher readiness.
