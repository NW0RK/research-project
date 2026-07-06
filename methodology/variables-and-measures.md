# Variables and Measures

## Overview

This study uses survey items to measure awareness, usage, satisfaction, perceived usefulness, internship readiness, reasons for non-use, and improvement priorities. Most scale items use a 1-5 Likert scale.

Recommended scale:

1. Strongly disagree / Very dissatisfied / Very low
2. Disagree / Dissatisfied / Low
3. Neutral / Moderate
4. Agree / Satisfied / High
5. Strongly agree / Very satisfied / Very high

## Variable Table

| Variable | Type | Measurement | Example Survey Item |
|---|---|---|---|
| respondent_id | Identifier | Assigned anonymous number | R001 |
| consent | Binary | Yes/No | Do you agree to participate? |
| year_of_study | Categorical | 1st, 2nd, 3rd, 4th, Other | What is your year of study? |
| school | Categorical | School/program group | Which school are you enrolled in? |
| searched_for_internship | Binary | Yes/No | Have you searched for an internship? |
| completed_internship | Binary | Yes/No | Have you completed an internship? |
| awareness_score | Numeric | 1-5 | I am aware of KIU internship support services. |
| used_support | Binary | Yes/No | Have you used KIU internship support services? |
| support_services_used | Text / multi-select | Service categories | Which support services have you used? |
| nonuse_reason | Categorical | Main reason | What is the main reason you have not used support services? |
| info_availability | Numeric | 1-5 | Internship information is easy to find. |
| communication_quality | Numeric | 1-5 | Internship-related communication is clear and timely. |
| application_support | Numeric | 1-5 | KIU provides useful support for internship applications. |
| cv_support | Numeric | 1-5 | KIU provides useful CV or resume support. |
| interview_support | Numeric | 1-5 | KIU provides useful interview preparation support. |
| industry_connections | Numeric | 1-5 | KIU provides helpful employer or industry connections. |
| accessibility | Numeric | 1-5 | Internship support services are easy to access. |
| overall_satisfaction | Numeric | 1-5 | Overall, I am satisfied with KIU internship support services. |
| finding_confidence | Numeric | 1-5 | I feel confident finding internship opportunities. |
| cv_confidence | Numeric | 1-5 | I feel confident preparing a strong CV. |
| interview_confidence | Numeric | 1-5 | I feel confident preparing for internship interviews. |
| employer_expectations | Numeric | 1-5 | I understand what employers expect from interns. |
| support_readiness_impact | Numeric | 1-5 | KIU support has improved my internship readiness. |
| top_improvement_priority | Categorical | Priority choice | Which improvement would help students the most? |
| biggest_weakness | Text | Open-ended | What is the biggest weakness of KIU internship support? |
| improvement_suggestion | Text | Open-ended | What improvement would you suggest? |

## Composite Scores

### Satisfaction Score

The satisfaction score is calculated only for respondents who used KIU internship support services. It is the mean of:

- info_availability
- communication_quality
- application_support
- cv_support
- interview_support
- industry_connections
- accessibility
- overall_satisfaction

### Readiness Score

The readiness score is calculated for all consenting respondents. It is the mean of:

- finding_confidence
- cv_confidence
- interview_confidence
- employer_expectations

The item `support_readiness_impact` is analyzed separately. It is not part of `readiness_score` because it directly measures perceived benefit from KIU support and applies only to support users.

## Notes for Interpretation

A higher score means a more positive perception. A readiness score close to 5 indicates that a student feels highly prepared for the internship search and application process. Because the study uses a cross-sectional survey, differences between users and non-users should be interpreted as associations, not proof that support services caused higher readiness.
