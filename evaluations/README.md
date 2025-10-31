# Evaluations

This folder contains configuration, results, and analysis scripts for evaluating AI prompt performance using promptfoo.

## Structure

- `promptfooconfig.yaml` — Main configuration file for running promptfoo evaluations. Defines prompts, providers, and tests.
- `results/` — Stores output files from promptfoo runs, such as `results.json`.
- `src/` — Contains analysis scripts, e.g., `analyze_results.py` for cost and latency analysis.
- `.env` — Environment variables (API keys, etc.).
- `.env.example` — Example environment file for reference.
- `.gitignore` — Specifies files/folders to exclude from version control.

## How to Use

1. **Set up your environment:**
   - Copy `.env.example` to `.env` and add your API keys.

2. **Run an evaluation:**
   - From this folder, run:
     ```
     promptfoo eval --config promptfooconfig.yaml --output restuls/results.json
     ```
   - Results will be saved in `results/results.json`.

3. **Analyze results:**
   - Run the analysis script:
     ```
     python src/analyze_results.py
     ```
   - This will print a cost and latency comparison table for each provider and prompt.

## What This Shows

- How prompt design (short vs. detailed) impacts cost, latency, and output quality.
- How to compare multiple providers (OpenAI, Anthropic, etc.) side by side.
- How to automate and analyze prompt evaluations at scale.

---

*Created as part of a prompt engineering and testing AI learning project.*
