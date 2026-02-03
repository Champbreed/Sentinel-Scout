# 🎮 Sentinel Scout: Spatial Observability Engine

**Sentinel Scout** turns raw VALORANT positional telemetry into actionable scouting insights. It treats player movement as an event stream and applies **unsupervised learning** to infer default setups like defensive anchors and offensive entry formations.

## 🛡️ Technical Philosophy: "Resilient Observability"
- **Constraint:** Encountered a `403 Forbidden` entitlement block on high-fidelity series-state telemetry via the GRID Open Access tier.
- **Pivot:** Architected a **data-source-agnostic** pipeline validated on **schema-accurate mock telemetry**. 
  *Crucially, clustering is computed at runtime from raw (x, y) coordinates—the engine is logic-complete and ready for production data.*

## 🚀 Key Features
- **Unsupervised Spatial Learning:** Uses **K-Means (K=2)** to learn tactical zones directly from raw coordinate streams without pre-labeled data.
- **Euclidean Spread Metric:** Calculates the average Euclidean distance to centroids to quantify team discipline (“Tight Stack” vs “Distributed”).
- **Automated Intelligence Artifacts:** Generates a structured terminal report and a saved tactical zone plot (`scouting_map.png`).
- **Headless Architecture:** Uses the `Matplotlib Agg` backend for reliable execution in CI/CD and containerized environments.

## ⚡ Quickstart
```bash
# Install dependencies
pip install -r requirements.txt

# Execute the scouting engine
python3 scout_rigor.py
Outputs:

Terminal: Structured scouting report (centroids, zone share, spread, confidence).

File: scouting_map.png (Spatial distribution plot).

📊 Live Output (Example)
Plaintext
🏆 --- COMPETITION-GRADE SCOUTING REPORT (FINAL) ---
🤖 Model: K-Means Clustering (K=2)
📏 Metric: Spread = Avg Euclidean distance to team centroid

📍 Opponent (DEF Defaults):
   - Position: Backsite/Anchor (Centroid ≈ [-490, 2125])
   - Spread Metric: 26.93 (Tight Stack)
   - Confidence: Low (2 samples)

📍 Cloud9 (ATT Defaults):
   - Position: Mid/Entry (Centroid ≈ [1050, 4388])
   - Spread Metric: 277.59 (Distributed)
   - Confidence: Low (4 samples)
🔭 Roadmap: The Observability Giant
Coordinate Normalization: Scale logic across all VALORANT maps.

Dynamic K-Selection: Implement "Elbow Method" to auto-detect the number of active tactical zones.

Least Privilege: Hardening the execution environment in alignment with man7/capabilities.

Developed for the VCT Hackathon 2026 - Focus on Data Resilience and Spatial Analytics. 
