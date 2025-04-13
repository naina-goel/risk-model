"""
test_real_data_pipeline.py

This script runs a full pipeline test using real historical market data.
It augments the data with synthetic sentiment signals and policy shocks, 
applies the risk scoring model, and generates a visualization.

Key Steps:
1. Load real market price data from 'data/real_market_data.csv'
2. Add:
   - Simulated Sentiment Scores (noisy sine wave)
   - Random binary Policy Shock events
3. Run the risk scoring model
4. Save and display a 3-panel plot showing:
   - 📈 Market Price trend
   - 💬 Sentiment with shocks
   - 🧠 Computed Risk Score

This script is used for:
- Manual sanity checks of the full pipeline
- Visual inspection of risk dynamics over time
- Generating output for presentations or reports
"""

# -------------------------------
# Import Required Libraries
# -------------------------------
from core.risk_model import compute_risk_score
from core.visualizer import plot_all
import pandas as pd
import numpy as np
import os

# Step 1: Load real market data
df = pd.read_csv("data/real_market_data.csv")
df['Market_Price'] = pd.to_numeric(df['Market_Price'], errors='coerce')
df.dropna(subset=['Market_Price'], inplace=True)

# Step 2: Add synthetic sentiment + policy shock signals
df['Sentiment_Score'] = np.clip(
    np.sin(np.linspace(0, 3 * np.pi, len(df))) + np.random.normal(0, 0.2, len(df)),
    -1, 1
)
df['Policy_Shock'] = 0
df.loc[df.sample(frac=0.05, random_state=42).index, 'Policy_Shock'] = 1

# Step 3: Run risk model
df = compute_risk_score(df)

# Step 4: Save + visualize
output_path = "outputs/real_risk_model_output.png"
plot_all(df, save_path=output_path)
