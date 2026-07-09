# Variables and Measures

## Overview

This study uses survey items to measure awareness, usage, satisfaction, perceived usefulness, internship readiness, reasons for non-use, and improvement priorities. Most scale items use a 1–5 Likert scale.

Scale anchors:

1. Strongly disagree
2. Disagree
3. Neutral
4. Agree
5. Strongly agree

## Variable Table

| Variable | Type | Measurement | Example Survey Item |
|---|---|---|---|
| `respondent_id` | Identifier | Assigned anonymous number | R001 |
| `consent` | Binary | Yes/No | Do you agree to participate? |
| `year_of_study` | Categorical | 2nd, 3rd, 4th year | What is your year of study? |
| `school` | Categorical | Computer Science, Management, Mathematics | Which school are you enrolled in? |
| `searched_for_internship` | Binary | Yes/No | Have you searched for an internship? |
| `completed_internship` | Binary | Yes/No | Have you completed an internship? |
| `awareness_score` | Numeric | 1–5 | I am aware of KIU internship support services. |
| `used_support` | Binary | Yes/No (grouping variable) | Have you used KIU internship support services? |
| `support_services_used` | Multi-select | Service categories | Which support services have you used? |
| `nonuse_reason` | Categorical | Main reason | What is the main reason you have not used support services? |
| `info_availability` | Numeric | 1–5, users only | Internship information is easy to find. |
| `communication_quality` | Numeric | 1–5, users only | Internship-related communication is clear and timely. |
| `application_support` | Numeric | 1–5, users only | KIU provides useful support for internship applications. |
| `cv_support` | Numeric | 1–5, users only | KIU provides useful CV or resume support. |
| `interview_support` | Numeric | 1–5, users only | KIU provides useful interview preparation support. |
| `industry_connections` | Numeric | 1–5, users only | KIU provides helpful employer or industry connections. |
| `accessibility` | Numeric | 1–5, users only | Internship support services are easy to access. |
| `overall_satisfaction` | Numeric | 1–5, users only | Overall, I am satisfied with KIU internship support services. |
| `support_readiness_impact` | Numeric | 1–5, users only (analysed separately) | KIU support has improved my internship readiness. |
| `finding_confidence` | Numeric | 1–5 | I feel confident finding internship opportunities. |
| `cv_confidence` | Numeric | 1–5 | I feel confident preparing a strong CV. |
| `interview_confidence` | Numeric | 1–5 | I feel confident preparing for internship interviews. |
| `employer_expectations` | Numeric | 1–5 | I understand what employers expect from interns. |
| `top_improvement_priority` | Categorical | Priority choice | Which improvement would help students the most? |
| `biggest_weakness` | Text | Open-ended | What is the biggest weakness of KIU internship support? |
| `improvement_suggestion` | Text | Open-ended | What improvement would you suggest? |

## Composite Scores

### Satisfaction Score

Calculated **only for respondents who used KIU internship support services** (n = 38). It is the mean of eight items:

- `info_availability`
- `communication_quality`
- `application_support`
- `cv_support`
- `interview_support`
- `industry_connections`
- `accessibility`
- `overall_satisfaction`

Observed: **M = 2.68, SD = 0.56, Cronbach's α = .767**

### Readiness Score

Calculated for **all consenting respondents** (N = 122). It is the mean of four items:

- `finding_confidence`
- `cv_confidence`
- `interview_confidence`
- `employer_expectations`

Observed: **M = 2.89, SD = 0.85, Cronbach's α = .771**

This is the study's **primary outcome variable** and the basis for the Welch t-test comparing users and non-users.

### Why `support_readiness_impact` Is Excluded

The item `support_readiness_impact` is analysed separately and is **not** part of `readiness_score`. It asks support users whether KIU services *improved* their readiness — a subjective attribution of benefit — rather than measuring a general readiness level. It also applies only to support users, so including it would make the composite non-comparable across groups. Observed among users: M = 2.95, SD = 0.93.

## Notes for Interpretation

A higher score means a more positive perception. A readiness score close to 5 indicates that a student feels highly prepared for the internship search and application process.

Because the study uses a **cross-sectional convenience sample**, differences between users and non-users must be interpreted as **associations**, not as proof that support services caused higher readiness. Self-selection is a plausible alternative explanation: more proactive or confident students may be more likely both to seek out services and to feel ready.
