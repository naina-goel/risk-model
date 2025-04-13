"""
risk_model.py

This module defines the core algorithm used to compute a dynamic risk score based on multiple real-world inspired indicators:
- Market price fluctuations
- Societal sentiment volatility
- Sudden policy shock events

It is a central component of the QuontX-inspired simulation system, translating quantitative signals into a composite Risk_Score that reflects systemic uncertainty.

The resulting `Risk_Score` column can be used for:
- Scenario modeling
- Stress testing
- Decision-support analytics

Inputs:
    DataFrame with at least the following columns:
    - Market_Price
    - Sentiment_Score
    - Policy_Shock

Output:
    DataFrame with additional columns:
    - Market_Change
    - Sentiment_Volatility
    - Risk_Score
"""

# -------------------------------
# Import Required Libraries
# -------------------------------
import numpy as np

def compute_risk_score(df):
    """
    Computes a dynamic risk score based on:
    - Market price changes
    - Sentiment volatility
    - Policy shocks

    Args:
        df (DataFrame): Must contain Market_Price, Sentiment_Score, Policy_Shock columns

    Returns:
        DataFrame with added columns:
        - Market_Change
        - Sentiment_Volatility
        - Risk_Score
    """
    df['Market_Change'] = np.abs(np.gradient(df['Market_Price']))
    df['Sentiment_Volatility'] = np.abs(np.gradient(df['Sentiment_Score']))

    df['Risk_Score'] = (
        0.4 * df['Sentiment_Volatility'] +
        0.4 * df['Market_Change'] +
        0.2 * df['Policy_Shock']
    )

    return df
