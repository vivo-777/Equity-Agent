import yfinance as yf
import pandas as pd
from typing import Dict, Any

def format_market_cap(val) -> str:
    """Helper to make huge numbers readable (e.g., 2.5T, 45B)"""
    if val is None or val == "N/A":
        return "N/A"
        
    try:
        # Convert to float if it's a string number
        val = float(val)
    except (ValueError, TypeError):
        return str(val)
        
    if val >= 1e12:
        return f"${val/1e12:.2f}T"
    elif val >= 1e9:
        return f"${val/1e9:.2f}B"
    elif val >= 1e6:
        return f"${val/1e6:.2f}M"
    else:
        return f"${val:,.0f}"

def fetch_market_data(ticker: str) -> Dict[str, Any]:
    """
    Fetch comprehensive market data for a given stock ticker.
    Returns a dictionary with summary metrics AND the raw history dataframe.
    """
    try:

        ticker = ticker.upper().strip()
        stock = yf.Ticker(ticker)

        try:
            info = stock.info
        except:
            info = {}

        hist = stock.history(period="6mo")
        
        if hist.empty:
            return {"error": f"No price data available for ticker: {ticker}"}

        current_price = hist['Close'].iloc[-1]

        if len(hist) >= 30:
            volatility = hist['Close'].pct_change().rolling(window=30).std().iloc[-1] * 100
        else:
            volatility = 0.0

        market_data = {
            "ticker": ticker,
            "current_price": round(current_price, 2),
            "volatility_30d": round(volatility, 2) if pd.notnull(volatility) else "N/A",

            "market_cap": format_market_cap(info.get('marketCap')),
            
            "pe_ratio": round(info.get('trailingPE', 0), 2) if info.get('trailingPE') else 'N/A',
            "forward_pe": round(info.get('forwardPE', 0), 2) if info.get('forwardPE') else 'N/A',
            
            "revenue_growth": f"{round(info.get('revenueGrowth', 0) * 100, 2)}%" if info.get('revenueGrowth') else 'N/A',
            "profit_margins": f"{round(info.get('profitMargins', 0) * 100, 2)}%" if info.get('profitMargins') else 'N/A',
            "debt_to_equity": round(info.get('debtToEquity', 0), 2) if info.get('debtToEquity') else 'N/A',
            
            "free_cash_flow": format_market_cap(info.get('freeCashflow')),
            "return_on_equity": f"{round(info.get('returnOnEquity', 0) * 100, 2)}%" if info.get('returnOnEquity') else 'N/A',
            
            "history_df": hist 
        }
        
        return market_data

    except Exception as e:
        return {"error": f"Market data fetch failed: {str(e)}"}
