# Results Template

## 4. Results

This section presents the findings from the student survey. Use the files in `analysis/outputs/` after running the analysis script. The most useful source for writing is `analysis-summary.md`; detailed tables are available in the CSV files.

## 4.1 Sample Characteristics

The final dataset included [number] valid consenting responses. Respondents represented [list schools] and included students from [list year levels].

Use `categorical-frequencies.csv` for this table:

| Characteristic | Category | Frequency | Percentage |
|---|---|---:|---:|
| Year of study | [category] | [n] | [%] |
| School | [category] | [n] | [%] |

## 4.2 Internship Search and Experience

Report how many students had searched for an internship and how many had completed one. Use `categorical-frequencies.csv`.

Suggested wording:

> A majority/minority of respondents reported that they had searched for an internship, while [percentage]% had already completed one.

## 4.3 Awareness, Usage, and Non-Use

Report the mean awareness score, the percentage of students who used support services, and the most common reason non-users gave for not using services.

Suggested wording:

> The mean awareness score was [mean], suggesting [low/moderate/high] awareness of KIU internship support services. [percentage]% of respondents reported using at least one support service.

## 4.4 Service Satisfaction and Usefulness

Report service evaluation means only among students who used support services. Use `scale-means.csv` and `service-evaluation-means.png`.

| Service Area | Mean Score |
|---|---:|
| Information availability | [mean] |
| Communication quality | [mean] |
| Application support | [mean] |
| CV support | [mean] |
| Interview support | [mean] |
| Industry connections | [mean] |
| Accessibility | [mean] |
| Overall satisfaction | [mean] |

Suggested wording:

> Among support users, the highest-rated service area was [area], while the lowest-rated service area was [area].

## 4.5 Internship Readiness

Report the overall readiness score and readiness item means. Readiness is calculated from four neutral items: finding confidence, CV confidence, interview confidence, and employer expectations.

Suggested wording:

> The mean readiness score was [mean], indicating that students reported [low/moderate/high] confidence in internship preparation.

## 4.6 Hypothesis Test

Compare readiness scores between students who used support services and students who did not. Use `readiness-by-support-usage.csv` and `ttest-results.csv`.

| Group | n | Mean Readiness | Standard Deviation |
|---|---:|---:|---:|
| Used support | [n] | [mean] | [sd] |
| Did not use support | [n] | [mean] | [sd] |

Suggested wording:

> A Welch independent samples t-test showed that the difference in readiness scores was [statistically significant/not statistically significant], mean difference = [value], 95% CI [[lower], [upper]], t([df]) = [value], p = [value], Cohen's d = [value].

## 4.7 Reliability Checks

If Cronbach's alpha was calculated, report it briefly using `reliability-results.csv`.

Suggested wording:

> The readiness items showed [acceptable/strong/weak] internal consistency, Cronbach's alpha = [value].

## 4.8 Open-Ended Responses and Priorities

Report the top improvement priorities from `categorical-frequencies.csv` and summarize open-ended themes using `analysis/open-ended-theme-coding-guide.md`.

Suggested wording:

> The most common improvement priorities were [priority 1], [priority 2], and [priority 3]. Open-ended responses similarly emphasized [theme 1] and [theme 2].
