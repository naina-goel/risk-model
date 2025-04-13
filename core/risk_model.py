import numpy as np

def compute_risk_score(df):
    """
    Computes a dynamic risk score based on:
    - Market price changes
    - Sentiment volatility
    - Policy shocks
    """
    df['Market_Change'] = np.abs(np.gradient(df['Market_Price']))
    df['Sentiment_Volatility'] = np.abs(np.gradient(df['Sentiment_Score']))

    df['Risk_Score'] = (
        0.4 * df['Sentiment_Volatility'] +
        0.4 * df['Market_Change'] +
        0.2 * df['Policy_Shock']
    )

    return df