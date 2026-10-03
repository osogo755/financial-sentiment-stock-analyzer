# Automated Financial News Sentiment & Stock Movement Analyzer

An automated data pipeline that correlates real-time financial news sentiment with stock price movements using FinBERT/NLP models and time-series analysis.

## Business Problem
Investment analysts waste hours reading financial reports and market news to gauge market sentiment. An automated pipeline that correlates real-time news sentiment with stock price movements allows analysts to detect trends faster.

## Technical Stack
* **Language & Libraries:** Python (`pandas`, `yfinance`, `transformers`, `torch`)
* **NLP Model:** `ProsusAI/finbert` (Hugging Face)
* **Data Sources:** Yahoo Finance API & News Feeds
* **Visualization:** Matplotlib / Plotly

## Project Architecture & Workflow
1. **Data Ingestion:** Fetch stock historical prices and market news using `yfinance`.
2. **Sentiment Analysis:** Classify news headlines into Positive, Negative, or Neutral sentiment using `FinBERT`.
3. **Correlation Analysis:** Compare daily average sentiment scores against stock returns to identify market signals.

## Project Structure
```text
financial-sentiment-analyzer/
├── README.md
├── requirements.txt
└── src/
    └── sentiment_pipeline.py