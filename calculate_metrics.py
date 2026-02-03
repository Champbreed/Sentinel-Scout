import pandas as pd
import numpy as np

def calculate_metrics():
    df = pd.read_csv("scouting_report.csv")
    
    print("\n📈 --- ADVANCED SCOUTING METRICS ---")
    for cluster in df['zone_cluster'].unique():
        cluster_data = df[df['zone_cluster'] == cluster]
        
        # Calculate Standard Deviation as a proxy for "Spread"
        spread = np.sqrt(cluster_data['x'].var() + cluster_data['y'].var())
        
        team_name = "Cloud9 Cluster" if cluster == 1 else "Enemy Cluster"
        print(f"{team_name} Spread (Tightness): {spread:.2f}")
        
    print("\n💡 NOTE: Lower spread = tighter coordination/stacking.")

if __name__ == "__main__":
    calculate_metrics()
