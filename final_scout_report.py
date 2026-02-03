import matplotlib
matplotlib.use("Agg")  # Forces non-GUI backend to stop WSL/Wayland errors
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Standardize on one filename
INPUT_CSV = "scouting_report.csv"
OUTPUT_MAP = "scouting_map.png"

def generate_final_deliverables():
    if not os.path.exists(INPUT_CSV):
        print(f"❌ Error: {INPUT_CSV} not found. Run scout_analysis.py first.")
        return

    df = pd.read_csv(INPUT_CSV)
    
    # 1. Calculate and Print Professional Metrics
    print("\n📋 --- OFFICIAL SCOUTING SUMMARY ---")
    for cluster in df['zone_cluster'].unique():
        cluster_data = df[df['zone_cluster'] == cluster]
        spread = np.sqrt(cluster_data['x'].var() + cluster_data['y'].var())
        
        # Identify team based on player names in the cluster
        team_label = "Cloud9 (Offense)" if "C9" in str(cluster_data['name'].iloc[0]) else "Enemy (Defense)"
        
        print(f"🔹 {team_label}:")
        print(f"   - Position: {'Backsite/Anchor' if cluster == 0 else 'Mid/Entry'}")
        print(f"   - Coordination Metric (Spread): {spread:.2f}")
        print(f"   - Behavior: {'Tight Stack' if spread < 100 else 'Spread Default'}")

    # 2. Generate the Map without Terminal Noise
    plt.figure(figsize=(10, 8))
    colors = ['#8e44ad', '#f1c40f'] # Purple for Enemy, Yellow for C9
    
    for i, cluster in enumerate(df['zone_cluster'].unique()):
        data = df[df['zone_cluster'] == cluster]
        plt.scatter(data['x'], data['y'], c=colors[i], label=f"Zone {cluster}", s=100, edgecolors='black')
        for _, row in data.iterrows():
            plt.annotate(row['name'], (row['x'], row['y']), xytext=(5, 5), textcoords='offset points')

    plt.title("VALORANT Spatial Analysis: Team Tendency Map")
    plt.xlabel("X Coord")
    plt.ylabel("Y Coord")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig(OUTPUT_MAP)
    print(f"\n🎨 SUCCESS: Heatmap saved to '{OUTPUT_MAP}'")
    print(f"📂 To view: explorer.exe {OUTPUT_MAP}")

if __name__ == "__main__":
    generate_final_deliverables()
