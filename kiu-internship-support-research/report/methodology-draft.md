# Methodology Draft

## Research Design

This study used a cross-sectional survey design to examine KIU undergraduate students' perceptions of internship support services. The design was appropriate because the research aimed to collect students' views at a specific point in time.

## Population and Sample

The target population was KIU undergraduate students. The sample consisted of students who voluntarily completed the Google Forms questionnaire. Because the survey was distributed through accessible student channels, the study used convenience sampling.

Report wording to complete after data collection:

> The final sample included [number] valid consenting responses from undergraduate students across [schools/year levels].

## Data Collection Instrument

Data were collected using a structured questionnaire created in Google Forms. The questionnaire included items about student background, internship search experience, awareness of KIU internship support services, service usage, satisfaction among support users, reasons for non-use, internship readiness, improvement priorities, and open-ended suggestions.

The form used section branching. Students who had used KIU internship support services answered service-evaluation and support-impact questions. Students who had not used support services answered a non-use reason question instead. All consenting respondents answered the internship readiness items. Most evaluation items used a five-point Likert scale, where higher values indicated more positive perceptions.

## Variables

The main independent grouping variable was whether students had used KIU internship support services. The main dependent variable was perceived internship readiness, calculated as the mean of four neutral readiness items: confidence finding internship opportunities, confidence preparing a CV or resume, confidence preparing for interviews, and understanding employer expectations.

Service satisfaction was calculated only for students who used support services. The item asking whether KIU support improved readiness was analyzed separately as `support_readiness_impact` because it directly measures perceived support impact and does not apply to non-users.

## Data Analysis

The data were analyzed using Python. Descriptive statistics summarized sample characteristics, service awareness, usage, satisfaction among support users, non-use reasons, readiness, and improvement priorities. Missing values were checked before reporting results.

If both support users and non-users had at least two valid readiness scores, a Welch independent samples t-test was used to compare readiness scores between the two groups. The analysis reported group means, standard deviations, mean difference, 95% confidence interval, p-value, Cohen's d, and Cronbach's alpha where sample size allowed. The comparison was interpreted as an association, not as proof that support service usage caused higher readiness.

## Ethical Considerations

Participation was voluntary, and the survey did not require names, student ID numbers, emails, phone numbers, or other direct identifiers. Responses were used only for academic purposes and reported in aggregate form.

## Limitations

The study was limited by convenience sampling, possible response bias, and reliance on self-reported perceptions. The results should therefore be interpreted as evidence from the surveyed students rather than as definitive evidence for all KIU undergraduates.
