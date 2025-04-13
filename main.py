# main.py

from core.data_generator import generate_data
from core.data_loader import get_real_market_data
from core.risk_model import compute_risk_score
from core.visualizer import plot_all

# Step 1: Generate simulated data
df = generate_data()

# Step 2: Compute risk score
df = compute_risk_score(df)

# Step 3: Visualize results and save file
import os
output_path = "outputs/real_risk_model_output.png"
plot_all(df, save_path=output_path)
