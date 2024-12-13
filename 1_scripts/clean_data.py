import pandas as pd

print("Starting data cleaning process...")

# Load raw data
raw_data = pd.read_csv("2_data/raw_data.csv")
print(f"Raw data loaded. Total rows: {raw_data.shape[0]}")

# Ensure symbols are balanced
required_symbols = ['AAPL', 'AMZN', 'MSFT']
balanced_data = raw_data[raw_data['symbol'].isin(required_symbols)]
print(f"Filtered data for required symbols. Rows after filtering: {balanced_data.shape[0]}")

# Convert timestamp to datetime
balanced_data['timestamp'] = pd.to_datetime(balanced_data['timestamp'])
print("Timestamp converted to datetime format.")

# Sort data by timestamp for each symbol
balanced_data = balanced_data.sort_values(by=['symbol', 'timestamp'])
print("Data sorted by 'symbol' and 'timestamp'.")

# Save cleaned data
balanced_data.to_csv("2_data/cleaned_mqtt_data.csv", index=False)
print("Cleaned data saved to '2_data/cleaned_mqtt_data.csv'.")