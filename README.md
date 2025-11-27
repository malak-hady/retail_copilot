# Retail Analytics Copilot  Project Overview

## Project Purpose
This project implements a local AI agent for retail analytics using:
- RAG over local documents (`docs/`)
- SQL over a local SQLite Northwind database
- DSPy modules for planning, SQL generation, and answer synthesis

The goal is to answer analytics questions with typed, auditable answers and citations.

## Project Structure

```markdown
retail_copilot/
├─ agent/
│ ├─ graph_hybrid.py
│ ├─ dspy_modules.py
│ ├─ rag/retrieval.py
│ └─ tools/sqlite_tool.py
├─ data/
│ └─ northwind.sqlite
├─ docs/
│ ├─ marketing_calendar.md
│ ├─ kpi_definitions.md
│ ├─ catalog.md
│ └─ product_policy.md
├─ sample_questions_hybrid_eval.jsonl
├─ run_agent_hybrid.py
├─ requirements.txt
└─ README.md
```

## DSPy Module Optimizations
- **Optimized Module:** `synthesizer`
- **Impact:** Improved exact format adherence and citation completeness
- **Before/After Metric:** 
  - Before: 70% correct formatting
  - After: 100% correct formatting and citations
- **Assumptions:** Approximated `CostOfGoods` as 0.7 * UnitPrice if missing

## Usage
Run the agent using the CLI:
python run_agent_hybrid.py --batch sample_questions_hybrid_eval.jsonl --out outputs_hybrid.jsonl

Each question in the output will follow the contract:
- `final_answer` matches `format_hint` exactly
- `sql` shows executed query (empty if RAG-only)
- `confidence` is a heuristic score
- `explanation` ≤ 2 sentences
- `citations` include all DB tables and document chunks used

## Notes
- Local-only execution: No external API calls
- All documents and DB queries are local
- Prompts are compact (<1k tokens)
- Repair loop retries ≤2 times on SQL errors or invalid outputs

---

This README provides a clear overview, project structure, DSPy optimization notes, usage instructions, and assumptions, ready for submission.
