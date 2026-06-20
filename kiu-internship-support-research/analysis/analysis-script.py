from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_PATH = BASE_DIR / "data" / "raw" / "google-forms-export-placeholder.csv"
OUTPUT_DIR = BASE_DIR / "analysis" / "outputs"

CATEGORICAL_COLUMNS = [
    "year_of_study",
    "school",
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
    "readiness_improvement",
]

NUMERIC_COLUMNS = ["awareness_score"] + SERVICE_COLUMNS + READINESS_COLUMNS


def standardize_yes_no(value):
    if pd.isna(value):
        return pd.NA
    text = str(value).strip().lower()
    if text in {"yes", "y", "true", "1"}:
        return "Yes"
    if text in {"no", "n", "false", "0"}:
        return "No"
    return pd.NA


def load_and_clean_data(path):
    df = pd.read_csv(path)
    df.columns = [column.strip() for column in df.columns]

    for column in ["searched_for_internship", "completed_internship", "used_support"]:
        if column in df.columns:
            df[column] = df[column].apply(standardize_yes_no)

    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df["satisfaction_score"] = df[SERVICE_COLUMNS].mean(axis=1)
    df["readiness_score"] = df[READINESS_COLUMNS].mean(axis=1)
    return df


def categorical_frequency_table(df):
    tables = []
    for column in CATEGORICAL_COLUMNS:
        counts = df[column].value_counts(dropna=False).rename_axis("category").reset_index(name="count")
        counts["variable"] = column
        counts["percentage"] = (counts["count"] / len(df) * 100).round(1)
        tables.append(counts[["variable", "category", "count", "percentage"]])
    return pd.concat(tables, ignore_index=True)


def scale_mean_table(df):
    columns = ["awareness_score"] + SERVICE_COLUMNS + READINESS_COLUMNS + [
        "satisfaction_score",
        "readiness_score",
    ]
    summary = (
        df[columns]
        .agg(["count", "mean", "std", "min", "max"])
        .transpose()
        .reset_index()
        .rename(columns={"index": "variable"})
    )
    summary["mean"] = summary["mean"].round(2)
    summary["std"] = summary["std"].round(2)
    return summary


def readiness_group_comparison(df):
    grouped = (
        df.groupby("used_support", dropna=False)["readiness_score"]
        .agg(["count", "mean", "std"])
        .reset_index()
    )
    grouped["mean"] = grouped["mean"].round(2)
    grouped["std"] = grouped["std"].round(2)
    return grouped


def run_ttest(df):
    used = df.loc[df["used_support"] == "Yes", "readiness_score"].dropna()
    not_used = df.loc[df["used_support"] == "No", "readiness_score"].dropna()

    if len(used) < 2 or len(not_used) < 2:
        return pd.DataFrame(
            [
                {
                    "test": "Independent samples t-test",
                    "status": "Not run",
                    "reason": "Each group needs at least two valid readiness scores.",
                    "used_support_n": len(used),
                    "not_used_support_n": len(not_used),
                    "t_statistic": pd.NA,
                    "p_value": pd.NA,
                }
            ]
        )

    result = stats.ttest_ind(used, not_used, equal_var=False)
    return pd.DataFrame(
        [
            {
                "test": "Welch independent samples t-test",
                "status": "Run",
                "reason": "Compares readiness scores by support usage group.",
                "used_support_n": len(used),
                "not_used_support_n": len(not_used),
                "used_support_mean": round(used.mean(), 2),
                "not_used_support_mean": round(not_used.mean(), 2),
                "t_statistic": round(result.statistic, 4),
                "p_value": round(result.pvalue, 4),
            }
        ]
    )


def save_charts(df, output_dir):
    usage_counts = df["used_support"].value_counts().sort_index()
    usage_counts.plot(kind="bar", color=["#4C78A8", "#F58518"])
    plt.title("Use of KIU Internship Support Services")
    plt.xlabel("Used support services")
    plt.ylabel("Number of respondents")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_dir / "support-usage-counts.png", dpi=150)
    plt.close()

    service_means = df[SERVICE_COLUMNS].mean().sort_values()
    service_means.plot(kind="barh", color="#54A24B")
    plt.title("Mean Service Evaluation Scores")
    plt.xlabel("Mean score (1-5)")
    plt.xlim(1, 5)
    plt.tight_layout()
    plt.savefig(output_dir / "service-evaluation-means.png", dpi=150)
    plt.close()

    readiness_by_usage = df.groupby("used_support")["readiness_score"].mean().sort_index()
    readiness_by_usage.plot(kind="bar", color=["#4C78A8", "#F58518"])
    plt.title("Mean Readiness Score by Support Usage")
    plt.xlabel("Used support services")
    plt.ylabel("Mean readiness score")
    plt.ylim(1, 5)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_dir / "readiness-by-support-usage.png", dpi=150)
    plt.close()


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = load_and_clean_data(RAW_PATH)
    df.to_csv(OUTPUT_DIR / "cleaned-survey-data.csv", index=False)

    categorical_frequency_table(df).to_csv(OUTPUT_DIR / "categorical-frequencies.csv", index=False)
    scale_mean_table(df).to_csv(OUTPUT_DIR / "scale-means.csv", index=False)
    readiness_group_comparison(df).to_csv(OUTPUT_DIR / "readiness-by-support-usage.csv", index=False)
    run_ttest(df).to_csv(OUTPUT_DIR / "ttest-results.csv", index=False)
    save_charts(df, OUTPUT_DIR)

    print("Analysis complete.")
    print(f"Rows analyzed: {len(df)}")
    print(f"Outputs saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

