# Data Codebook

## Dataset Description

The dataset contains survey responses from KIU undergraduate students about internship support services. Each row represents one respondent. The raw CSV should be exported from Google Forms and saved in `data/raw/`.

## Missing Values

Use blank cells for missing values. During analysis, blank cells in numeric columns will be converted to missing values.

## Variable Definitions

| Column | Description | Type | Allowed Values |
|---|---|---|---|
| respondent_id | Anonymous respondent code | Text | R001, R002, etc. |
| year_of_study | Student year level | Categorical | 1st year, 2nd year, 3rd year, 4th year |
| school | Student school | Categorical | Computer Science and Engineering, Management, Medicine, Other |
| searched_for_internship | Whether student searched for an internship | Binary | Yes, No |
| completed_internship | Whether student completed an internship | Binary | Yes, No |
| awareness_score | Awareness of internship support services | Numeric | 1-5 |
| used_support | Whether student used KIU internship support | Binary | Yes, No |
| info_availability | Ease of finding internship information | Numeric | 1-5 |
| communication_quality | Clarity and timeliness of communication | Numeric | 1-5 |
| application_support | Usefulness of application support | Numeric | 1-5 |
| cv_support | Usefulness of CV/resume support | Numeric | 1-5 |
| interview_support | Usefulness of interview preparation | Numeric | 1-5 |
| industry_connections | Helpfulness of employer/industry connections | Numeric | 1-5 |
| accessibility | Ease of accessing support services | Numeric | 1-5 |
| overall_satisfaction | Overall satisfaction with services | Numeric | 1-5 |
| finding_confidence | Confidence finding internship opportunities | Numeric | 1-5 |
| cv_confidence | Confidence preparing a CV/resume | Numeric | 1-5 |
| interview_confidence | Confidence preparing for interviews | Numeric | 1-5 |
| employer_expectations | Understanding employer expectations | Numeric | 1-5 |
| readiness_improvement | Perception that KIU support improved readiness | Numeric | 1-5 |
| biggest_weakness | Student-identified weakness | Text | Open response |
| improvement_suggestion | Student recommendation | Text | Open response |

## Composite Variables Created During Analysis

| New Variable | Calculation | Interpretation |
|---|---|---|
| satisfaction_score | Mean of service evaluation items | Higher values indicate stronger satisfaction |
| readiness_score | Mean of readiness items | Higher values indicate stronger perceived internship readiness |

## Important Note

If the Google Forms export uses longer question text as headers, rename the columns to match this codebook before running the analysis script.

