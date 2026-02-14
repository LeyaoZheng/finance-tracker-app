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

def forecast_next_months(totals, months_ahead=3):
    if len(totals) < 2:
        return []

    # Smooth with simple moving average
    smoothed = totals.copy()

    if len(totals) >= 3:
        for i in range(1, len(totals)-1):
            smoothed[i] = (totals[i-1] + totals[i] + totals[i+1]) / 3

    x = np.arange(len(smoothed))
    y = smoothed

    m, b = np.polyfit(x, y, 1)

    future_x = np.arange(len(smoothed), len(smoothed) + months_ahead)
    predictions = m * future_x + b

    return predictions.astype(int)


def detect_anomalies(transactions):
    if not transactions:
        return []

    amounts = np.array([t["amount_cents"] for t in transactions])

    median = np.median(amounts)

    anomalies = []
    for t in transactions:
        if abs(t["amount_cents"]) > 2 * abs(median):
            anomalies.append(t["id"])

    return anomalies

