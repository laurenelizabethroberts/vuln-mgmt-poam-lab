# src/utils.py
from datetime import date, timedelta

def today_str(delta_days: int = 0) -> str:
    return str(date.today() + timedelta(days=delta_days))
