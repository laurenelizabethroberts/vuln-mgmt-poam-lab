# 🧾 Vulnerability Management + POA&M Lab

This lab simulates a real-world vulnerability management process, including identification, prioritization, and documentation of remediation plans using the **Plan of Action & Milestones (POA&M)** format aligned with **NIST 800-53** and **FISMA**.

---

## 📘 Example 1 – Critical Vulnerability (Log4Shell)

| POAM_ID | System | Vulnerability_Title | Severity | NIST_Controls | Risk_Score | Planned_Completion_Date | Status |
|----------|---------|---------------------|-----------|----------------|-------------|--------------------------|---------|
| POAM-2025-001 | app-01 (Prod) | Apache Log4j RCE ("Log4Shell") | Critical | RA-5, SI-2, CM-6, SC-7, SR-3 | 14 | 2025-10-22 | Open |

**Summary:**  
Java application uses vulnerable `log4j-core`. Applied WAF block, upgraded to 2.17.x, verified remediation through rescan.  
[Full POA&M Entry →](docs/POAM_filled.csv)

---

## ☁️ Example 2 – Cloud Misconfiguration (Public S3 Bucket)

| POAM_ID | System | Vulnerability_Title | Severity | NIST_Controls | Risk_Score | Planned_Completion_Date | Status |
|----------|---------|---------------------|-----------|----------------|-------------|--------------------------|---------|
| POAM-2025-002 | AWS `customer-data-prod` S3 Bucket | Publicly Accessible Bucket | High | AC-3, AC-6, SC-7, SI-4 | 12 | 2025-10-20 | Open |

**Summary:**  
AWS S3 bucket configured with public read access. Locked down bucket, applied least privilege IAM policies, enabled AWS Config rules and continuous monitoring.  
[Full POA&M Entry →](docs/POAM_filled.csv)

---

### Tools Used
- Python, Pandas, CSV  
- AWS Security Hub, GuardDuty, Config  
- NIST 800-53 and FISMA mapping  
- Markdown + POA&M reporting

### What I Learned
- How to translate vulnerabilities into **auditable compliance documentation**
- How to map findings to **NIST control families**
- How to build structured, trackable remediation workflows
