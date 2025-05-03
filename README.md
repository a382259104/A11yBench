# Accessibility Issue Trend Analysis

## Overview
This project analyzes GitHub accessibility issues to:
1. **Forecast trends** in accessibility fixes using Prophet time-series modeling.
2. **Evaluate seasonality** (monthly/weekly patterns).
3. It also attempts to benchmark llms on how well they can identity the categories of WCAP violations


## Key Findings
- 📉 **No significant trends** found (flat Kendall’s τ: `τ=0.08, p=0.62`).
- 📅 **No strong seasonality** (random fluctuations dominate).
- 🔍 Insights: _"Accessibility fixes remain ad-hoc, not systematic."_
