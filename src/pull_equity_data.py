import yfinance as yf
import pandas as pd
from pathlib import Path

TICKER = "AAPL"
START_DATE = "2015-01-01"
END_DATE = None  # None = today

RAW_DATA_DIR = Path("data/raw")
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

#pull data
df = yf.download(
    TICKER,
    start=START_DATE,
    end=END_DATE,
    auto_adjust=False
)

output_path = RAW_DATA_DIR / f"{TICKER}_historical_raw.csv"
df.to_csv(output_path) #save raw

print(f"Raw data saved to {output_path}")
