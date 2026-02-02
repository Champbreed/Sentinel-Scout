import requests

# Use your new key here
API_KEY = "bOva6yRoK6ylz8XlxbYR0EXGhDe2bC935BK2q1km"
# This is a sample Series ID. You can find more in the GRID Portal documentation.
SERIES_ID = "2589176" 
URL = f"https://api.grid.gg/file-download/end-state/grid/series/{SERIES_ID}"

def get_scouting_data():
    headers = {"x-api-key": API_KEY}
    print(f"📡 Connecting to GRID... Downloading Series {SERIES_ID}")
    
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 200:
        with open("raw_match_data.json", "w") as f:
            f.write(response.text)
        print("✅ Data Downloaded Successfully! Ready for Scout Analysis.")
    else:
        print(f"❌ Failed! Status Code: {response.status_code}")
        print("Tip: Check if the Series ID is still active in the GRID portal.")

if __name__ == "__main__":
    get_scouting_data()

