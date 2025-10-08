# src/mappings.py
import re

# Minimal illustrative patterns → control families
_RULES = [
    (r"(authentication|credential|password|mfa)", "IA-2, IA-5"),
    (r"(encryption|tls|openssl|heartbleed)", "SC-12, SC-13"),
    (r"(logging|monitor|siem|detection)", "AU-2, AU-6, SI-4"),
    (r"(patch|vulnerability|scan|remediation)", "RA-5, SI-2"),
    (r"(network|firewall|segmentation|rdp|smb)", "SC-7, AC-4"),
    (r"(change|configuration|baseline)", "CM-2, CM-6"),
    (r"(data|exfiltration|leak)", "SI-4, SC-28"),
    (r"(access|iam|authorization)", "AC-2, AC-3"),
    (r"(malware|rce|remote code)", "SI-3, SI-4"),
    (r"(supply chain|dependency|library|log4j|spring4shell|xz)", "SR-3, SI-2, RA-5"),
    (r"(s3|bucket|object storage|public access)", "AC-3, AC-6, SC-7, SI-4"),
]

def map_controls_for_row(title: str) -> str:
    t = title.lower()
    hits = []
    for pattern, controls in _RULES:
        if re.search(pattern, t, re.I):
            hits.append(controls)
    return "; ".join(sorted(set(hits))) if hits else "RA-5; SI-2"
