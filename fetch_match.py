import os
import json

def load_data():
    mock_path = "raw_match_data/match_mock_data.json"
    
    # Check if we have our mock 'fail-safe'
    if os.path.exists(mock_path):
        with open(mock_path, 'r') as f:
            print("💡 API Blocked: Using Local Mock Data for Analysis...")
            return json.load(f)
    else:
        print("❌ Error: No API access and no mock file found.")
        return None

if __name__ == "__main__":
    data = load_data()
    if data:
        print(f"✅ Data loaded for Series: {data['series_id']} on Map: {data['map']}")
        # Now you can pass 'data' to your clustering/analysis function
