💰 Full-Stack Personal Finance Analytics Platform with LLM Integration

A full-stack financial analytics web application that enables transaction management, statistical forecasting, anomaly detection, and AI-powered budgeting insights.

Live Demo: https://finance-tracker-app-nrx2.onrender.com

Tech Stack: Python, Flask, SQLite, NumPy, OpenAI API, JavaScript, Render

🚀 Features
📊 Financial Analytics

SQL-backed transaction management (CRUD operations)

Monthly aggregation and net income calculation

Statistical volatility analysis (standard deviation via NumPy)

Time-series forecasting for future cash flow trends

Anomaly detection for irregular transactions

🤖 AI Budgeting Advisor

Token-optimized OpenAI LLM integration

Structured financial summary compression

Asynchronous REST endpoint to prevent blocking

Bilingual support (English / Chinese)

Error-handled cloud inference

🌐 Production Deployment

Deployed using Gunicorn on Render

Dynamic port binding for cloud compatibility

Environment-variable secured API key management

Mobile-responsive Progressive Web App (PWA)

Installable on iOS via Safari

🏗 Architecture Overview

Frontend:

HTML/CSS (mobile-first responsive design)

JavaScript Fetch API for asynchronous AI calls

Backend:

Flask REST API

SQLite database

NumPy-based statistical computation

OpenAI API integration for LLM advisory

Cloud:

Render deployment

Gunicorn WSGI server

Secure environment configuration

📈 Core Technical Concepts

RESTful API design

SQL schema modeling and data aggregation

Statistical modeling and volatility analysis

Time-series trend forecasting

Anomaly detection logic

Prompt engineering and token optimization

Asynchronous request handling

Production debugging and cloud deployment

🛠 Installation (Local Development)

Clone the repository

git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker


Create virtual environment

python -m venv .venv
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Set environment variable

export OPENAI_API_KEY="your_api_key_here"


Run the application

python web_app.py


Visit:
http://127.0.0.1:5000

🔐 Environment Variables
Variable	Description
OPENAI_API_KEY	Required for AI budgeting advisor
📦 Deployment

The application is deployed on Render using:

gunicorn web_app:app --bind 0.0.0.0:$PORT


The project supports dynamic port assignment and production WSGI serving.

🎯 Project Highlights

Designed token-efficient LLM integration to minimize API costs

Implemented statistical financial modeling using NumPy

Diagnosed and resolved cloud deployment issues including dynamic port binding and environment configuration

Built cross-platform PWA with iOS installation support

📌 Future Improvements

Add PostgreSQL support

Implement user authentication

Add financial data visualization (Chart.js)

Add AI response caching

Add rate limiting

Add Docker containerization

Add unit testing suite
