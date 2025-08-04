# scripts/descriptive_stats.py

import pandas as pd
from pathlib import Path

# Load overall player stats CSV
csv_path = Path("../extracted_csv/players_overall.csv")
df = pd.read_csv(csv_path)

# Clean numeric columns
df["PPG"] = pd.to_numeric(df["PPG"], errors="coerce")
df["FG%"] = pd.to_numeric(df["FG%"], errors="coerce")
df["TOT"] = pd.to_numeric(df["TOT"], errors="coerce")
df["AST"] = pd.to_numeric(df["AST"], errors="coerce")
df["TO"] = pd.to_numeric(df["TO"], errors="coerce")

# Calculate AST/TO ratio
df["AST_TO_Ratio"] = df["AST"] / df["TO"]
df["AST_TO_Ratio"] = df["AST_TO_Ratio"].round(2)

# Drop rows with missing key values
df = df.dropna(subset=["PPG", "FG%", "TOT", "AST_TO_Ratio"])

# Get Top Stats
top_scorer = df.loc[df["PPG"].idxmax()]
best_fg = df.loc[df["FG%"].idxmax()]
top_rebounder = df.loc[df["TOT"].idxmax()]
best_ast_to = df.loc[df["AST_TO_Ratio"].idxmax()]

# Print Summary
print("\n🎯 Top Players Summary (2023–24):\n")
print(f"🏀 Top Scorer: {top_scorer['Name']} — {top_scorer['PPG']} PPG")
print(f"🎯 Best FG%: {best_fg['Name']} — {best_fg['FG%']*100:.1f}%")
print(f"🧱 Most Rebounds: {top_rebounder['Name']} — {int(top_rebounder['TOT'])} rebounds")
print(f"📊 Best AST/TO Ratio: {best_ast_to['Name']} — {best_ast_to['AST_TO_Ratio']}")

# Save results to JSON (optional)
summary = {
    "top_scorer": {"name": top_scorer["Name"], "ppg": float(top_scorer["PPG"])},
    "best_fg": {"name": best_fg["Name"], "fg_percent": float(best_fg["FG%"])},
    "top_rebounder": {"name": top_rebounder["Name"], "rebounds": int(top_rebounder["TOT"])},
    "best_ast_to_ratio": {"name": best_ast_to["Name"], "ratio": float(best_ast_to["AST_TO_Ratio"])},
}

output_path = Path("../results/descriptive_summary.json")
output_path.parent.mkdir(exist_ok=True)
pd.Series(summary).to_json(output_path, indent=2)
print(f"\n✅ Summary saved to: {output_path}")
