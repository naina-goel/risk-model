# visualizer.py

import matplotlib.pyplot as plt

def plot_all(df, save_path='risk_model_output.png'):
    """
    Plots the full simulation: market price, sentiment score, and risk score.
    Also saves the output to an image file.
    """
    plt.figure(figsize=(14, 8))

    # Plot 1: Market Price
    plt.subplot(3, 1, 1)
    plt.plot(df['Date'], df['Market_Price'], label='Market Price', color='blue')
    plt.title('Market Price Over Time')
    plt.ylabel('Price')
    plt.grid(True)

    # Plot 2: Sentiment Score with Policy Shocks
    plt.subplot(3, 1, 2)
    plt.plot(df['Date'], df['Sentiment_Score'], label='Sentiment Score', color='green')
    plt.scatter(df['Date'][df['Policy_Shock'] == 1], df['Sentiment_Score'][df['Policy_Shock'] == 1],
                color='red', label='Policy Shock', zorder=5)
    plt.title('Sentiment Score with Policy Shocks')
    plt.ylabel('Sentiment')
    plt.legend()
    plt.grid(True)

    # Plot 3: Risk Score
    plt.subplot(3, 1, 3)
    plt.plot(df['Date'], df['Risk_Score'], label='Risk Score', color='purple')
    plt.title('Calculated Risk Score')
    plt.xlabel('Date')
    plt.ylabel('Risk Score')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(save_path)  # ✅ Now save_path is defined
    print(f"Plot saved to: {save_path}")
    plt.show()