
# Promptfoo Assertions and Analysis

This project demonstrates prompt engineering, evaluation, and analysis using [promptfoo](https://github.com/promptfoo/promptfoo). It covers prompt types, provider configs, assertion strategies, and automated result analysis.

## Project Structure

- **/prompts/** — Examples of single, multi-line, and file-based prompts.
- **/providers/** — Configurations for cloud and local model providers (OpenAI, Anthropic, LM Studio, etc.).
- **/assertions/** — Assertion sets and test configs, including deterministic and model-graded metrics.
- **/evaluations/** — End-to-end evaluation configs, results, and Python scripts for cost/latency analysis.
- **/tests/** — Test cases and CSVs for promptfoo batch testing.

## How to Use

1. **Install dependencies** (if needed):
  - `npm install -g promptfoo` or use npx
  - `pip install pandas` (for Python analysis)

2. **Set up API keys:**
  - Copy `.env.example` to `.env` in the root and fill in your provider keys.

3. **Run an evaluation:**
  - Example: `promptfoo eval --config evaluations/promptfooconfig.yaml --output results/results.json`
  - Results are saved in the corresponding `results/` folder.

4. **Analyze results:**
  - Example: `python evaluations/src/analyze_results.py`
  - View cost, latency, and other metrics per provider and prompt.
