import pandas as pd
import json

# Load results
with open('results/results.json', 'r') as file:
  data = json.load(file)

# Prepare data for cost and latency analysis
rows = []
for result in data.get('results', {}).get('prompts', []):
  cost_per_request = result.get('metrics', {}).get('cost', 0)
  latency_ms = result.get('metrics', {}).get('totalLatencyMs', 0)
  daily_cost = cost_per_request * 100_000
  monthly_cost = daily_cost * 30
  yearly_cost = monthly_cost * 12
  rows.append({
      'provider': result.get('provider', 'unknown'),
      'prompt': result.get('raw', 'unknown'),
      'cost_per_request': cost_per_request,
      'latency_ms': latency_ms,
      'daily_cost': daily_cost,
      'monthly_cost': monthly_cost,
      'yearly_cost': yearly_cost
  })

# Convert to DataFrame
df = pd.DataFrame(rows)

# Print Cost Analysis and Latency
print("\n====== Cost Analysis for 100,000 requests ======\n")

for prompt_text, group in df.groupby('prompt'):
  print(f"--- Prompt: {prompt_text} ---\n")
  print(group.drop(columns=['prompt']).to_string(
    index=False,
    col_space=20,
    formatters={
        'cost_per_request': '${:,.5f}'.format,
        'latency_ms': '{:,.2f} ms'.format,
        'daily_cost': '${:,.2f}'.format,
        'monthly_cost': '${:,.2f}'.format,
        'yearly_cost': '${:,.2f}'.format
    }
  ))
  print("\n")
  best_cost_provider = group.loc[group['yearly_cost'].idxmin()]
  best_latency_provider = group.loc[group['latency_ms'].idxmin()]
  print(f"Lowest cost provider for this prompt: {best_cost_provider['provider']}")
  print(f"Fastest provider for this prompt: {best_latency_provider['provider']}\n")

print("\n")