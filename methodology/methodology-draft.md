# Methodology

## Research Design

This study uses a quantitative, cross-sectional survey design supplemented by a small number of open-ended items. It captures KIU undergraduate students' perceptions of internship support services at a single point in time, covering awareness, usage, service satisfaction (among users), perceived internship readiness, reasons for non-use, and priority areas for improvement.

A cross-sectional design fits the research question because it allows comparison between students who have and have not used support services without requiring longitudinal tracking, which was not feasible within the course timeline. The open-ended items provide qualitative context that helps interpret the quantitative patterns.

## Participants and Sampling

The target population is KIU undergraduate students in the **Computer Science, Management, and Mathematics** schools, from **2nd through 4th year**. First-year students were excluded, since they are unlikely to have engaged meaningfully with internship search or support services at this stage of their studies. Students from other, newly introduced KIU majors were also excluded, as these programs are too recently established to have sufficient institutional information on their internship support provisions.

Convenience sampling was used, chosen for practicality given the course project's limited timeframe. Because this is a non-probability method, findings are reported as descriptive of the surveyed sample rather than as statistically representative of the full KIU student body.

**Final analytic sample: N = 122.** All 122 respondents consented, fell within the target years and schools, and completed every required item, so no responses required exclusion.

## Data Collection Instrument

Data was collected using a custom, self-administered Google Forms questionnaire (see `survey-questionnaire.md`), estimated at 5–7 minutes to complete. Since no existing validated scale fit KIU's specific internship-support context, the team developed the instrument itself, drawing on constructs from the literature review. The readiness items were shaped by the self-efficacy and confidence dimensions central to the CareerEDGE model, while the service-evaluation items were built around service-quality dimensions such as reliability, accessibility, and personalized guidance.

The form includes:

- A required consent question (non-consenters routed to a thank-you screen)
- Academic background: year of study, school
- Internship search and completion history
- A single awareness item and a binary usage question that branches the survey
- **Users:** a multi-select of services used plus nine service-evaluation Likert items
- **Non-users:** a single categorical item on their main reason for non-use
- Four internship-readiness items (all respondents)
- A single-select improvement-priority item
- Two optional open-ended questions

All Likert items use a 1 ("Strongly disagree") to 5 ("Strongly agree") scale.

## Variables

See `variables-and-measures.md` for the full codebook.

The main grouping variable is `used_support`. The primary outcome variable is `readiness_score`, the mean of four readiness items: confidence finding internship opportunities, confidence preparing a CV or resume, confidence preparing for interviews, and understanding employer expectations.

Service evaluation variables (users only) include information availability, communication quality, application support, CV support, interview support, industry connections, accessibility, and overall satisfaction. The item `support_readiness_impact` is analyzed separately because it directly asks support users whether KIU support improved their readiness, making it an attribution measure rather than a readiness level.

## Procedure

The questionnaire was built and distributed through Google Forms. Before full distribution, it was pilot-tested with two students to check that the wording, response options, and branching logic were clear and functioned correctly. No substantive issues were raised, and the pilot responses were collected separately and are not part of the analysed data.

The final form link was shared through KIU class group chats, student association channels, and academic networks over an **eleven-day collection window from 28 June to 8 July 2026**. A single official form link was used throughout, and Google Forms was configured to accept **only one response per account**, preventing duplicate submissions at the point of collection. No identifying information, including email addresses, was recorded in the exported data.

Responses were logged automatically to a linked Google Sheet, exported to CSV, and screened for completeness and duplication before analysis. No duplicate or incomplete records were found.

## Data Analysis

Analysis was conducted in **Python**, using `pandas` for data handling, `SciPy` for the normality and correlation tests, and `Matplotlib` for figures. The Welch t-test statistic, degrees of freedom, confidence interval, Cohen's d, and Cronbach's alpha were computed directly from their formulas within `analysis/analysis-script.py`.

**Descriptive analysis** reported:

- Frequencies and percentages for all categorical variables
- Means and standard deviations for awareness, service evaluation, readiness, and support-impact scores
- Missing-value counts for key variables
- Thematic coding of open-ended weakness and improvement responses

**Reliability:** Cronbach's alpha for the readiness score (α = .771) and the satisfaction score (α = .767).

**Inferential analysis:** A Welch independent-samples t-test compared mean readiness scores between support users (n = 38) and non-users (n = 84). Welch's version was chosen because it does not assume equal group sizes or equal variances, both of which were expected given the imbalance between groups. Normality of the readiness score was checked with the Shapiro–Wilk test (W = .983, p = .130) before running the parametric analyses, with the Mann–Whitney U test held as a non-parametric fallback.

Result: users M = 3.23 (SD = 0.70), non-users M = 2.74 (SD = 0.87); mean difference 0.50, 95% CI [0.20, 0.79], t(88.06) = 3.36, p = .001, d = 0.60. **H₀ was rejected.**

Pearson correlation, with Spearman's rank correlation as a robustness check, explored the relationships between awareness and readiness (r = .43, p < .001) and between year of study and readiness (r = .27, p = .002).

Because the design is cross-sectional, all group differences are described as **associations**, not as causal proof that support services raised readiness.

## Ethical Considerations

Participation was entirely voluntary, and students could withdraw at any point before submitting. No direct identifiers — names, student IDs, email addresses, or phone numbers — were collected. The consent screen explained the study's purpose, confirmed that participation was optional, and gave an estimated completion time. Responses were stored in a team-controlled Google Drive folder. Open-ended answers were checked for accidental identifiers before reporting. All findings are presented in aggregate, small subgroups are reported with caution, and no response is quoted in a way that could identify the student who wrote it.

See `ethics-and-consent.md` for the full plan.

## Limitations

*(Reported in the Discussion section of the final report, per the project guide.)*

The convenience sample is heavily weighted toward 3rd-year Computer Science students, so Management and Mathematics students — and 2nd- and 4th-year students — are represented by small subgroups. The cross-sectional design means the user/non-user readiness difference is an association, not proof of causation; more proactive students may be more likely both to use services and to feel ready (self-selection). All measures are self-reported perceptions rather than actual placement outcomes. The instrument was custom-built and only minimally piloted (two test respondents). Finally, the study covers a single small institution, which limits generalisability.
