# Data Codebook

## Dataset Description

The dataset contains survey responses from KIU undergraduate students about internship support services. Each row represents one anonymous respondent. The raw CSV should be exported from Google Forms and saved in `data/raw/`.

## Missing Values

Use blank cells for missing values. During analysis, blank cells in numeric columns are converted to missing values. Branching questions should remain blank when they do not apply. For example, non-users should have blank service-evaluation fields, and support users should have a blank `nonuse_reason`.

## Variable Definitions

| Column | Description | Type | Allowed Values |
|---|---|---|---|
| respondent_id | Anonymous respondent code for analysis only | Text | R001, R002, etc. |
| consent | Whether respondent agreed to participate | Binary | Yes, No |
| year_of_study | Student year level | Categorical | 1st year, 2nd year, 3rd year, 4th year, Other |
| school | Student school | Categorical | Computer Science and Engineering, Management, Medicine, Other |
| searched_for_internship | Whether student searched for an internship | Binary | Yes, No |
| completed_internship | Whether student completed an internship | Binary | Yes, No |
| awareness_score | Awareness of internship support services | Numeric | 1-5 |
| used_support | Whether student used KIU internship support | Binary | Yes, No |
| support_services_used | Services used by support users | Text / multi-select | Semicolon-separated selections from the questionnaire |
| nonuse_reason | Main reason for not using support services | Categorical | Survey response option or Other |
| info_availability | Ease of finding internship information | Numeric | 1-5; blank if `used_support` = No |
| communication_quality | Clarity and timeliness of communication | Numeric | 1-5; blank if `used_support` = No |
| application_support | Usefulness of application support | Numeric | 1-5; blank if `used_support` = No |
| cv_support | Usefulness of CV/resume support | Numeric | 1-5; blank if `used_support` = No |
| interview_support | Usefulness of interview preparation | Numeric | 1-5; blank if `used_support` = No |
| industry_connections | Helpfulness of employer/industry connections | Numeric | 1-5; blank if `used_support` = No |
| accessibility | Ease of accessing support services | Numeric | 1-5; blank if `used_support` = No |
| overall_satisfaction | Overall satisfaction with services | Numeric | 1-5; blank if `used_support` = No |
| finding_confidence | Confidence finding internship opportunities | Numeric | 1-5 |
| cv_confidence | Confidence preparing a CV/resume | Numeric | 1-5 |
| interview_confidence | Confidence preparing for interviews | Numeric | 1-5 |
| employer_expectations | Understanding employer expectations | Numeric | 1-5 |
| support_readiness_impact | Perception that KIU support improved readiness | Numeric | 1-5; blank if `used_support` = No |
| top_improvement_priority | Improvement that would help students most | Categorical | Survey response option or Other |
| biggest_weakness | Student-identified weakness | Text | Open response |
| improvement_suggestion | Student recommendation | Text | Open response |

## Composite Variables Created During Analysis

| New Variable | Calculation | Interpretation |
|---|---|---|
| satisfaction_score | Mean of service evaluation items, calculated only for support users | Higher values indicate stronger satisfaction with used services |
| readiness_score | Mean of `finding_confidence`, `cv_confidence`, `interview_confidence`, and `employer_expectations` | Higher values indicate stronger perceived internship readiness |

## Important Notes

- `support_readiness_impact` is not part of `readiness_score` because it directly asks about the perceived impact of KIU support. Keeping it separate makes the comparison between users and non-users fairer.
- If the Google Forms export uses longer question text as headers, rename the columns to match this codebook before running the analysis script.
- Do not store names, student IDs, emails, phone numbers, or other direct identifiers in the dataset.
