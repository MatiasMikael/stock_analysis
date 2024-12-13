# stock_analysis

## Description
Analyze synthetic stock data for AAPL, AMZN, MSFT:
- Data cleaning and processing.
- Generating synthetic stock data.
- Visualizing stock trends and volume distributions.

## Directory Structure
1_scripts/
- clean_data.py: Cleans raw data and ensures consistency.
- load_data.py: Generates synthetic stock data for analysis.
- visualize_data.py: Produces visual insights into data.

2_data/
- raw_data.csv: Synthetic data containing stock prices and volume.
- cleaned_mqtt_data.csv: Data processed for analysis.

3_results/
* stock_prices_over_time.png: Line plot showing stock prices over time for each symbol.
* X-axis: Time; Y-axis: Closing price (€); Line: Symbol-specific trends.
* volume_distribution.png: Histogram showing volume distribution per symbol.
* X-axis: Volume (x10⁶); Y-axis: Frequency; KDE overlay highlights density.

## How to Run
Generate synthetic data:
- `python 1_scripts/load_data.py`
  
Clean the data:
- `python 1_scripts/clean_data.py`

Generate visualizations:
- `python 1_scripts/visualize_data.py`

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this project in compliance with the terms of the MIT License.
