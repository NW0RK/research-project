# Presentation Q&A Prep

The presentation is graded **individually**. Every team member must be able to answer questions on **any** section, not just their own. Use these answers as a base, but be able to explain them in your own words.

---

## The one-sentence story

> KIU's internship support is associated with higher student readiness — but two-thirds of students never touch it, mostly because they don't know it exists.

---

## Numbers to know cold

| Fact | Value |
|---|---|
| Final sample | **N = 122** (all consented, no exclusions) |
| Collection window | 28 June – 8 July 2026, Google Forms |
| Sample makeup | 68.0% 3rd year; 62.3% CS, 27.9% Management, 9.8% Mathematics |
| Searched for an internship | 78.7% |
| Completed an internship | 33.6% |
| **Used KIU support services** | **31.1% (38 of 122)** |
| Awareness | M = 2.92, SD = 1.32 (below midpoint) |
| #1 non-use reason | "Didn't know they existed" — 32.1% of non-users |
| Users' satisfaction composite | M = 2.68, SD = 0.56 |
| Best-rated service | Industry connections, M = 3.26 |
| **Worst-rated services** | **Interview prep M = 1.55; CV support M = 1.92** |
| Readiness (all) | M = 2.89, SD = 0.85 |
| Readiness by group | Users **3.23** (SD 0.70) vs. non-users **2.74** (SD 0.87) |
| **The t-test** | **t(88.06) = 3.36, p = .001, d = 0.60** |
| 95% CI of mean difference | [0.20, 0.79] |
| Hypothesis decision | **H₀ rejected** |
| Normality check | Shapiro–Wilk W = .983, p = .130 (normal) |
| Awareness ↔ readiness | r(120) = .43, p < .001 (ρ = .44) |
| Year ↔ readiness | r(120) = .27, p = .002 (ρ = .26) |
| Reliability | α = .771 (readiness), α = .767 (satisfaction) |
| Top improvement wanted | Earlier communication, 38.5% |
| Open-ended responses | 76 weaknesses, 70 suggestions |

---

## Design and method questions

### Why did you use a survey?

The research question is about student **perceptions**, so a survey collects comparable responses from many students quickly. Likert items allow descriptive statistics and a group comparison; the open-ended questions capture improvement ideas the closed items would miss. The course also required a survey as the primary instrument.

### Why a cross-sectional design?

It fits the research question and the one-month timeline. We wanted to compare students who had and had not used support services at one point in time, not track change over time — which is also why we're careful to call our result an association, not a causal effect.

### Why convenience sampling?

Practicality within a course timeline. We distributed the form through accessible student channels. It's a non-probability method, so findings describe the perceptions of the surveyed students rather than fully representative evidence for all KIU undergraduates.

### Why exclude 1st-year students and other majors?

First-years rarely have internship-search experience yet, so their answers wouldn't speak to the research question. The other majors are newly launched programmes without established internship-support provisions, so there's no meaningful service for them to evaluate.

### Is your sample representative?

No, and we don't claim it is. It skews toward 3rd-year (68.0%) and Computer Science (62.3%) students. Mathematics has only 12 respondents, so we report that subgroup with caution. This is a stated limitation, and stratified sampling is one of our suggested follow-ups.

### Did you validate your instrument?

We built it ourselves because no existing validated scale fit KIU's specific context. Item design draws on the CareerEDGE model (readiness = self-efficacy/confidence) and service-quality dimensions from the career-services literature. We pilot-tested it with two students to check wording and branching. Internal consistency was acceptable for both composites (α = .77), though full validation is beyond a course project — and we say so in the limitations.

### How did you prevent duplicate responses?

One official form link, with Google Forms set to accept only one response per account. Importantly, that setting recorded **no email address** in the exported data — the CSV has 26 columns, none identifying. Screening confirmed no duplicate rows.

---

## Statistics questions *(the most likely area to be probed)*

### How did you measure internship readiness?

Four items: confidence finding internship opportunities, confidence preparing a CV, confidence preparing for interviews, and understanding employer expectations. The readiness score is their mean. Cronbach's α = .771, so the items hang together as one construct.

### Why is `support_readiness_impact` not in the readiness score?

Because it asks something different. It asks users whether *KIU services improved* their readiness — a subjective attribution of benefit — not their readiness level. It also only applies to the 38 users, so including it would make the composite non-comparable across groups. We report it separately (M = 2.95).

### Why Welch's t-test instead of a standard independent t-test?

Welch's doesn't assume equal variances or equal group sizes. Our groups were unbalanced (38 vs. 84) with different SDs (0.70 vs. 0.87), so Welch's is the safer choice. It's also the modern default recommendation even when variances look similar.

### Why is df = 88.06 and not a whole number?

Welch's test uses the Welch–Satterthwaite approximation for degrees of freedom, which adjusts for unequal variances and produces a fractional value. The decimal is actually evidence we ran Welch's correctly.

### Did you check the assumptions?

Yes. Shapiro–Wilk on the readiness score gave W = .983, p = .130 — no significant departure from normality, so parametric tests are appropriate. Welch's t-test handles the unequal variances. We had Mann–Whitney U ready as a non-parametric fallback but didn't need it.

### What does d = 0.60 mean?

Cohen's d is the effect size — the group difference expressed in standard deviations. By convention 0.2 is small, 0.5 medium, 0.8 large. So 0.60 is a **medium** effect: the difference is not just statistically significant but practically meaningful, roughly half a standard deviation.

### What's the exact p-value?

p = .0012, reported as p = .001.

### Why report a confidence interval?

The 95% CI [0.20, 0.79] shows the plausible range of the true mean difference. It excludes zero, which is consistent with rejecting H₀, and it also shows the difference could be as small as 0.2 points — useful honesty about precision.

### Can you say the support services *caused* higher readiness?

**No.** Cross-sectional design plus convenience sampling means this is an **association**. A plausible alternative explanation is self-selection: more proactive or already-confident students may be more likely both to seek out services and to feel ready. That's exactly why we propose a pre–post study as future research.

### Why did you also run correlations?

As exploratory support for the same pattern. Awareness correlated moderately with readiness (r = .43, p < .001) and year of study weakly (r = .27, p = .002). Spearman's ρ was reported alongside Pearson's r as a robustness check, because Likert data isn't strictly interval.

### Your satisfaction score is based on only 38 people — isn't that too small?

Those 38 are every service user in our sample, not a subsample. Cronbach's α held at .767 even at that n. But we do treat finer subgroups (e.g., Mathematics, n = 12) cautiously and say so.

---

## Findings questions

### What was the headline result?

Two things in tension. Students who used the services reported significantly higher readiness (3.23 vs. 2.74, d = 0.60), so the services appear to matter. But only 31.1% of students had ever used them, awareness averaged below the scale midpoint, and the single most common reason for non-use was not knowing the services existed. The services aren't useless — they're largely invisible.

### Interview support scored 1.55 out of 5. Is the service that bad?

More likely it barely exists. Of the 38 users, 94.7% had only used internship information or announcements; just 2 had used interview preparation and 3 had used CV support. The low rating probably reflects **absence** rather than poor quality. We flag this as one of our unexpected findings.

### Does your data match the existing literature?

Strikingly, yes on utilisation. Our 31.1% almost exactly reproduces the UK Office for Students figure of 33% who ever use centralised career services — the "satisfaction–utilisation paradox" replicates at KIU. It also matches the 2025 UK finding that engagement with internship support is associated with higher perceived employability.

### Where do your findings *contradict* the literature?

Western studies typically find students most satisfied with transactional help (CV reviews, mock interviews) and least satisfied with deep personalised guidance. At KIU the pattern is reversed: transactional preparation is the **weakest**-rated area. Our explanation is that these services are barely delivered here, rather than delivered badly.

### Why include open-ended responses?

They explain the numbers. The very low interview-support score becomes interpretable once students write that they "don't get any tips on how to prepare CVs or for interviews." Four themes emerged: low awareness/visibility, late communication, field-mismatched opportunities (raised mainly by Management and Mathematics students), and lack of practical preparation.

### What should KIU improve first?

Visibility, because that's where the bottleneck is and it's the cheapest fix. Students themselves chose earlier communication (38.5%) and a central internship platform (21.3%) as the top two priorities. Second tier: actually deliver CV and interview preparation, and build field-specific partnerships for Management and Mathematics students.

---

## Critical / reflective questions

### What is the biggest limitation?

Convenience sampling and the resulting skew toward 3rd-year CS students. Beyond that: self-selection as a confound, self-reported perceptions rather than actual placement outcomes, a custom instrument with only minimal piloting, and single-institution scope.

### If you did this again, what would you change?

Stratify recruitment so Management and Mathematics are properly represented, and run a pre–post design around a specific service (e.g., a mock-interview workshop) so we could test causation rather than association.

### What would you do with more time?

Follow-up interviews with the students who reported field-mismatched opportunities, to check whether that complaint generalises or is an artifact of our small Management and Mathematics subgroups.

### Why should anyone care about this study?

Because the fix implied by the data is cheap. The dominant barrier isn't resourcing or quality — it's that students don't know the services exist. Communication and a central platform cost far less than hiring advisers, and our data suggests raising utilisation is likely to be genuinely valuable rather than cosmetic.

---

## Presentation logistics

- **Total time:** 12–17 minutes team + 3–5 min Q&A
- **Section timing:** Intro 3–4 · Literature 2–3 · Methodology 2–3 · Results 3–4 · Discussion/Conclusion 2–3
- **Slides:** min 18pt font, one idea per slide, slide numbers, every figure titled with labelled axes
- **Must-have visuals:** the readiness-by-group bar chart (the money slide) and the service-evaluation chart (the 1.55 bar tells the story visually)
- **Rehearse saying "association, not causation" naturally** — it's the single most likely trap question
