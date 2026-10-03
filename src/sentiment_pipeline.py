import yfinance as yf
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 1. Fetch Stock Historical Data
def fetch_stock_data(ticker="AAPL", period="1mo"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    df['Daily_Return'] = df['Close'].pct_change()
    return df

# 2. Financial Sentiment Analysis using VADER
def analyze_sentiment(text_list):
    analyzer = SentimentIntensityAnalyzer()
    results = []
    
    for text in text_list:
        score = analyzer.polarity_scores(text)['compound']
        if score >= 0.05:
            sentiment = "positive"
        elif score <= -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        results.append(sentiment)
        
    return results

if __name__ == "__main__":
    print("--- 1. Fetching Stock Data for AAPL ---")
    stock_df = fetch_stock_data("AAPL")
    print(stock_df[['Close', 'Daily_Return']].tail())
    
    print("\n--- 2. Analyzing Financial News Sentiment ---")
    sample_news = [
        "Apple reports record quarterly revenue driven by strong iPhone sales.",
        "Supply chain disruptions may delay upcoming hardware releases.",
        "Markets remain flat ahead of upcoming Federal Reserve interest rate decision."
    ]
    
    sentiments = analyze_sentiment(sample_news)
    for news, sentiment in zip(sample_news, sentiments):
        print(f"[{sentiment.upper()}] - {news}")