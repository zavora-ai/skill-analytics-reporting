# Analytics & Reporting Skill (Revenue Intelligence)

> Revenue intelligence for AI agents — metrics, funnels, anomaly detection, forecasting, and dashboards. Don't just pull numbers — find the story, explain why, and recommend action.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--analytics-green)](https://github.com/zavora-ai/mcp-analytics)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## Revenue Impact

- **Funnel analysis** finds where revenue leaks (conversion drop-offs)
- **Anomaly detection** catches revenue drops within hours, not days
- **Forecasting** enables accurate revenue planning
- **Change attribution** explains WHY metrics moved (actionable, not just data)

| Workflow | Revenue Impact | Tool Calls |
|----------|---------------|-----------|
| Revenue Metrics | Track growth | 3-4 |
| Funnel Analysis | **Find revenue leaks** | 2-3 |
| Anomaly Detection | **Catch drops early** | 2-3 |
| Forecasting | Revenue planning | 2-3 |
| Dashboard Building | Executive visibility | 3-5 |
| Change Attribution | **Root cause → action** | 2-3 |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-analytics-reporting.git \
  ~/.skills/skills/analytics-reporting
```

## Requirements

**Required:** `mcp-analytics` (28 tools)

**Revenue combos:**
- `mcp-slack` — anomaly alerts and daily digests
- `mcp-crm` — funnel insights → sales actions
- `mcp-finance` — verify analytics revenue matches books

## Folder Structure

```
analytics-reporting/
├── SKILL.md                      # Main skill
├── assets/
│   └── funnel-report.md          # Funnel analysis template
├── references/
│   ├── tool-sequences.md         # 28 tools categorized
│   ├── cross-mcp-workflows.md    # Analytics + Slack + CRM + Finance
│   └── examples.md               # MRR, funnels, anomalies
├── README.md
└── LICENSE
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)

## How It Works

### The Insight Principle

This skill doesn't just pull numbers — it answers "so what?" and "now what?" for every metric:
1. **What happened?** (query_metric, compare_metric)
2. **Why?** (explain_change, breakdown_metric)
3. **What's next?** (forecast_metric, generate_insight_summary)
4. **What should we do?** (specific recommendations)

## Success Criteria

| Metric | Target |
|--------|--------|
| Insight quality | Actionable recommendations, not just numbers |
| Anomaly speed | Revenue drops caught within hours |
| Forecast accuracy | Confidence intervals on all predictions |
