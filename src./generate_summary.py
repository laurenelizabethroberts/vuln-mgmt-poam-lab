# src/generate_summary.py
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
POAM = ROOT / "docs" / "POAM_filled.csv"
OUT  = ROOT / "docs" / "Executive_Summary.md"

TEMPLATE_TOP = """# 🧾 Executive Summary – Vulnerability Management + POA&M Lab

This document summarizes key findings, remediation actions, and compliance alignment for this simulated vulnerability management program.

---
"""

def main():
    if not POAM.exists():
        raise SystemExit("POAM file not found. Run poam_builder.py first.")

    df = pd.read_csv(POAM)
    top = df.sort_values("Risk_Score", ascending=False).head(5)

    lines = [TEMPLATE_TOP, "## 🔍 Top Risks Identified\n"]
    for _, r in top.iterrows():
        lines.append(f"- **{r['Vulnerability_Title']}** on `{r['System']}` (Severity: {r['Severity']}, Risk: {r['Risk_Score']})")
    lines.append("\n---\n")
    lines.append("## 🛠️ Mitigation Summary\n- See detailed POA&M entries in `docs/POAM_filled.csv`.\n")
    lines.append("\n---\n")
    lines.append("## 🧩 Compliance Alignment\n- NIST 800-53: RA-5, SI-2, CM-6, AC-3, SC-7, SI-4\n- FISMA: Continuous Monitoring & POA&M tracking\n")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] Executive summary updated → {OUT}")

if __name__ == "__main__":
    main()
