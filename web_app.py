from flask import Flask, render_template, request, redirect
from flask import request
from flask import jsonify
from db import init_db, add_transaction, get_all_transactions
from db import delete_transaction
from analytics import get_monthly_summary
from analytics import forecast_next_months
from analytics import detect_anomalies
from ai_llm import get_llm_budget_advice

app = Flask(__name__)
init_db()

@app.route("/")
def home():

    transactions = get_all_transactions()
    months, totals, avg, std = get_monthly_summary()
    predictions = forecast_next_months(totals).tolist() if len(totals) >= 2 else []
    anomalies = detect_anomalies(transactions)

    lang = request.args.get("lang", "en")

    return render_template(
        "index.html",
        transactions=transactions,
        months=months,
        totals=totals,
        avg=avg,
        std=std,
        predictions=predictions,
        anomalies=anomalies,
        lang=lang
    )


@app.route("/ai-advice", methods=["POST"])
def ai_advice():

    transactions = get_all_transactions()
    months, totals, avg, std = get_monthly_summary()
    predictions = forecast_next_months(totals).tolist() if len(totals) >= 2 else []
    anomalies = detect_anomalies(transactions)

    lang = request.form.get("lang", "en")

    summary = (
        f"Totals: {[round(t/100, 1) for t in totals]}\n"
        f"Avg: {round(avg/100, 1)}\n"
        f"Volatility: {round(std/100, 1)}\n"
        f"Forecast: {[round(p/100, 1) for p in predictions]}"
    )


    advice = get_llm_budget_advice(lang=lang, summary=summary)

    return jsonify({"advice": advice})


@app.route("/add", methods=["POST"])
def add():
    date = request.form["date"]
    amount = float(request.form["amount"])
    category = request.form["category"]
    lang = request.form.get("lang", "en")

    amount_cents = int(round(amount * 100))
    add_transaction(date, amount_cents, category)

    return redirect(f"/?lang={lang}")


@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete(transaction_id):
    lang = request.form.get("lang", "en")
    delete_transaction(transaction_id)
    return redirect(f"/?lang={lang}")
