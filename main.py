"""
main.py

A primary entry point for executing the societal-financial risk modeling pipeline. 
This script simulates input signals and orchestrates the full process of computing and 
visualizing dynamic risk scores based on market, sentiment, and policy interactions.

Workflow Overview:
1. 📊 Simulate financial and societal data (Market_Price, Sentiment_Score, Policy_Shock)
2. 🧠 Compute the dynamic Risk_Score using the modeling algorithm
3. 📈 Generate and save a 3-panel visualization:
    - Market Price over time
    - Sentiment Score with Policy Shocks
    - Calculated Risk Score

Output:
    A saved PNG plot in `outputs/real_risk_model_output.png`

To run:
    python main.py
"""

# -------------------------------
# Import Core Modules
# -------------------------------
from core.data_generator import generate_data
from core.data_loader import get_real_market_data
from core.risk_model import compute_risk_score
from core.visualizer import plot_all
import os

# Step 1: Generate simulated data
df = generate_data()

# Step 2: Compute risk score
df = compute_risk_score(df)

# Step 3: Visualize results and save file
output_path = "outputs/real_risk_model_output.png"
plot_all(df, save_path=output_path)
