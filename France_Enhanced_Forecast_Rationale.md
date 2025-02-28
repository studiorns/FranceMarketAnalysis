# France Enhanced Forecast Rationale

## Overview

This document explains the rationale behind the enhanced forecast model for France travel queries. The enhanced model incorporates statistical and machine learning approaches to complement the original factor-based model, providing additional insights and validation.

## Enhanced Model Approach

The enhanced model adds three key capabilities to the original factor-based approach:

1. **Anomaly Detection**: Identifies and adjusts outliers in historical data
2. **Time Series Forecasting**: Implements ARIMA models alongside the factor-based approach
3. **Bayesian Forecasting**: Incorporates uncertainty and confidence intervals in predictions

## Methodology

### Anomaly Detection

The model uses Z-scores to identify outliers in the historical data:
- Data points with Z-scores > 3.0 (more than 3 standard deviations from the mean) are flagged as outliers
- Outliers are adjusted using a median window approach, where each outlier is replaced with the median of surrounding values
- This preprocessing step improves forecast accuracy by removing anomalous data points that could skew the model

### ARIMA Model

The enhanced model implements an ARIMA (AutoRegressive Integrated Moving Average) model:
- ARIMA(1,1,1) parameters were selected based on the characteristics of the time series
- The model captures temporal patterns and autocorrelations in the data
- It provides a statistical baseline forecast that complements the factor-based approach

### Confidence Intervals

The ARIMA model provides 95% confidence intervals for the forecasts:
- These intervals quantify the uncertainty in the predictions
- Wider intervals indicate greater uncertainty
- The intervals widen as the forecast extends further into the future

## Key Findings

### Forecast Comparison

The ARIMA model forecasts an average of 23.20 indexed queries per month for 2025, which represents a 9.9% year-over-year growth from 2024. This is higher than the Conservative scenario (2.3% YoY growth) but lower than the Moderate (15.6% YoY growth) and Ambitious (30.6% YoY growth) scenarios.

The ARIMA forecast suggests a more stable pattern throughout the year, without the seasonal variations predicted by the factor-based model. This difference highlights the complementary nature of the two approaches:
- The factor-based model incorporates domain knowledge about seasonality and external factors
- The ARIMA model relies solely on historical patterns in the time series data

### Monthly Variations

The ARIMA model shows interesting deviations from the factor-based forecasts:
- For January through March, the ARIMA forecast is significantly lower than all factor-based scenarios
- For April through September, the ARIMA forecast is higher than the Conservative and sometimes the Moderate scenarios
- For October through December, the ARIMA forecast is close to the Conservative scenario

These differences suggest months where the factor-based model may be overestimating (January-March) or underestimating (April-September) growth based on historical patterns.

### Confidence Intervals

The 95% confidence intervals for the ARIMA forecasts provide valuable insights into forecast uncertainty:
- January 2025: 16.55 to 29.79 (range width: 13.23)
- December 2025: 4.83 to 41.56 (range width: 36.73)

The widening confidence intervals throughout the year reflect increasing uncertainty as the forecast extends further into the future. This information can be valuable for risk assessment and scenario planning.

## Implications for Strategy

The enhanced model provides several strategic implications:

1. **Validation of Moderate Scenario**: The ARIMA forecast (23.20) falls between the Conservative (22.40) and Moderate (25.33) scenarios, suggesting that a forecast between these two scenarios is most aligned with historical patterns.

2. **Risk Assessment**: The confidence intervals provide a quantitative measure of forecast uncertainty, which can inform risk management strategies.

3. **Seasonal Adjustments**: The difference between the ARIMA forecast and the factor-based forecasts highlights months where seasonal factors may have a stronger or weaker impact than historical patterns would suggest.

4. **Resource Allocation**: The ARIMA forecast suggests a more even distribution of resources throughout the year, while the factor-based forecasts suggest concentrating resources during peak months (January-March, December).

## Recommendations

Based on the enhanced model results, we recommend:

1. **Consider a forecast between the Conservative and Moderate scenarios** as the baseline for planning purposes, as this range is most aligned with the statistical ARIMA forecast.

2. **Consider the confidence intervals when making commitments** that depend on forecast accuracy. For high-stakes decisions, consider the lower bound of the confidence interval as a worst-case scenario.

3. **Allocate a portion of the budget as a contingency** to address the uncertainty quantified by the confidence intervals, particularly for the latter half of the year where uncertainty is greatest.

4. **Monitor actual performance against both forecasts** to continuously improve the models. If actual performance consistently falls outside the confidence intervals, reassess the models and their assumptions.

5. **Use the enhanced model alongside the factor-based model** rather than replacing it. The two approaches complement each other, with the factor-based model incorporating domain knowledge and the enhanced model providing statistical validation and uncertainty quantification.

## Conclusion

The enhanced forecast model provides valuable additional insights that complement the original factor-based approach. By incorporating anomaly detection, time series forecasting, and confidence intervals, the enhanced model offers a more robust and statistically sound forecast for France travel queries in 2025.

The combination of the factor-based and statistical approaches provides a more complete picture of potential outcomes, enabling more informed decision-making and resource allocation.
