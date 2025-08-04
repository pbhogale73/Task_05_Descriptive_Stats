# 🏀 Task 05 – LLM-Based Analysis of Basketball Statistics

This project explores how effectively a modern large language model (LLM), specifically *GPT-4o* from OpenAI, can interpret and reason about structured sports data. The focus is on the 2023–2024 Syracuse University Women’s Basketball season, using natural language prompts to evaluate the model’s analytical capabilities.

---

## 📊 Data Overview

- *Source*: [Syracuse Women’s Basketball Official Site](https://cuse.com)
- *Content*: Season statistics in PDF format
- *Coverage*:
  - Individual player stats (entire season + conference-only)
  - Team performance metrics
  - Game-level results
- *Note*: The raw PDF data was processed locally and is intentionally excluded from this repository in line with project requirements.

---

## 📁 Directory Layout


.
├── data/                        # Raw PDF file (excluded from GitHub)
├── extracted_csv/              # Structured CSVs derived from PDF
│   ├── players_overall.csv
│   └── players_conference.csv
├── prompts/
│   └── basketball_prompts.md   # Questions asked to the LLM
├── results/
│   ├── descriptive_summary.json    # Stats calculated via Python
│   └── llm_testing_results.json    # GPT-4o responses and correctness
├── scripts/
│   ├── data_extractor.py           # PDF parsing and cleaning
│   ├── descriptive_stats.py        # Metric computation logic
│   └── llm_evaluator.py            # Prompt response logger
└── README.md


---

## 🧠 Model Details

- *LLM Used*: gpt-4o (OpenAI)
- *Release Date*: May 2024
- *Why GPT-4o?*
  - Excels at processing and reasoning over structured data
  - Faster and more cost-efficient than previous GPT-4 variants
  - Capable of handling longer contexts and multimodal inputs
- *Platform*: ChatGPT (chat.openai.com)

---

## 🔍 Types of Prompts Used

A range of natural language questions were tested, such as:

- Who led the team in scoring?
- Which player had the most accurate shooting?
- Who dominated in rebounds?
- Who maintained the best assist-to-turnover balance?
- What should the coach focus on to improve future performance?

> Full list: [prompts/basketball_prompts.md](./prompts/basketball_prompts.md)

---

## ✅ LLM Evaluation Summary

| Category                  | Result        |
|--------------------------|---------------|
| Core player stats         | ✅ Accurate   |
| Efficiency analysis       | ✅ Accurate   |
| Rebounding + AST/TO       | ✅ Accurate   |
| Strategic reasoning       | 🔄 Planned for next phase |

All tested queries were correctly answered by GPT-4o, with outputs verified against Python-generated ground truth data.

---

## 🔮 Planned Enhancements (Next Reporting Period)

- Introduce visual analytics (e.g., bar charts, radar graphs)
- Benchmark GPT-4o against other models like *Claude, **Gemini, and **Copilot*
- Explore complex prompt chains for strategic questions
- Automate prompt handling via the OpenAI API
