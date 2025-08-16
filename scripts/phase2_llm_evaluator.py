#!/usr/bin/env python3
"""
Phase 2 LLM Evaluator - Complex Reasoning Tests
Tests advanced prompts requiring strategic thinking and basketball domain knowledge
"""

import json
from pathlib import Path
from datetime import date

# Setup output directory
output_file = Path("../results/phase2_llm_testing_results.json")
output_file.parent.mkdir(exist_ok=True)

# Phase 2 Test Results - Complex Reasoning Prompts
phase2_results = {
    "metadata": {
        "phase": "Phase 2 - Complex Reasoning",
        "models_tested": ["claude-sonnet-4", "gpt-4o"],
        "test_date": str(date.today()),
        "focus": "Strategic reasoning, coaching insights, data limitations"
    },
    "complex_prompts": [
        {
            "id": 5,
            "category": "Team Analysis",
            "prompt": "Was the team stronger on offense or defense? Provide evidence using points per game and opponent points.",
            "claude_response": "Cannot complete full analysis - missing opponent points data. Offensive strengths identified: Fair (22.3 PPG), Wilson (56.8% FG%), good ball control. Need team defensive stats for comparison.",
            "gpt4o_response": "[TO BE TESTED]",
            "claude_status": "Partial - Data Limitation Identified",
            "data_limitation": "Missing team defensive statistics, opponent points per game",
            "reasoning_quality": "High - Transparent about limitations"
        },
        {
            "id": 6,
            "category": "Player Analysis",
            "prompt": "Which player had the most well-rounded performance across scoring, rebounding, and defense?",
            "claude_response": "Dyaisha Fair - Top scorer (22.3 PPG) + best playmaker (1.73 AST/TO). Most complete player with available data.",
            "gpt4o_response": "[TO BE TESTED]",
            "claude_status": "Good Answer",
            "data_limitation": "Individual defensive stats not available",
            "reasoning_quality": "Good - Used available metrics effectively"
        },
        {
            "id": 7,
            "category": "Coaching Strategy",
            "prompt": "If the coach wanted to win 2 more games next season, should they focus on improving offense or defense, and why?",
            "claude_response": "Focus on DEFENSE. Solid offensive foundation exists (Fair scoring, Wilson efficiency). Defense typically correlates higher with winning close games. Build around Latham's rebounding strength.",
            "gpt4o_response": "[TO BE TESTED]",
            "claude_status": "Excellent Strategic Reasoning",
            "data_limitation": "None significant for this analysis",
            "reasoning_quality": "Excellent - Applied basketball analytics principles"
        },
        {
            "id": 8,
            "category": "Clutch Performance",
            "prompt": "Which one player should the coach prioritize to turn close games into wins? Justify based on efficiency and clutch stats.",
            "claude_response": "Dyaisha Fair - Primary scorer (22.3 PPG) with good decision-making (1.73 AST/TO). Already handles pressure as main option, focus on late-game situations training.",
            "gpt4o_response": "[TO BE TESTED]",
            "claude_status": "Well-Justified",
            "data_limitation": "No clutch-specific stats available",
            "reasoning_quality": "Good - Logical extrapolation from available data"
        },
        {
            "id": 9,
            "category": "Temporal Analysis",
            "prompt": "How does the team's performance in the first half of games compare to the second half?",
            "claude_response": "Cannot answer - requires game segment data not available in season totals. Need half-by-half statistics.",
            "gpt4o_response": "[TO BE TESTED]",
            "claude_status": "Impossible - Wrong Data Granularity",
            "data_limitation": "Season totals insufficient, need game-level temporal data",
            "reasoning_quality": "High - Correctly identified impossible task"
        }
    ],
    "visualization_testing": {
        "claude_capabilities": [
            "Interactive bar charts (PPG comparison)",
            "Scatter plots (Efficiency vs Usage)",
            "Radar charts (Multi-dimensional player profiles)",
            "Dashboard layout with coaching insights",
            "Real-time data binding"
        ],
        "gpt4o_capabilities": "[TO BE TESTED]"
    },
    "key_insights": {
        "llm_strengths": [
            "Excellent strategic reasoning when data supports analysis",
            "Good basketball domain knowledge application",
            "Transparent about data limitations"
        ],
        "failure_modes": [
            "Questions requiring unavailable data granularity",
            "Temporal analysis without game-level data",
            "May need coaching analytics frameworks"
        ],
        "best_practices": [
            "Always verify strategic recommendations against domain knowledge",
            "Test data limitation handling explicitly",
            "Compare reasoning quality across different LLMs"
        ]
    },
    "next_testing_priorities": [
        "Test GPT-4o on same complex prompts",
        "Compare visualization generation capabilities",
        "Test additional LLMs (Gemini, Copilot)",
        "Expand dataset for temporal analysis"
    ]
}

# Save results
with open(output_file, "w") as f:
    json.dump(phase2_results, f, indent=2)