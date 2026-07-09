import math
from pathlib import Path

try:
    import pandas as pd
except ModuleNotFoundError as exc:
    raise SystemExit("pandas is required. Install it with: pip install pandas") from exc

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    plt = None

try:
    from PIL import Image, ImageDraw, ImageFont
except ModuleNotFoundError:
    Image = None
    ImageDraw = None
    ImageFont = None


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_PATH = BASE_DIR / "data" / "raw" / "final_survey_results.csv"
OUTPUT_DIR = BASE_DIR / "analysis" / "outputs"

RAW_COLUMN_ALIASES = {
    "1. Do you agree to participate in this survey?": "consent",
    "2. What is your year of study?": "year_of_study",
    "3. Which school are you enrolled in?": "school",
    "4. Have you searched for an internship during your undergraduate studies?": "searched_for_internship",
    "5. Have you completed an internship during your undergraduate studies?": "completed_internship",
    "6. I am aware of KIU internship support services.": "awareness_score",
    "7. Have you used any KIU internship support services?": "used_support",
    "8. Which KIU internship support services have you used? Select all that apply.": "support_services_used",
    "9. Internship-related information is easy to find.": "info_availability",
    "10. Communication about internship opportunities is clear and timely.": "communication_quality",
    "11. KIU provides useful support for internship applications.": "application_support",
    "12. KIU provides useful CV or resume support.": "cv_support",
    "13. KIU provides useful interview preparation support.": "interview_support",
    "14. KIU provides helpful employer or industry connections.": "industry_connections",
    "15. Internship support services are easy to access.": "accessibility",
    "16. Overall, I am satisfied with KIU internship support services.": "overall_satisfaction",
    "17. KIU support services have improved my internship readiness.": "support_readiness_impact",
    "18. What is the main reason you have not used KIU internship support services?": "nonuse_reason",
    "19. I feel confident finding internship opportunities.": "finding_confidence",
    "20. I feel confident preparing a strong CV or resume.": "cv_confidence",
    "21. I feel confident preparing for internship interviews.": "interview_confidence",
    "22. I understand what employers expect from interns.": "employer_expectations",
    "23. Which improvement would help students the most?": "top_improvement_priority",
    "24. What is the biggest weakness of KIU internship support services?": "biggest_weakness",
    "25. What improvement would you suggest for KIU internship support services?": "improvement_suggestion",
}

EXPECTED_COLUMNS = [
    "respondent_id",
    "consent",
    "year_of_study",
    "school",
    "searched_for_internship",
    "completed_internship",
    "awareness_score",
    "used_support",
    "support_services_used",
    "nonuse_reason",
    "info_availability",
    "communication_quality",
    "application_support",
    "cv_support",
    "interview_support",
    "industry_connections",
    "accessibility",
    "overall_satisfaction",
    "finding_confidence",
    "cv_confidence",
    "interview_confidence",
    "employer_expectations",
    "support_readiness_impact",
    "top_improvement_priority",
    "biggest_weakness",
    "improvement_suggestion",
]

CATEGORICAL_COLUMNS = [
    "year_of_study",
    "school",
    "searched_for_internship",
    "completed_internship",
    "used_support",
    "nonuse_reason",
    "top_improvement_priority",
]

YES_NO_COLUMNS = [
    "consent",
    "searched_for_internship",
    "completed_internship",
    "used_support",
]

SERVICE_COLUMNS = [
    "info_availability",
    "communication_quality",
    "application_support",
    "cv_support",
    "interview_support",
    "industry_connections",
    "accessibility",
    "overall_satisfaction",
]

READINESS_COLUMNS = [
    "finding_confidence",
    "cv_confidence",
    "interview_confidence",
    "employer_expectations",
]

NUMERIC_COLUMNS = [
    "awareness_score",
    *SERVICE_COLUMNS,
    *READINESS_COLUMNS,
    "support_readiness_impact",
]

LABELS = {
    "awareness_score": "Awareness",
    "info_availability": "Information availability",
    "communication_quality": "Communication quality",
    "application_support": "Application support",
    "cv_support": "CV support",
    "interview_support": "Interview support",
    "industry_connections": "Industry connections",
    "accessibility": "Accessibility",
    "overall_satisfaction": "Overall satisfaction",
    "finding_confidence": "Finding confidence",
    "cv_confidence": "CV confidence",
    "interview_confidence": "Interview confidence",
    "employer_expectations": "Employer expectations",
    "support_readiness_impact": "Support readiness impact",
    "satisfaction_score": "Satisfaction score",
    "readiness_score": "Readiness score",
}


def _beta_continued_fraction(a, b, x, max_iterations=200, tolerance=3e-12):
    tiny = 1e-300
    qab = a + b
    qap = a + 1
    qam = a - 1
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < tiny:
        d = tiny
    d = 1.0 / d
    h = d

    for m in range(1, max_iterations + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        h *= d * c

        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < tolerance:
            break

    return h


def regularized_beta(x, a, b):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0

    log_beta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(log_beta + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1) / (a + b + 2):
        return front * _beta_continued_fraction(a, b, x) / a
    return 1 - front * _beta_continued_fraction(b, a, 1 - x) / b


def student_t_cdf(t_value, degrees_freedom):
    if degrees_freedom <= 0:
        return pd.NA
    x = degrees_freedom / (degrees_freedom + t_value**2)
    beta_value = regularized_beta(x, degrees_freedom / 2, 0.5)
    if t_value >= 0:
        return 1 - 0.5 * beta_value
    return 0.5 * beta_value


def student_t_ppf(probability, degrees_freedom):
    if not 0 < probability < 1:
        raise ValueError("Probability must be between 0 and 1.")
    if degrees_freedom <= 0:
        return pd.NA
    if probability == 0.5:
        return 0.0

    sign = 1
    target = probability
    if probability < 0.5:
        sign = -1
        target = 1 - probability

    low = 0.0
    high = 1.0
    while student_t_cdf(high, degrees_freedom) < target:
        high *= 2
        if high > 1e6:
            raise RuntimeError("Could not bracket Student t critical value.")

    for _ in range(100):
        midpoint = (low + high) / 2
        if student_t_cdf(midpoint, degrees_freedom) < target:
            low = midpoint
        else:
            high = midpoint

    return sign * (low + high) / 2


def standardize_yes_no(value):
    if pd.isna(value):
        return pd.NA
    text = str(value).strip().lower()
    if text.startswith("yes") or text in {"y", "true", "1"}:
        return "Yes"
    if text.startswith("no") or text in {"n", "false", "0"}:
        return "No"
    return pd.NA


def validate_columns(df):
    missing = [column for column in EXPECTED_COLUMNS if column not in df.columns]
    if missing:
        expected = ", ".join(EXPECTED_COLUMNS)
        missing_text = ", ".join(missing)
        raise ValueError(
            "The CSV is missing expected columns: "
            f"{missing_text}\nExpected columns are: {expected}"
        )


def normalize_raw_columns(df):
    df = df.rename(columns=RAW_COLUMN_ALIASES)

    if "respondent_id" not in df.columns:
        df.insert(0, "respondent_id", [f"R{index:03d}" for index in range(1, len(df) + 1)])

    return df


def load_and_clean_data(path):
    if not path.exists():
        raise FileNotFoundError(f"Could not find CSV file: {path}")

    df = pd.read_csv(path)
    df.columns = [column.strip() for column in df.columns]
    df = normalize_raw_columns(df)
    validate_columns(df)

    for column in YES_NO_COLUMNS:
        df[column] = df[column].apply(standardize_yes_no)

    original_count = len(df)
    df = df.loc[df["consent"] == "Yes"].copy()
    dropped_count = original_count - len(df)

    if df.empty:
        raise ValueError("No consenting responses found after filtering `consent` == Yes.")

    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    support_users = df["used_support"] == "Yes"
    df["satisfaction_score"] = pd.NA
    df.loc[support_users, "satisfaction_score"] = df.loc[support_users, SERVICE_COLUMNS].mean(axis=1)
    df["satisfaction_score"] = pd.to_numeric(df["satisfaction_score"], errors="coerce")
    df["readiness_score"] = df[READINESS_COLUMNS].mean(axis=1)
    df.attrs["dropped_nonconsent_count"] = dropped_count
    return df


def categorical_frequency_table(df):
    tables = []
    for column in CATEGORICAL_COLUMNS:
        counts = df[column].fillna("Missing").value_counts().rename_axis("category").reset_index(name="count")
        counts["variable"] = column
        counts["percentage"] = (counts["count"] / len(df) * 100).round(1)
        tables.append(counts[["variable", "category", "count", "percentage"]])
    return pd.concat(tables, ignore_index=True)


def missing_values_table(df):
    columns = EXPECTED_COLUMNS + ["satisfaction_score", "readiness_score"]
    rows = []
    for column in columns:
        missing_count = int(df[column].isna().sum())
        rows.append(
            {
                "variable": column,
                "missing_count": missing_count,
                "missing_percentage": round(missing_count / len(df) * 100, 1),
            }
        )
    return pd.DataFrame(rows)


def summarize_series(name, series, scope):
    clean = pd.to_numeric(series, errors="coerce").dropna()
    return {
        "variable": name,
        "label": LABELS.get(name, name),
        "scope": scope,
        "count": len(clean),
        "mean": round(clean.mean(), 2) if len(clean) else pd.NA,
        "std": round(clean.std(ddof=1), 2) if len(clean) > 1 else pd.NA,
        "min": round(clean.min(), 2) if len(clean) else pd.NA,
        "max": round(clean.max(), 2) if len(clean) else pd.NA,
    }


def scale_mean_table(df):
    support_df = df.loc[df["used_support"] == "Yes"]
    rows = [summarize_series("awareness_score", df["awareness_score"], "All consenting respondents")]

    for column in SERVICE_COLUMNS:
        rows.append(summarize_series(column, support_df[column], "Support users only"))

    rows.append(summarize_series("satisfaction_score", support_df["satisfaction_score"], "Support users only"))

    for column in READINESS_COLUMNS:
        rows.append(summarize_series(column, df[column], "All consenting respondents"))

    rows.append(summarize_series("readiness_score", df["readiness_score"], "All consenting respondents"))
    rows.append(
        summarize_series(
            "support_readiness_impact",
            support_df["support_readiness_impact"],
            "Support users only",
        )
    )
    return pd.DataFrame(rows)


def readiness_group_comparison(df):
    grouped = (
        df.groupby("used_support", dropna=False)["readiness_score"]
        .agg(["count", "mean", "std"])
        .reset_index()
    )
    grouped["mean"] = grouped["mean"].round(2)
    grouped["std"] = grouped["std"].round(2)
    return grouped


def cohen_d(group_a, group_b):
    n_a = len(group_a)
    n_b = len(group_b)
    if n_a < 2 or n_b < 2:
        return pd.NA
    pooled_variance = (
        ((n_a - 1) * group_a.var(ddof=1)) + ((n_b - 1) * group_b.var(ddof=1))
    ) / (n_a + n_b - 2)
    if pooled_variance <= 0:
        return pd.NA
    return (group_a.mean() - group_b.mean()) / pooled_variance**0.5


def run_ttest(df):
    used = df.loc[df["used_support"] == "Yes", "readiness_score"].dropna()
    not_used = df.loc[df["used_support"] == "No", "readiness_score"].dropna()

    base = {
        "test": "Welch independent samples t-test",
        "used_support_n": len(used),
        "not_used_support_n": len(not_used),
        "used_support_mean": round(used.mean(), 2) if len(used) else pd.NA,
        "not_used_support_mean": round(not_used.mean(), 2) if len(not_used) else pd.NA,
    }

    if len(used) < 2 or len(not_used) < 2:
        return pd.DataFrame(
            [
                {
                    **base,
                    "status": "Not run",
                    "reason": "Each group needs at least two valid readiness scores.",
                    "mean_difference": pd.NA,
                    "ci_95_lower": pd.NA,
                    "ci_95_upper": pd.NA,
                    "degrees_freedom": pd.NA,
                    "t_statistic": pd.NA,
                    "p_value": pd.NA,
                    "cohen_d": pd.NA,
                }
            ]
        )

    var_used = used.var(ddof=1)
    var_not_used = not_used.var(ddof=1)
    standard_error = ((var_used / len(used)) + (var_not_used / len(not_used))) ** 0.5

    if standard_error == 0:
        return pd.DataFrame(
            [
                {
                    **base,
                    "status": "Not run",
                    "reason": "Readiness scores have no variance across comparison groups.",
                    "mean_difference": pd.NA,
                    "ci_95_lower": pd.NA,
                    "ci_95_upper": pd.NA,
                    "degrees_freedom": pd.NA,
                    "t_statistic": pd.NA,
                    "p_value": pd.NA,
                    "cohen_d": pd.NA,
                }
            ]
        )

    mean_difference = used.mean() - not_used.mean()
    numerator = ((var_used / len(used)) + (var_not_used / len(not_used))) ** 2
    denominator = ((var_used / len(used)) ** 2 / (len(used) - 1)) + (
        (var_not_used / len(not_used)) ** 2 / (len(not_used) - 1)
    )
    degrees_freedom = numerator / denominator
    t_statistic = mean_difference / standard_error
    p_value = (1 - student_t_cdf(abs(t_statistic), degrees_freedom)) * 2
    critical_value = student_t_ppf(0.975, degrees_freedom)
    ci_lower = mean_difference - critical_value * standard_error
    ci_upper = mean_difference + critical_value * standard_error

    reported_p_value = "<0.0001" if p_value < 0.0001 else round(p_value, 4)

    return pd.DataFrame(
        [
            {
                **base,
                "status": "Run",
                "reason": "Compares readiness scores by support usage group.",
                "mean_difference": round(mean_difference, 2),
                "ci_95_lower": round(ci_lower, 2),
                "ci_95_upper": round(ci_upper, 2),
                "degrees_freedom": round(degrees_freedom, 2),
                "t_statistic": round(t_statistic, 4),
                "p_value": reported_p_value,
                "cohen_d": round(cohen_d(used, not_used), 3),
            }
        ]
    )


def cronbach_alpha(items):
    complete = items.dropna()
    if complete.shape[0] < 2 or complete.shape[1] < 2:
        return pd.NA
    item_variances = complete.var(axis=0, ddof=1)
    total_variance = complete.sum(axis=1).var(ddof=1)
    if total_variance == 0:
        return pd.NA
    item_count = complete.shape[1]
    return item_count / (item_count - 1) * (1 - item_variances.sum() / total_variance)


def reliability_table(df):
    support_df = df.loc[df["used_support"] == "Yes"]
    checks = [
        ("readiness_items", READINESS_COLUMNS, df, "All consenting respondents"),
        ("service_evaluation_items", SERVICE_COLUMNS, support_df, "Support users only"),
    ]
    rows = []
    for scale_name, columns, source_df, scope in checks:
        complete_count = source_df[columns].dropna().shape[0]
        alpha = cronbach_alpha(source_df[columns])
        rows.append(
            {
                "scale": scale_name,
                "scope": scope,
                "items": len(columns),
                "complete_response_count": complete_count,
                "cronbach_alpha": round(alpha, 3) if pd.notna(alpha) else pd.NA,
                "status": "Run" if pd.notna(alpha) else "Not run",
            }
        )
    return pd.DataFrame(rows)


def truncate_label(label, max_length=44):
    text = str(label)
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


def chart_font(size):
    if ImageFont is None:
        return None
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


def save_pillow_horizontal_chart(series, title, output_path, max_value=None, value_format="{:.1f}"):
    series = series.dropna()
    if series.empty:
        return

    width = 1100
    row_height = 46
    top_margin = 82
    bottom_margin = 60
    left_margin = 360
    right_margin = 110
    height = top_margin + bottom_margin + row_height * len(series)
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    title_font = chart_font(24)
    label_font = chart_font(16)
    small_font = chart_font(14)

    draw.text((32, 24), title, fill="#1F2933", font=title_font)
    chart_left = left_margin
    chart_right = width - right_margin
    chart_width = chart_right - chart_left
    max_data = float(max_value if max_value is not None else max(series.max(), 1))

    axis_y = height - bottom_margin + 8
    draw.line((chart_left, axis_y, chart_right, axis_y), fill="#9AA5B1", width=1)

    for index, (label, value) in enumerate(series.items()):
        y = top_margin + index * row_height
        bar_height = 24
        bar_width = 0 if max_data == 0 else int(chart_width * float(value) / max_data)
        draw.text((32, y + 4), truncate_label(label), fill="#243B53", font=label_font)
        draw.rectangle(
            (chart_left, y + 4, chart_left + bar_width, y + 4 + bar_height),
            fill="#4C78A8",
        )
        draw.text(
            (chart_left + bar_width + 8, y + 5),
            value_format.format(float(value)),
            fill="#243B53",
            font=small_font,
        )

    image.save(output_path)


def save_pillow_charts(df, output_dir):
    support_users = df["used_support"] == "Yes"

    usage_counts = df["used_support"].value_counts().reindex(["No", "Yes"]).dropna()
    save_pillow_horizontal_chart(
        usage_counts,
        "Use of KIU Internship Support Services",
        output_dir / "support-usage-counts.png",
        value_format="{:.0f}",
    )

    service_means = df.loc[support_users, SERVICE_COLUMNS].mean().sort_values()
    service_means.index = [LABELS.get(label, label) for label in service_means.index]
    save_pillow_horizontal_chart(
        service_means,
        "Mean Service Evaluation Scores Among Support Users",
        output_dir / "service-evaluation-means.png",
        max_value=5,
    )

    readiness_by_usage = df.groupby("used_support")["readiness_score"].mean().reindex(["No", "Yes"]).dropna()
    save_pillow_horizontal_chart(
        readiness_by_usage,
        "Mean Readiness Score by Support Usage",
        output_dir / "readiness-by-support-usage.png",
        max_value=5,
    )

    improvement_counts = df["top_improvement_priority"].dropna().value_counts().head(8).sort_values()
    save_pillow_horizontal_chart(
        improvement_counts,
        "Top Improvement Priorities",
        output_dir / "top-improvement-priorities.png",
        value_format="{:.0f}",
    )


def save_charts(df, output_dir):
    if plt is None:
        if Image is None:
            print("matplotlib and Pillow are not installed; skipping PNG chart exports.")
            return
        print("matplotlib is not installed; using Pillow for basic PNG chart exports.")
        save_pillow_charts(df, output_dir)
        return

    support_users = df["used_support"] == "Yes"

    usage_counts = df["used_support"].value_counts().reindex(["No", "Yes"]).dropna()
    usage_counts.plot(kind="bar", color=["#4C78A8", "#F58518"])
    plt.title("Use of KIU Internship Support Services")
    plt.xlabel("Used support services")
    plt.ylabel("Number of respondents")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_dir / "support-usage-counts.png", dpi=150)
    plt.close()

    service_means = df.loc[support_users, SERVICE_COLUMNS].mean().sort_values()
    service_means.index = [LABELS.get(label, label) for label in service_means.index]
    service_means.plot(kind="barh", color="#54A24B")
    plt.title("Mean Service Evaluation Scores Among Support Users")
    plt.xlabel("Mean score (1-5)")
    plt.xlim(1, 5)
    plt.tight_layout()
    plt.savefig(output_dir / "service-evaluation-means.png", dpi=150)
    plt.close()

    readiness_by_usage = df.groupby("used_support")["readiness_score"].mean().reindex(["No", "Yes"]).dropna()
    readiness_by_usage.plot(kind="bar", color=["#4C78A8", "#F58518"])
    plt.title("Mean Readiness Score by Support Usage")
    plt.xlabel("Used support services")
    plt.ylabel("Mean readiness score")
    plt.ylim(1, 5)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_dir / "readiness-by-support-usage.png", dpi=150)
    plt.close()

    improvement_counts = df["top_improvement_priority"].dropna().value_counts().head(8).sort_values()
    improvement_counts.plot(kind="barh", color="#B279A2")
    plt.title("Top Improvement Priorities")
    plt.xlabel("Number of respondents")
    plt.tight_layout()
    plt.savefig(output_dir / "top-improvement-priorities.png", dpi=150)
    plt.close()


def markdown_table(df, columns):
    subset = df[columns].copy()
    headers = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"
    rows = []
    for _, row in subset.iterrows():
        values = [str(row[column]) if pd.notna(row[column]) else "" for column in columns]
        rows.append("| " + " | ".join(values) + " |")
    return "\n".join([headers, separator, *rows])


def build_summary_markdown(df, frequency_df, scale_df, group_df, ttest_df, reliability_df):
    usage = frequency_df.loc[frequency_df["variable"] == "used_support"].copy()
    usage_text = markdown_table(usage, ["category", "count", "percentage"])

    service_rows = scale_df.loc[scale_df["variable"].isin(SERVICE_COLUMNS)].dropna(subset=["mean"])
    highest_service = service_rows.sort_values("mean", ascending=False).head(1)
    lowest_service = service_rows.sort_values("mean", ascending=True).head(1)
    highest_service_text = (
        f"{highest_service.iloc[0]['label']} ({highest_service.iloc[0]['mean']})"
        if not highest_service.empty
        else "Not available"
    )
    lowest_service_text = (
        f"{lowest_service.iloc[0]['label']} ({lowest_service.iloc[0]['mean']})"
        if not lowest_service.empty
        else "Not available"
    )

    readiness_mean = scale_df.loc[scale_df["variable"] == "readiness_score", "mean"].iloc[0]
    awareness_mean = scale_df.loc[scale_df["variable"] == "awareness_score", "mean"].iloc[0]
    support_impact = scale_df.loc[scale_df["variable"] == "support_readiness_impact", "mean"].iloc[0]

    ttest = ttest_df.iloc[0]
    if ttest["status"] == "Run":
        ttest_text = (
            f"Support users reported a mean readiness score of {ttest['used_support_mean']}, "
            f"compared with {ttest['not_used_support_mean']} for non-users. "
            f"The mean difference was {ttest['mean_difference']} "
            f"(95% CI [{ttest['ci_95_lower']}, {ttest['ci_95_upper']}]), "
            f"t({ttest['degrees_freedom']}) = {ttest['t_statistic']}, "
            f"p = {ttest['p_value']}, Cohen's d = {ttest['cohen_d']}."
        )
    else:
        ttest_text = f"The t-test was not run: {ttest['reason']}"

    improvement = frequency_df.loc[frequency_df["variable"] == "top_improvement_priority"].head(5)
    reliability_text = markdown_table(
        reliability_df,
        ["scale", "scope", "complete_response_count", "cronbach_alpha", "status"],
    )

    return f"""# Analysis Summary

Rows analyzed after consent filtering: {len(df)}

Rows removed because consent was not "Yes": {df.attrs.get("dropped_nonconsent_count", 0)}

## Support Usage

{usage_text}

## Main Scale Results

- Mean awareness score: {awareness_mean}
- Mean readiness score: {readiness_mean}
- Mean support readiness impact among support users: {support_impact}
- Highest-rated service area among support users: {highest_service_text}
- Lowest-rated service area among support users: {lowest_service_text}

## Readiness Comparison

{markdown_table(group_df, ["used_support", "count", "mean", "std"])}

{ttest_text}

## Reliability Checks

{reliability_text}

## Top Improvement Priorities

{markdown_table(improvement, ["category", "count", "percentage"])}

## Reporting Caution

Because this project uses a cross-sectional convenience sample, describe the readiness comparison as an association in the surveyed sample. Do not claim that support service usage caused higher readiness.
"""


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = load_and_clean_data(RAW_PATH)
    frequency_df = categorical_frequency_table(df)
    missing_df = missing_values_table(df)
    scale_df = scale_mean_table(df)
    group_df = readiness_group_comparison(df)
    ttest_df = run_ttest(df)
    reliability_df = reliability_table(df)

    df.to_csv(OUTPUT_DIR / "cleaned-survey-data.csv", index=False)
    frequency_df.to_csv(OUTPUT_DIR / "categorical-frequencies.csv", index=False)
    missing_df.to_csv(OUTPUT_DIR / "missing-values.csv", index=False)
    scale_df.to_csv(OUTPUT_DIR / "scale-means.csv", index=False)
    group_df.to_csv(OUTPUT_DIR / "readiness-by-support-usage.csv", index=False)
    ttest_df.to_csv(OUTPUT_DIR / "ttest-results.csv", index=False)
    reliability_df.to_csv(OUTPUT_DIR / "reliability-results.csv", index=False)
    save_charts(df, OUTPUT_DIR)

    summary = build_summary_markdown(df, frequency_df, scale_df, group_df, ttest_df, reliability_df)
    (OUTPUT_DIR / "analysis-summary.md").write_text(summary, encoding="utf-8")

    print("Analysis complete.")
    print(f"Rows analyzed: {len(df)}")
    print(f"Rows removed because consent was not Yes: {df.attrs.get('dropped_nonconsent_count', 0)}")
    print(f"Outputs saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
