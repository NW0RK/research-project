# Evaluating the Effectiveness of KIU's Internship Support Services for Undergraduate Students

This repository contains the working files for a Basic Research Methods and Tools final project. The study evaluates how KIU undergraduate students perceive the effectiveness of KIU's internship support services in helping them find, prepare for, and apply to internships.

The team will collect questionnaire responses through Google Forms. This repository does not contain a survey app; it contains the research plan, methodology drafts, data structure, dummy data, analysis scripts, report materials, and presentation materials needed to complete the project.

## Main Research Question

How effective do KIU undergraduate students perceive KIU's internship support services to be in helping them find, prepare for, and apply to internships?

## Hypotheses

H0: There is no significant difference in perceived internship readiness between students who have used KIU internship support services and students who have not.

H1: Students who have used KIU internship support services report significantly higher perceived internship readiness than students who have not.

## Project Focus

The study measures:

- Awareness of KIU internship support services
- Usage of KIU internship support services
- Satisfaction with the services among students who used support
- Perceived usefulness of specific support areas
- Perceived internship readiness
- Reasons students do not use support services
- Priority improvements students want most
- Weaknesses and improvement suggestions

## Folder Structure

```text
literature-review/   Search strategy, source matrix, and literature review draft
methodology/         Study design, variables, sampling, ethics, and questionnaire
data/                Raw Google Forms export placeholder, cleaned example data, and codebook
analysis/            Analysis plan, Python script, output summaries, and theme-coding guide
report/              Academic report sections, templates, and references file
presentation/        Slide outline, speaker notes, and Q&A preparation
appendices/          Survey, consent form, and extra tables
```

## Collecting Data With Google Forms

1. Create a new Google Form using the questionnaire in `methodology/survey-questionnaire.md`.
2. Add the informed consent statement at the beginning of the form.
3. Use section branching:
   - "No" consent ends the form.
   - Support users answer service evaluation and support impact questions.
   - Non-users answer the non-use reason question.
   - Everyone who consents answers readiness and improvement priority questions.
4. Use consistent Likert scale labels: 1 = Strongly disagree, 5 = Strongly agree.
5. Avoid collecting names, student IDs, emails, phone numbers, or other direct identifiers unless your instructor explicitly requires them.
6. Share the form link with KIU undergraduate students through appropriate class channels, student groups, or university communication channels.
7. Aim for 50+ valid responses if possible. Treat 80+ as a stretch target and 30 as the minimum practical threshold.

## Exporting Google Forms Responses to CSV

1. Open the Google Form.
2. Go to the `Responses` tab.
3. Click the green Google Sheets icon to create or open the response spreadsheet.
4. In Google Sheets, select `File > Download > Comma-separated values (.csv)`.
5. Save the file as `data/raw/google-forms-export-placeholder.csv`.
6. Check that the column names match the codebook in `data/codebook.md`.
7. Keep branching fields blank when they do not apply. For example, non-users should have blank service-evaluation fields.
8. Run the analysis script after replacing the dummy data.

## Running the Python Analysis

Install the required package if needed:

```bash
pip install pandas
```

For polished chart styling, you may also install `matplotlib`. The script can still create basic PNG charts when Pillow is available.

From the `kiu-internship-support-research` folder, run:

```bash
python analysis/analysis-script.py
```

From the workspace root, run:

```bash
python kiu-internship-support-research/analysis/analysis-script.py
```

The script will:

- Load the CSV file
- Validate that expected columns are present
- Remove rows where the respondent did not consent
- Clean basic response fields
- Report missing values
- Calculate frequencies and percentages
- Calculate mean satisfaction among support users
- Calculate readiness from neutral readiness items only
- Compare readiness between students who used support and those who did not
- Run a Welch t-test when both groups have enough responses
- Report mean difference, 95% confidence interval, Cohen's d, and Cronbach's alpha when possible
- Save summary tables, charts, and `analysis/outputs/analysis-summary.md`

You can also open `analysis/python-analysis-notebook.ipynb` in Jupyter Notebook, JupyterLab, or Google Colab.

## Using the Report Materials

The `report/` folder follows a standard academic structure:

- Abstract
- Introduction
- Literature Review
- Methodology
- Results
- Discussion
- Conclusion
- References
- Appendices

Start with `report/final-report-outline.md`, then copy or adapt text from the draft files. Use `analysis/outputs/analysis-summary.md` after running the script to fill the results, discussion, and conclusion sections with actual findings.

## Preparing the Presentation

Use `presentation/slide-outline.md` for a 12-17 minute team presentation. Assign slides to team members early, and use `presentation/speaker-notes-template.md` to keep the delivery focused. The presentation should emphasize the research question, method, key results, interpretation, limitations, and practical recommendations for improving internship support services. Use `presentation/q-and-a-prep.md` to prepare for likely instructor questions.

## Recommended Workflow

1. Finalize the research question and hypotheses.
2. Complete the literature source matrix and confirm the final citation style.
3. Build the Google Forms questionnaire from the template.
4. Collect responses.
5. Export the responses as CSV.
6. Run the analysis script.
7. Insert results into the report templates.
8. Prepare the presentation and rehearse as a team.
