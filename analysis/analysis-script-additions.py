"""Additions for analysis-script.py — tested against the real dataset."""
from scipy import stats
import pandas as pd

def normality_check(df):
    """Shapiro-Wilk test on the readiness score. Justifies parametric tests."""
    clean = df["readiness_score"].dropna()
    if len(clean) < 3:
        return pd.DataFrame([{"variable": "readiness_score", "status": "Not run",
                              "reason": "Fewer than three valid scores."}])
    w, p = stats.shapiro(clean)
    return pd.DataFrame([{
        "variable": "readiness_score", "test": "Shapiro-Wilk", "n": len(clean),
        "w_statistic": round(w, 4), "p_value": round(p, 4),
        "normal_at_05": "Yes" if p >= 0.05 else "No",
        "status": "Run",
    }])


def correlation_table(df):
    """Pearson (with Spearman robustness check) for awareness/year vs readiness."""
    year_map = {"2nd year": 2, "3rd year": 3, "4th year": 4}
    pairs = [
        ("awareness_score", "readiness_score", df["awareness_score"], df["readiness_score"]),
        ("year_of_study", "readiness_score", df["year_of_study"].map(year_map), df["readiness_score"]),
    ]
    rows = []
    for x_name, y_name, x, y in pairs:
        valid = pd.concat([x, y], axis=1).dropna()
        if len(valid) < 3:
            rows.append({"x": x_name, "y": y_name, "status": "Not run"})
            continue
        a, b = valid.iloc[:, 0], valid.iloc[:, 1]
        r, p_r = stats.pearsonr(a, b)
        rho, p_s = stats.spearmanr(a, b)
        rows.append({
            "x": x_name, "y": y_name, "n": len(valid),
            "pearson_r": round(r, 3), "pearson_p": round(p_r, 4),
            "spearman_rho": round(rho, 3), "spearman_p": round(p_s, 4),
            "status": "Run",
        })
    return pd.DataFrame(rows)