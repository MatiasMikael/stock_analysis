import pandas as pd
import random
from datetime import datetime, timedelta

# Generate synthetic stock data
def generate_synthetic_data(symbols, start_date, days, rows_per_day):
    print("Starting synthetic data generation...")
    data = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    print(f"Initial date set to {current_date}")
    
    for day in range(days):
        print(f"Generating data for day {day + 1}/{days}...")
        for row in range(rows_per_day):
            symbol = random.choice(symbols)
            open_price = random.uniform(200, 500)
            high_price = open_price + random.uniform(1, 10)
            low_price = open_price - random.uniform(1, 10)
            close_price = random.uniform(low_price, high_price)
            volume = random.randint(1000000, 100000000)
            data.append({
                "symbol": symbol,
                "timestamp": current_date.isoformat(),
                "open": round(open_price, 2),
                "high": round(high_price, 2),
                "low": round(low_price, 2),
                "close": round(close_price, 2),
                "volume": volume
            })
        current_date += timedelta(days=1)
        print(f"Completed data for date: {current_date - timedelta(days=1)}")
    
    print("Synthetic data generation completed.")
    return pd.DataFrame(data)

# Configuration
print("Setting configuration...")
symbols = ["AAPL", "MSFT", "AMZN"]
start_date = "2024-12-01"
days = 30  # Number of days of data
rows_per_day = 10  # Number of rows per day
print(f"Symbols: {symbols}, Start Date: {start_date}, Days: {days}, Rows per Day: {rows_per_day}")

# Generate data
print("Calling generate_synthetic_data function...")
synthetic_data = generate_synthetic_data(symbols, start_date, days, rows_per_day)

# Save to CSV
print("Saving data to CSV...")
synthetic_data.to_csv('2_data/raw_data.csv', index=False)
print("Synthetic data generated and saved to 2_data/raw_data.csv")