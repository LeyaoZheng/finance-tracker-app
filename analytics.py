import numpy as np
from db import get_conn

def get_monthly_summary():
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT substr(date, 1, 7) AS month,
                   SUM(amount_cents) AS total
            FROM transactions
            GROUP BY month
            ORDER BY month;
        """).fetchall()

    months = [r["month"] for r in rows]
    totals = np.array([r["total"] for r in rows], dtype=np.int64)

    if len(totals) == 0:
        return months, totals, 0, 0

    avg = np.mean(totals)
    std = np.std(totals)

    return months, totals, avg, std
