# Task_05_Descriptive_Stats

## Research Objective
Evaluate how well large language models (LLMs) interpret structured **Syracuse Women’s Basketball (2023–24)** data—from basic stat lookups to higher-order coaching insights.

---

## Data (brief)
- **Source:** Official Syracuse athletics season PDF (not included in repo)
- **Derived:** `players_overall.csv`, `players_conference.csv`
- **Note:** Raw PDFs are excluded per assignment rules. Validation stats are computed via Python.

---

## Models
- **GPT-4o (OpenAI):** Primary for factual queries and quick checks  
- **Claude Sonnet 4 (Anthropic):** Used for strategic/analytical prompts

---

## Prompt Sets
- **Basic stats:** top scorer, best FG%, most rebounds, best AST/TO  
- **Reasoning & coaching:** offense vs defense, most well-rounded player, “win 2 more games” focus, clutch/priority player, 1H vs 2H (only if data supports)

---

## Results Summary

### 1 Basic Statistical Accuracy
| Model | Accuracy | Notes |
|---|---:|---|
| **GPT-4o** | **4/4 (100%)** | All answers matched computed ground truth (PPG, FG%, REB, AST/TO). |
| **Claude Sonnet 4** | **4/4 (100%)** | Mirrored GPT-4o on basic stat lookups. |

### 2 Reasoning & Coaching Prompts
| Question Type | GPT-4o | Claude Sonnet 4 | Key Notes |
|---|---|---|---|
| Offense vs Defense | Partial; needs team PPG & Opp PPG | **Stronger** when aggregates provided | Injecting team aggregates improves quality. |
| Most Well-Rounded Player | Subjective without a metric | **Clear** with composite scoring | Using z-score composite (PPG, REB, STL/BLK) reduces ambiguity. |
| “Win 2 More Games” Focus | Reasonable but generic | **Defense-first** case well-argued | Sensitivity (±2 PPG / Opp PPG) via Pythagorean expectation helps. |
| Priority “Clutch” Player | Plausible pick, caveats | **Well-justified** pick, caveats | Lacks clutch splits; both call out limits when asked. |
| 1H vs 2H Comparison | Not answerable | Not answerable | Requires game/half splits; correctly flagged as missing. |

**Takeaways**
- Both models are **perfect** on straightforward stat retrieval.  
- Strategy quality improves when prompts include:
  - Team aggregates (team PPG, Opp PPG)  
  - Explicit formulas (e.g., weighted composite, Pythagorean expectation)  
  - Clear “unanswerable if missing” rules

---

## Repro (quick)
```bash
# 1) Extract from PDF (if starting fresh)
python scripts/data_extractor.py

# 2) Compute validation stats
python scripts/descriptive_stats.py   # -> results/descriptive_summary.json

# 3) Log LLM results (basic)
python scripts/llm_evaluator.py       # or record directly in results JSON

# 4) Append reasoning/coaching entries (optional helper)
# create results/manual_reasoning_responses.json then:
python scripts/llm_reasoning_evaluator.py
```

---

## Repo Layout (minimal)
```
data/                      # (excluded) raw PDF
extracted_csv/
  players_overall.csv
  players_conference.csv
prompts/
  basketball_prompts.md    # basic + reasoning/coaching questions
results/
  descriptive_summary.json # computed ground truth (Python)
  llm_testing_results.json # all LLM Q&A with status/notes
scripts/
  data_extractor.py
  descriptive_stats.py
  llm_evaluator.py
  llm_reasoning_evaluator.py
README.md
```

---

## What’s Next
- Add **team_summary.csv** (team PPG & Opp PPG) to ground strategy prompts.
- Pull **game-level** data to enable close-game, clutch, and half-split analysis.
- Automate composite metric calculation; let LLMs **interpret**, not compute.

---

## Key Achievements
- **100% accuracy on basic stats** for **both** GPT-4o and Claude (4/4 each).  
- **Strategy prompts improved** materially when we injected **team aggregates** and required **explicit formulas**.  
- Established a **reusable evaluation pipeline** (`llm_evaluator.py`, `llm_reasoning_evaluator.py`, unified `llm_testing_results.json`).  
- **Hallucination control:** prompts explicitly require refusal or caveats when data is missing (e.g., clutch/half splits).  
- Delivered a **concise prompt set** separating basic vs. reasoning/coaching tasks to make evaluation comparable.  
- Kept repo **reproducible and clean**: clear scripts, minimal artifacts, ground-truth JSON for quick validation.
