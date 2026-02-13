from flask import Flask, render_template, request, redirect
from db import init_db, add_transaction, get_all_transactions
from analytics import get_monthly_summary

app = Flask(__name__)
init_db()

@app.route("/")
def home():
    transactions = get_all_transactions()
    months, totals, avg, std = get_monthly_summary()
    
    return render_template("index.html", transactions=transactions,
        months=months,
        totals=totals,
        avg=avg,
        std=std)

@app.route("/add", methods=["POST"])
def add():
    date = request.form["date"]
    amount = float(request.form["amount"])
    category = request.form["category"]

    amount_cents = int(round(amount * 100))
    add_transaction(date, amount_cents, category)

    return redirect("/")

if __name__ == "__main__":
    app.run()
