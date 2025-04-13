"""
test_real_data_pipeline.py

Test case: Run the risk model on real_market_data.csv
Generates real_risk_model_output.png
"""

from core.risk_model import compute_risk_score
from core.visualizer import plot_all
import pandas as pd
import os

# Step 1: Load real market data
df = pd.read_csv("data/real_market_data.csv")
df['Market_Price'] = pd.to_numeric(df['Market_Price'], errors='coerce')
df.dropna(subset=['Market_Price'], inplace=True)

# Step 2: Add placeholder sentiment + policy shock columns
# For now, use a sine wave as pseudo-sentiment and some random shock events
import numpy as np

df['Sentiment_Score'] = np.clip(np.sin(np.linspace(0, 3 * np.pi, len(df))) + np.random.normal(0, 0.2, len(df)), -1, 1)
df['Policy_Shock'] = 0
df.loc[df.sample(frac=0.05, random_state=42).index, 'Policy_Shock'] = 1  # Random 5% shock events

# Step 3: Run risk model
df = compute_risk_score(df)

# Step 4: Save + visualize
output_path = "outputs/real_risk_model_output.png"
plot_all(df, save_path=output_path)