# 🏭 SalesSense AI — JSW Steel Dashboard

A Real-Time Sales Dashboard with AI-powered insights built with Python, Streamlit, Pandas, and Plotly. Inspired by JSW Steel's Indian steel business context.

## 📌 Project Status
🔨 Almost Done — Deploying Soon!

## 🛠️ Tech Stack
- Python 3.14
- Streamlit — Dashboard UI
- Pandas — Data Processing
- Plotly — Interactive Charts
- Groq AI (LLaMA 3.3) — AI Insights & Chat
- Git & GitHub — Version Control

## ✅ Progress
- [x] Project setup & environment
- [x] JSW Steel style dataset generated (2000 rows)
- [x] KPI Cards (Sales, Profit, Orders, Volume in ₹ Crores)
- [x] Interactive Charts (Bar, Pie, Line, Horizontal Bar)
- [x] Sidebar Filters (Region, Category)
- [x] AI Insights (Auto-generated business insights)
- [ ] Ask Your Data (Chat feature)
- [ ] Deployed Live on Streamlit Cloud

## 📁 Project Structure
SalesSense-AI/
├── app.py                  # Main application
├── generate_data.py        # JSW Steel data generator
├── sales_data.csv          # Generated dataset (not pushed to GitHub)
├── .env                    # API keys (not pushed to GitHub)
├── .gitignore              # Git ignore rules
└── README.md               # This file

## 🚀 How to Run Locally
1. Clone the repo
2. Install dependencies: `pip install streamlit pandas plotly groq python-dotenv`
3. Add your Groq API key in `.env` file as `GROQ_API_KEY=your_key`
4. Generate data: `python generate_data.py`
5. Run the app: `streamlit run app.py`

## 👨‍💻 Built By
Balaji — AIML Engineer Intern
Building real world AI projects to transition into a corporate AIML role.