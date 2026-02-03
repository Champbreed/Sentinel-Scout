import pandas as pd
import matplotlib.pyplot as plt

def generate_map():
    # Load the report you just generated
    try:
        df = pd.read_csv("scouting_report.csv")
    except FileNotFoundError:
        print("❌ Error: Run scout_analysis.py first to generate the CSV.")
        return

    plt.figure(figsize=(10, 8))
    
    # Plot the clusters with different colors
    scatter = plt.scatter(df['x'], df['y'], c=df['zone_cluster'], cmap='viridis', s=100, edgecolors='black')
    
    # Label each point with the player name
    for i, txt in enumerate(df['name']):
        plt.annotate(txt, (df['x'][i], df['y'][i]), xytext=(5, 5), textcoords='offset points')

    plt.title("VALORANT Scouting Report: Map Position Hot Zones (Mock Ascent)")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Save the plot
    plt.savefig("scouting_map.png")
    print("🎨 SUCCESS: Heatmap saved to 'scouting_map.png'")
    print("👉 If you are using WSL, you can open it with: explorer.exe scouting_map.png")

if __name__ == "__main__":
    generate_map()
