import json
import pandas as pd
from sklearn.cluster import KMeans

def run_scout_analysis():
    print("🛰️ Sentinel Scout: Analyzing Player Tendencies...")
    
    with open('raw_match_data.json', 'r') as f:
        data = json.load(f)

    # Filter for kills that happen in the first 20 seconds (The "Default" setup)
    defaults = [e['location'] for e in data['events'] if e['type'] == 'kill' and e['time'] <= 20]
    
    if not defaults:
        print("No early round data found.")
        return

    df = pd.DataFrame(defaults)

    # Use AI (K-Means) to group these locations into 3 'Main Setup' zones
    kmeans = KMeans(n_clusters=min(3, len(df)), n_init=10)
    df['zone'] = kmeans.fit_predict(df[['x', 'y']])

    print("\n🚨 CLOUD9 SCOUTING REPORT: ENEMY DEFAULT ZONES")
    for i, center in enumerate(kmeans.cluster_centers_):
        print(f"Zone {i+1}: Coordinates ({center[0]:.0f}, {center[1]:.0f}) - High Engagement Area")

    # Save CSV for submission
    df.to_csv("scout_report.csv", index=False)
    print("\n✅ Report saved to scout_report.csv")

if __name__ == "__main__":
    run_scout_analysis()
