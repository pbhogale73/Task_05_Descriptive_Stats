# scripts/data_extractor.py

import pdfplumber
import pandas as pd
import re
from pathlib import Path

# Paths
pdf_path = Path("../data/Basketball 23-24.pdf")
output_dir = Path("../extracted_csv")
output_dir.mkdir(exist_ok=True)

# Column headers from the PDF table
columns = [
    "No", "Name", "GP-GS", "MIN", "AVG", "FG-FGA", "FG%", "3FG-FGA", "3FG%", "FT-FTA", "FT%",
    "OFF", "DEF", "TOT", "RPG", "PF", "DQ", "AST", "TO", "BLK", "STL", "PTS", "PPG"
]

# Helper to split player stat lines
def split_player_row(row):
    match = re.match(r"^(\d{2}) ([A-Za-z,\.\-'\s]+?) (\d{1,2}-\d{1,2} .*)", row)
    if not match:
        return None
    number, name, rest = match.groups()
    stats = rest.split()
    return [number, name.strip()] + stats

# Lists to store extracted data
player_overall_data, player_conference_data = [], []
capture_mode = None

# Open and read PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        lines = page.extract_text().split("\n")
        for line in lines:
            if "Overall Statistics" in line and "Conference Games Only" not in line:
                capture_mode = "overall"
            elif "Conference Games Only" in line:
                capture_mode = "conference"

            if re.match(r"^\d{2} ", line) and "Total" not in line:
                if capture_mode == "overall":
                    player_overall_data.append(line)
                elif capture_mode == "conference":
                    player_conference_data.append(line)

            if "Total" in line:
                capture_mode = None

# Parse rows and write to CSV
overall_rows = [split_player_row(r) for r in player_overall_data if split_player_row(r)]
conference_rows = [split_player_row(r) for r in player_conference_data if split_player_row(r)]

pd.DataFrame(overall_rows, columns=columns).to_csv(output_dir / "players_overall.csv", index=False)
pd.DataFrame(conference_rows, columns=columns).to_csv(output_dir / "players_conference.csv", index=False)

print("✅ Extraction complete. CSVs saved to:", output_dir)
