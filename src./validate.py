# src/validate.py
REQUIRED_COLS = {
    "host","vuln_title","severity","cvss_base","exploit_available","asset_criticality"
}

def validate_scan_csv(df):
    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"Scan CSV missing required columns: {sorted(missing)}")
