import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned data
print("Loading data from cleaned_mqtt_data.csv...")
data = pd.read_csv("2_data/cleaned_mqtt_data.csv")
data['timestamp'] = pd.to_datetime(data['timestamp'])  # Convert timestamp to datetime
print("Data loaded successfully.")

# Stock Prices Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='timestamp', y='close', hue='symbol', linewidth=2)
plt.title('Stock Prices Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Close Price (€)')
plt.xticks(rotation=45)
plt.legend(title='Symbol')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('3_results/stock_prices_over_time.png')
plt.show()

# Volume Distribution per Symbol
plt.figure(figsize=(12, 6))
sns.histplot(data=data, x='volume', hue='symbol', kde=True, multiple='stack', bins=20)
plt.title('Volume Distribution per Symbol')
plt.xlabel('Volume (x10⁶)')
plt.ylabel('Frequency')
plt.legend(title='Symbol')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('3_results/volume_distribution.png')
plt.show()

print("Plots generated and saved to 3_results folder.")