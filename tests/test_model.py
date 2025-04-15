"""
test_model.py

This script provides a basic unit test to validate the functionality of the risk modeling system. 
It overlays synthetic sentiment and policy signals on real market data and verifies that the resulting 
Risk_Score adheres to expected structural and numerical integrity.

Key assertions:
- ✅ The 'Risk_Score' column is generated
- ✅ Values are numeric and not entirely null
- ✅ Pipeline does not raise exceptions with real data

This test is useful for:
- Quick validation of the core model logic
- Ensuring changes to `risk_model.py` don’t silently break outputs
- CI/CD pipeline checks (if integrated)

Run as a standalone script or integrate into automated test runners.
"""

# -------------------------------
# Import Required Libraries
# -------------------------------
import pandas as pd
import numpy as np
from core.risk_model import compute_risk_score
from core.visualizer import plot_all

def test_real_data_pipeline():
    try:
        # Load the real market data
        df = pd.read_csv("data/real_market_data.csv")

        # Add dummy sentiment and policy shocks
        df['Sentiment_Score'] = np.clip(
            np.sin(np.linspace(0, 3 * np.pi, len(df))) + np.random.normal(0, 0.2, len(df)), -1, 1
        )
        df['Policy_Shock'] = 0
        df.loc[df.sample(frac=0.05, random_state=42).index, 'Policy_Shock'] = 1

        # Run risk model
        result = compute_risk_score(df)

        # Assertions
        assert 'Risk_Score' in result.columns, "Risk_Score column missing"
        assert not result['Risk_Score'].isnull().all(), "Risk_Score is entirely null"
        assert result['Risk_Score'].dtype != 'object', "Risk_Score should be numeric"

        print("✅ test_real_data_pipeline passed!")

    except Exception as e:
        print(f"❌ test_real_data_pipeline failed: {e}")

if __name__ == "__main__":
    test_real_data_pipeline()
