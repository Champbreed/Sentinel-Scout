import json
import pandas as pd
from sklearn.cluster import KMeans
import os

# 1. Load the Data
DATA_PATH = "raw_match_data/match_mock_data.json"

def run_scouting_report():
    if not os.path.exists(DATA_PATH):
        print("❌ Error: Mock data file missing.")
        return

    with open(DATA_PATH, 'r') as f:
        data = json.load(f)

    # 2. Extract Coordinates
    coords = []
    for snapshot in data.get("snapshots", []):
        for player in snapshot.get("playerStates", []):
            coords.append({
                "name": player["name"],
                "x": player["x"],
                "y": player["y"]
            })

    df = pd.DataFrame(coords)
    print(f"📊 Extracted {len(df)} positioning points.")

    # 3. K-Means Clustering (Identifying 2 Hot Zones)
    # Even with small data, this proves the pipeline works
    kmeans = KMeans(n_clusters=2, n_init=10)
    df['zone_cluster'] = kmeans.fit_predict(df[['x', 'y']])

    # 4. Generate the Report
    print("\n📝 --- SCOUTING REPORT: HOT ZONES ---")
    for i, center in enumerate(kmeans.cluster_centers_):
        print(f"Zone {i+1} Center: X={center[0]:.2f}, Y={center[1]:.2f}")

    # Save results for the Committee
    df.to_csv("scouting_report.csv", index=False)
    print("\n✨ SUCCESS: Scouting Report saved to 'scouting_report.csv'")

if __name__ == "__main__":
    run_scouting_report()
