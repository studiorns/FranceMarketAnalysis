#!/usr/bin/env python3
"""
Simplified Enhanced France Travel Queries Forecast Model

This script implements a simplified version of the enhanced forecast model with:
1. Anomaly Detection: Identifies and adjusts outliers in historical data
2. Time Series Forecasting: Implements ARIMA models for comparison
3. Bayesian Forecasting: Incorporates uncertainty and confidence intervals

Usage:
    python france_forecast_enhanced_simple.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Historical data (manually extracted from Travel_Queries_Forecast_France_Updated.csv)
historical_data = [
    {'Month': 'January', 'Year': 2020, 'Indexed_Queries': 9.587367178},
    {'Month': 'January', 'Year': 2021, 'Indexed_Queries': 8.217237308},
    {'Month': 'January', 'Year': 2022, 'Indexed_Queries': 15.31227863},
    {'Month': 'January', 'Year': 2023, 'Indexed_Queries': 21.03837072},
    {'Month': 'January', 'Year': 2024, 'Indexed_Queries': 31.24675325},
    {'Month': 'February', 'Year': 2020, 'Indexed_Queries': 17.37190083},
    {'Month': 'February', 'Year': 2021, 'Indexed_Queries': 4.653482881},
    {'Month': 'February', 'Year': 2022, 'Indexed_Queries': 16.69893743},
    {'Month': 'February', 'Year': 2023, 'Indexed_Queries': 18.80991736},
    {'Month': 'February', 'Year': 2024, 'Indexed_Queries': 28.17768595},
    {'Month': 'March', 'Year': 2020, 'Indexed_Queries': 9.129279811},
    {'Month': 'March', 'Year': 2021, 'Indexed_Queries': 6.165289256},
    {'Month': 'March', 'Year': 2022, 'Indexed_Queries': 14.35360094},
    {'Month': 'March', 'Year': 2023, 'Indexed_Queries': 18.54604486},
    {'Month': 'March', 'Year': 2024, 'Indexed_Queries': 24.07201889},
    {'Month': 'April', 'Year': 2020, 'Indexed_Queries': 4.177095632},
    {'Month': 'April', 'Year': 2021, 'Indexed_Queries': 5.43270366},
    {'Month': 'April', 'Year': 2022, 'Indexed_Queries': 12.55548996},
    {'Month': 'April', 'Year': 2023, 'Indexed_Queries': 16.73140496},
    {'Month': 'April', 'Year': 2024, 'Indexed_Queries': 18.64167651},
    {'Month': 'May', 'Year': 2020, 'Indexed_Queries': 4.106847698},
    {'Month': 'May', 'Year': 2021, 'Indexed_Queries': 5.436835891},
    {'Month': 'May', 'Year': 2022, 'Indexed_Queries': 10.71487603},
    {'Month': 'May', 'Year': 2023, 'Indexed_Queries': 15.13164109},
    {'Month': 'May', 'Year': 2024, 'Indexed_Queries': 18.64167651},
    {'Month': 'June', 'Year': 2020, 'Indexed_Queries': 4.435655254},
    {'Month': 'June', 'Year': 2021, 'Indexed_Queries': 4.884297521},
    {'Month': 'June', 'Year': 2022, 'Indexed_Queries': 11.54191263},
    {'Month': 'June', 'Year': 2023, 'Indexed_Queries': 12.85182999},
    {'Month': 'June', 'Year': 2024, 'Indexed_Queries': 15.55785124},
    {'Month': 'July', 'Year': 2020, 'Indexed_Queries': 4.631641086},
    {'Month': 'July', 'Year': 2021, 'Indexed_Queries': 17.31818182},
    {'Month': 'July', 'Year': 2022, 'Indexed_Queries': 10.93506494},
    {'Month': 'July', 'Year': 2023, 'Indexed_Queries': 17.31818182},
    {'Month': 'July', 'Year': 2024, 'Indexed_Queries': 17.70602125},
    {'Month': 'August', 'Year': 2020, 'Indexed_Queries': 5.471664699},
    {'Month': 'August', 'Year': 2021, 'Indexed_Queries': 6.646399055},
    {'Month': 'August', 'Year': 2022, 'Indexed_Queries': 13.94805195},
    {'Month': 'August', 'Year': 2023, 'Indexed_Queries': 19.36363636},
    {'Month': 'August', 'Year': 2024, 'Indexed_Queries': 18.79397875},
    {'Month': 'September', 'Year': 2020, 'Indexed_Queries': 4.347697757},
    {'Month': 'September', 'Year': 2021, 'Indexed_Queries': 8.89433294},
    {'Month': 'September', 'Year': 2022, 'Indexed_Queries': 13.73081464},
    {'Month': 'September', 'Year': 2023, 'Indexed_Queries': 20.50826446},
    {'Month': 'September', 'Year': 2024, 'Indexed_Queries': 20.33471074},
    {'Month': 'October', 'Year': 2020, 'Indexed_Queries': 4.33175915},
    {'Month': 'October', 'Year': 2021, 'Indexed_Queries': 13.88193625},
    {'Month': 'October', 'Year': 2022, 'Indexed_Queries': 16.93978749},
    {'Month': 'October', 'Year': 2023, 'Indexed_Queries': 22.22904368},
    {'Month': 'October', 'Year': 2024, 'Indexed_Queries': 23.7420307},
    {'Month': 'November', 'Year': 2020, 'Indexed_Queries': 5.811688312},
    {'Month': 'November', 'Year': 2021, 'Indexed_Queries': 14.73140496},
    {'Month': 'November', 'Year': 2022, 'Indexed_Queries': 18.51062574},
    {'Month': 'November', 'Year': 2023, 'Indexed_Queries': 24.53837072},
    {'Month': 'November', 'Year': 2024, 'Indexed_Queries': 22.64167651},
    {'Month': 'December', 'Year': 2020, 'Indexed_Queries': 5.811688312},
    {'Month': 'December', 'Year': 2021, 'Indexed_Queries': 16.94746163},
    {'Month': 'December', 'Year': 2022, 'Indexed_Queries': 17.05903188},
    {'Month': 'December', 'Year': 2023, 'Indexed_Queries': 24.86835891},
    {'Month': 'December', 'Year': 2024, 'Indexed_Queries': 23.33707202}
]

# Factor-based forecast results (manually extracted from Travel_Queries_Forecast_France_Updated.csv)
factor_forecast = [
    {'Month': 'January', '2024_Queries': 31.25, 'Conservative': 38.01, 'Moderate': 45.12, 'Ambitious': 53.16},
    {'Month': 'February', '2024_Queries': 28.18, 'Conservative': 31.41, 'Moderate': 36.96, 'Ambitious': 43.56},
    {'Month': 'March', '2024_Queries': 24.07, 'Conservative': 26.78, 'Moderate': 31.42, 'Ambitious': 37.19},
    {'Month': 'April', '2024_Queries': 18.64, 'Conservative': 19.20, 'Moderate': 21.73, 'Ambitious': 24.31},
    {'Month': 'May', '2024_Queries': 18.64, 'Conservative': 18.95, 'Moderate': 21.45, 'Ambitious': 24.02},
    {'Month': 'June', '2024_Queries': 15.56, 'Conservative': 15.14, 'Moderate': 16.83, 'Ambitious': 18.75},
    {'Month': 'July', '2024_Queries': 17.71, 'Conservative': 17.79, 'Moderate': 19.93, 'Ambitious': 22.39},
    {'Month': 'August', '2024_Queries': 18.79, 'Conservative': 18.48, 'Moderate': 20.71, 'Ambitious': 23.29},
    {'Month': 'September', '2024_Queries': 20.33, 'Conservative': 18.36, 'Moderate': 19.98, 'Ambitious': 21.76},
    {'Month': 'October', '2024_Queries': 23.74, 'Conservative': 22.17, 'Moderate': 23.51, 'Ambitious': 24.85},
    {'Month': 'November', '2024_Queries': 22.64, 'Conservative': 20.05, 'Moderate': 21.45, 'Ambitious': 22.85},
    {'Month': 'December', '2024_Queries': 23.34, 'Conservative': 22.47, 'Moderate': 24.85, 'Ambitious': 27.27}
]

def main():
    """Main function to run the enhanced forecast model."""
    print("Starting enhanced forecast model for France...")
    
    # Convert historical data to DataFrame
    df = pd.DataFrame(historical_data)
    
    # Create a date column
    df['Date'] = pd.to_datetime(
        df['Year'].astype(str) + '-' + 
        df['Month'].apply(lambda x: {
            'January': '01', 'February': '02', 'March': '03', 'April': '04',
            'May': '05', 'June': '06', 'July': '07', 'August': '08',
            'September': '09', 'October': '10', 'November': '11', 'December': '12'
        }[x]) + '-01'
    )
    
    # Sort by date
    df = df.sort_values('Date')
    
    # Create a time series
    time_series = df.set_index('Date')['Indexed_Queries']
    
    # Detect outliers
    print("Detecting outliers...")
    z_scores = stats.zscore(df['Indexed_Queries'])
    df['Outlier'] = abs(z_scores) > 3.0
    df['Z_Score'] = z_scores
    outliers = df[df['Outlier']]
    
    # Adjust outliers
    print("Adjusting outliers...")
    adjusted_series = time_series.copy()
    for idx in outliers.index:
        date_idx = outliers.loc[idx, 'Date']
        # Use median of surrounding values
        window_start = max(0, time_series.index.get_loc(date_idx) - 1)
        window_end = min(len(time_series), time_series.index.get_loc(date_idx) + 2)
        window_values = time_series.iloc[window_start:window_end]
        # Exclude the outlier itself from the window
        window_values = window_values[window_values.index != date_idx]
        if not window_values.empty:
            adjusted_series.loc[date_idx] = window_values.median()
    
    # Plot outliers
    print("Plotting outliers...")
    plt.figure(figsize=(12, 6))
    plt.plot(time_series.index, time_series.values, 'b-', label='Original Data')
    plt.scatter(outliers['Date'], outliers['Indexed_Queries'], color='red', label='Outliers')
    plt.plot(adjusted_series.index, adjusted_series.values, 'g--', label='Adjusted Data')
    plt.title('France Travel Queries Time Series with Outliers')
    plt.xlabel('Date')
    plt.ylabel('Indexed Queries')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('france_outliers_detection.png')
    plt.close()
    
    # Fit ARIMA model
    print("Fitting ARIMA model...")
    model = ARIMA(adjusted_series, order=(1, 1, 1))
    arima_model = model.fit()
    
    # Generate forecast
    print("Generating ARIMA forecast...")
    steps = 12
    forecast = arima_model.forecast(steps=steps)
    forecast_index = pd.date_range(start=time_series.index[-1], periods=steps+1, freq='MS')[1:]
    
    # Get confidence intervals
    pred_ci = arima_model.get_forecast(steps=steps).conf_int()
    
    # Create forecast DataFrame
    arima_forecast = pd.DataFrame({
        'ARIMA_Forecast': forecast,
        'Lower_CI': pred_ci.iloc[:, 0],
        'Upper_CI': pred_ci.iloc[:, 1]
    }, index=forecast_index)
    
    # Convert factor forecast to DataFrame
    factor_df = pd.DataFrame(factor_forecast)
    
    # Create a date column for 2025
    factor_df['Date'] = pd.to_datetime(
        '2025-' + 
        factor_df['Month'].apply(lambda x: {
            'January': '01', 'February': '02', 'March': '03', 'April': '04',
            'May': '05', 'June': '06', 'July': '07', 'August': '08',
            'September': '09', 'October': '10', 'November': '11', 'December': '12'
        }[x]) + '-01'
    )
    
    # Set the date as index
    factor_df = factor_df.set_index('Date')
    
    # Combine with statistical forecasts
    comparison = pd.DataFrame(index=factor_df.index)
    comparison['Factor_Conservative'] = factor_df['Conservative']
    comparison['Factor_Moderate'] = factor_df['Moderate']
    comparison['Factor_Ambitious'] = factor_df['Ambitious']
    comparison['ARIMA_Forecast'] = arima_forecast['ARIMA_Forecast']
    comparison['ARIMA_Lower_CI'] = arima_forecast['Lower_CI']
    comparison['ARIMA_Upper_CI'] = arima_forecast['Upper_CI']
    
    # Calculate YoY change for ARIMA forecast
    arima_yoy = []
    for month, row in comparison.iterrows():
        month_name = month.strftime('%B')
        month_2024 = factor_forecast[next((i for i, item in enumerate(factor_forecast) if item['Month'] == month_name), 0)]['2024_Queries']
        arima_yoy.append(((row['ARIMA_Forecast'] - month_2024) / month_2024) * 100)
    
    comparison['ARIMA_YoY'] = arima_yoy
    
    # Plot forecasts
    print("Plotting forecasts...")
    plt.figure(figsize=(12, 6))
    
    # Plot historical data
    plt.plot(time_series.index, time_series.values, 'b-', label='Historical Data')
    
    # Plot factor-based forecasts
    plt.plot(comparison.index, comparison['Factor_Conservative'], 'g--', label='Factor Conservative')
    plt.plot(comparison.index, comparison['Factor_Moderate'], 'g-', label='Factor Moderate')
    plt.plot(comparison.index, comparison['Factor_Ambitious'], 'g:', label='Factor Ambitious')
    
    # Plot ARIMA forecast
    plt.plot(comparison.index, comparison['ARIMA_Forecast'], 'r-', label='ARIMA Forecast')
    plt.fill_between(
        comparison.index,
        comparison['ARIMA_Lower_CI'],
        comparison['ARIMA_Upper_CI'],
        color='r', alpha=0.1, label='ARIMA 95% CI'
    )
    
    plt.title('France Travel Queries Forecast Comparison')
    plt.xlabel('Date')
    plt.ylabel('Indexed Queries')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('france_forecast_comparison.png')
    plt.close()
    
    # Save results
    print("Saving results...")
    comparison.to_csv('france_forecast_comparison.csv')
    arima_forecast.to_csv('france_arima_forecast.csv')
    
    # Print summary
    print("\nARIMA Forecast Summary:")
    print(f"Average 2025 Forecast: {comparison['ARIMA_Forecast'].mean():.2f}")
    print(f"Average YoY Growth: {comparison['ARIMA_YoY'].mean():.2f}%")
    print(f"Confidence Interval Width (Jan): {comparison['ARIMA_Upper_CI'].iloc[0] - comparison['ARIMA_Lower_CI'].iloc[0]:.2f}")
    print(f"Confidence Interval Width (Dec): {comparison['ARIMA_Upper_CI'].iloc[-1] - comparison['ARIMA_Lower_CI'].iloc[-1]:.2f}")
    
    print("\nDone!")
    
    return comparison, arima_forecast

if __name__ == "__main__":
    comparison, arima_forecast = main()
