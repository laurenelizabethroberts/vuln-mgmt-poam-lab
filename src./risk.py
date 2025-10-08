# src/risk.py
_CRIT_WEIGHT = {"Low": 0, "Medium": 1, "High": 2, "Critical": 3}

def compute_risk_score(cvss_base: float, exploit_available: bool, asset_criticality: str) -> int:
    exploit_bonus = 2.0 if exploit_available else 0.0
    crit_bonus = _CRIT_WEIGHT.get(asset_criticality.title(), 0)
    score = cvss_base + exploit_bonus + crit_bonus
    return int(round(score))
