"""
data_generator.py

This module simulates synthetic time-series data to emulate the dynamics of financial markets,
societal sentiment, and policy interventions. It is used for testing and benchmarking the
risk modeling pipeline inspired by the vision of modeling real-world complexity.

Generated features include:
- Simulated market prices (random walk)
- Sentiment scores (noisy sine wave)
- Binary policy shock events (randomly injected)

Used as a source for synthetic inputs to evaluate and visualize the risk scoring system.
"""

# -------------------------------
# Import Required Libraries
# -------------------------------
import numpy as np
import pandas as pd
import random

def generate_data(num_days=100, seed=42):
    """
    Simulates financial and societal data over a given number of days.
    
    Returns:
        DataFrame with columns:
        - Date
        - Market_Price
        - Sentiment_Score
        - Policy_Shock
    """
    np.random.seed(seed)
    random.seed(seed)

    # Create date range
    dates = pd.date_range(start="2024-01-01", periods=num_days)

    # Simulated market prices using random walk
    market_price = np.cumsum(np.random.normal(0, 1, num_days)) + 100

    # Simulated sentiment score using noisy sine wave
    sentiment_score = np.clip(
        np.sin(np.linspace(0, 3 * np.pi, num_days)) + np.random.normal(0, 0.2, num_days),
        -1, 1
    )

    # Random policy shocks (binary events)
    policy_shock = np.zeros(num_days)
    shock_days = random.sample(range(20, num_days - 10), 3)
    for day in shock_days:
        policy_shock[day] = 1

    # Combine into DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Market_Price': market_price,
        'Sentiment_Score': sentiment_score,
        'Policy_Shock': policy_shock
    })

    return df
