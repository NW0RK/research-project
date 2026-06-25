# Survey Questionnaire

## Title

Student Perceptions of KIU Internship Support Services

## Introductory Text

We are conducting a student research project for the Basic Research Methods and Tools course. The purpose of this survey is to understand how KIU undergraduate students perceive KIU's internship support services. The survey should take approximately 5-7 minutes. Participation is voluntary, and responses will be used only for academic purposes and reported in summary form.

Please do not write your name, student ID, email address, phone number, or other identifying information.

## Google Forms Branching Setup

Use the following section logic:

1. Make the consent question required.
2. If the respondent selects "No, I do not agree to participate," send them to a final thank-you section and submit the form.
3. If the respondent selects "Yes, I agree to participate," continue to the survey.
4. If `used_support` is "Yes," show the support-use and service-evaluation sections.
5. If `used_support` is "No," skip the service-evaluation section and show the non-use reason section.
6. All consenting respondents should answer the readiness, improvement priority, and open-ended sections.

## Section 1: Consent

1. Do you agree to participate in this survey?
   - Yes, I agree to participate.
   - No, I do not agree to participate.

Suggested CSV column name: `consent`

## Section 2: Academic Background

2. What is your year of study?
   - 1st year
   - 2nd year
   - 3rd year
   - 4th year
   - Other

Suggested CSV column name: `year_of_study`

3. Which school are you enrolled in?
   - Computer Science and Engineering
   - Management
   - Medicine
   - Other

Suggested CSV column name: `school`

## Section 3: Internship Experience

4. Have you searched for an internship during your undergraduate studies?
   - Yes
   - No

Suggested CSV column name: `searched_for_internship`

5. Have you completed an internship during your undergraduate studies?
   - Yes
   - No

Suggested CSV column name: `completed_internship`

## Section 4: Awareness and Usage

Use a 1-5 scale where 1 = Strongly disagree and 5 = Strongly agree.

6. I am aware of KIU internship support services.

Suggested CSV column name: `awareness_score`

7. Have you used any KIU internship support services?
   - Yes
   - No

Suggested CSV column name: `used_support`

## Section 5A: Support Use Details

Show this section only to respondents who answered "Yes" to using KIU internship support services.

8. Which KIU internship support services have you used? Select all that apply.
   - Internship information or announcements
   - CV or resume support
   - Application support
   - Interview preparation
   - Employer or alumni events
   - One-to-one advising
   - Other

Suggested CSV column name: `support_services_used`

Use a 1-5 scale where 1 = Strongly disagree and 5 = Strongly agree.

9. Internship-related information is easy to find.
10. Communication about internship opportunities is clear and timely.
11. KIU provides useful support for internship applications.
12. KIU provides useful CV or resume support.
13. KIU provides useful interview preparation support.
14. KIU provides helpful employer or industry connections.
15. Internship support services are easy to access.
16. Overall, I am satisfied with KIU internship support services.
17. KIU support services have improved my internship readiness.

Suggested CSV column names:

- `info_availability`
- `communication_quality`
- `application_support`
- `cv_support`
- `interview_support`
- `industry_connections`
- `accessibility`
- `overall_satisfaction`
- `support_readiness_impact`

## Section 5B: Non-Use Reason

Show this section only to respondents who answered "No" to using KIU internship support services.

18. What is the main reason you have not used KIU internship support services?
   - I did not know the services existed
   - I knew about them but did not need them
   - I did not know how to access them
   - The available services did not seem relevant to my field
   - I planned to use them later
   - Other

Suggested CSV column name: `nonuse_reason`

## Section 6: Internship Readiness

Ask all consenting respondents. Use a 1-5 scale where 1 = Strongly disagree and 5 = Strongly agree.

19. I feel confident finding internship opportunities.
20. I feel confident preparing a strong CV or resume.
21. I feel confident preparing for internship interviews.
22. I understand what employers expect from interns.

Suggested CSV column names:

- `finding_confidence`
- `cv_confidence`
- `interview_confidence`
- `employer_expectations`

## Section 7: Improvement Priority

23. Which improvement would help students the most?
   - Earlier communication about internship opportunities
   - One central internship information platform
   - More CV or resume support
   - More mock interview practice
   - More employer and alumni networking events
   - More school-specific internship guidance
   - Other

Suggested CSV column name: `top_improvement_priority`

## Section 8: Open-Ended Questions

24. What is the biggest weakness of KIU internship support services?

Suggested CSV column name: `biggest_weakness`

25. What improvement would you suggest for KIU internship support services?

Suggested CSV column name: `improvement_suggestion`

## Notes for Google Forms Setup

- Keep consent, academic background, usage, readiness, and improvement priority required.
- Keep open-ended questions optional to reduce survey fatigue.
- Use the column names listed in `data/codebook.md` when preparing the CSV for analysis.
- Do not include names, student IDs, emails, phone numbers, or other direct identifiers.
