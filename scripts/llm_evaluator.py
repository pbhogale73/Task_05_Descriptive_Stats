import json
from pathlib import Path
from datetime import date

output_file = Path("../results/llm_testing_results.json")
output_file.parent.mkdir(exist_ok=True)

llm_results = {
    "model": "gpt-4o",
    "provider": "OpenAI",
    "tested_on": str(date.today()),
    "responses": [
        {
            "prompt": "Who was the top scorer on the Syracuse Women's Basketball team during the 2023–2024 season?",
            "llm_answer": "Dyaisha Fair with 22.3 points per game.",
            "correct_answer": "Dyaisha Fair with 22.3 points per game.",
            "status": "✅"
        },
        {
            "prompt": "Which player had the highest field goal percentage on the team?",
            "llm_answer": "Saniaa Wilson with 56.8%.",
            "correct_answer": "Saniaa Wilson with 56.8%.",
            "status": "✅"
        },
        {
            "prompt": "Who collected the most total rebounds during the season?",
            "llm_answer": "Alyssa Latham with 224 rebounds.",
            "correct_answer": "Alyssa Latham with 224 rebounds.",
            "status": "✅"
        },
        {
            "prompt": "Which player had the best assist-to-turnover ratio?",
            "llm_answer": "Dyaisha Fair with a ratio of 1.73.",
            "correct_answer": "Dyaisha Fair with a ratio of 1.73.",
            "status": "✅"
        }
    ]
}

with open(output_file, "w") as f:
    json.dump(llm_results, f, indent=2)

print(f"✅ LLM results (with model info) saved to: {output_file}")
