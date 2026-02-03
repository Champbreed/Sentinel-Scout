import os
import requests
import json

# Use the 'Open Access' endpoint from your screenshot
URL = "https://api-op.grid.gg/central-data/graphql"
API_KEY = os.environ.get("GRID_API_KEY")

def hunt_vct_series():
    if not API_KEY:
        print("❌ ERROR: Set your API key first: export GRID_API_KEY='your_key'")
        return

    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    # Query from your GRID documentation
    query = """
    query {
      allSeries(
        first: 10,
        filter: { 
            titleId: 6, 
            types: ESPORTS 
        },
        orderBy: StartTimeScheduled,
        orderDirection: DESC
      ) {
        edges {
          node {
            id
            startTimeScheduled
            tournament {
              name
            }
            teams {
              name
            }
          }
        }
      }
    }
    """

    print(f"📡 Querying Open Access Gateway: {URL}...")
    
    try:
        response = requests.post(URL, headers=headers, json={'query': query})
        
        if response.status_code == 200:
            data = response.json()
            series_list = data.get('data', {}).get('allSeries', {}).get('edges', [])
            
            print("\n🎯 --- UPCOMING/RECENT VCT SERIES ---")
            for edge in series_list:
                node = edge['node']
                teams = " vs ".join([t['name'] for t in node.get('teams', [])])
                print(f"ID: {node['id']} | {node['startTimeScheduled']} | {teams}")
        else:
            print(f"❌ Failed: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"🚨 Connection Error: {e}")

if __name__ == "__main__":
    hunt_vct_series()
