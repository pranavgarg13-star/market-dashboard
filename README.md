# 📊 AI Market Intelligence Dashboard

A real-time financial analytics dashboard that collects cryptocurrency and stock market data, performs analysis, and predicts Bitcoin price trends using machine learning.

The system automatically fetches market data, stores it in a dataset, generates charts, and displays insights in a live dashboard.

---

## 🚀 Features

• Real-time crypto and stock market tracking  
• Automated data collection using a scheduler  
• Interactive financial charts  
• AI-powered Bitcoin price prediction  
• Live dashboard with market indicators  
• Percentage movement detection  
• Professional dark-themed UI

---

## 🧠 Technologies Used

Python  
Flask  
Pandas  
Plotly  
Scikit-learn  
YFinance API  
Scheduler Automation

---

## 🏗 System Architecture

Market APIs  
↓  
Data Fetcher  
↓  
Dataset Storage (CSV)  
↓  
Data Analysis (Pandas)  
↓  
AI Prediction Model  
↓  
Visualization (Plotly Charts)  
↓  
Flask Dashboard  
↓  
Web Browser

---

## 📂 Project Structure

```
market_dashboard
│
├── app.py
├── scheduler.py
├── requirements.txt
│
├── data
│   └── market_data.csv
│
├── modules
│   ├── data_fetcher.py
│   ├── analysis.py
│   └── prediction.py
│
├── templates
│   └── dashboard.html
│
└── static
    ├── crypto_chart.html
    └── stock_chart.html
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/market-dashboard.git
cd market-dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

Start the data collection scheduler:

```bash
python scheduler.py
```

Run the dashboard:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📈 AI Prediction

The system uses a **Linear Regression model** to predict the next Bitcoin price based on historical market data.

Model workflow:

1. Load dataset
2. Create feature index
3. Train regression model
4. Predict next market value
5. Display trend direction

Example output:

```
Current BTC: 73420
Predicted BTC: 73590
Trend: UP
```

---

## 🔄 Automation

A scheduler automatically collects market data every **2 minutes**.

```
schedule.every(2).minutes.do(update_market_data)
```

This keeps the dataset and dashboard updated in real time.

---

## 📊 Dashboard Preview

The dashboard displays:

• Live market price cards  
• Percentage movement indicators  
• AI market prediction  
• Crypto price charts  
• Stock price charts  

---

## 📌 Future Improvements

• Multi-crypto AI prediction  
• Buy / Sell signal generation  
• Volatility detection  
• Portfolio tracking  
• Deployment on cloud server

---

## 👨‍💻 Author

Pranav Garg

---

## 📜 License

This project is for educational and learning purposes.
