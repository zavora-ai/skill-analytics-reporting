# Analytics Tool Sequences Reference

## Tool Inventory (mcp-analytics, 28 tools)

### Discovery (5) — Understand what data exists
| Tool | Purpose |
|------|---------|
| `list_data_sources` | Connected warehouses/DBs/streams |
| `list_datasets` | Available tables with row counts |
| `describe_dataset` | Schema, columns, PII flags |
| `list_metrics` | Defined metrics with owners |
| `get_metric_definition` | Formula, aggregation, dimensions |

### Querying (5) — Pull the numbers
| Tool | Purpose | Revenue Impact |
|------|---------|---------------|
| `query_metric` | Time-series data for a metric | **Revenue tracking** |
| `breakdown_metric` | Metric by dimension | **Segment analysis** |
| `compare_metric` | Period-over-period comparison | **Growth tracking** |
| `query_events` | Raw event data | Investigation |
| `query_report` | Run saved report | Reporting |

### Analysis (6) — Find the story
| Tool | Purpose | Revenue Impact |
|------|---------|---------------|
| `analyze_funnel` | Conversion through steps | **Find revenue leaks** |
| `analyze_cohort` | Retention by cohort | **Predict LTV** |
| `detect_anomalies` | Find unusual patterns | **Catch revenue drops** |
| `forecast_metric` | Predict future values | **Revenue planning** |
| `explain_change` | Why did metric change? | **Root cause** |
| `generate_insight_summary` | AI highlights | **Executive summary** |

### Dashboards (5) — Visualize
| Tool | Purpose |
|------|---------|
| `list_dashboards` | All dashboards |
| `get_dashboard` | Dashboard with widgets |
| `summarize_dashboard` | Key takeaways |
| `create_dashboard` | Create new |
| `add_widget` | Add chart/number/funnel |

### Governance (5) — Stay compliant
| Tool | Purpose |
|------|---------|
| `validate_analytics_policy` | Check if query is allowed |
| `check_export_risk` | PII/row-count risk |
| `request_data_access` | Request restricted data |
| `get_query_audit_trail` | Audit log |
| `get_segments` | User segments |

## Sequence: Revenue Health Check (4 calls)

```
1. query_metric(name: "mrr", period: "last_30d", granularity: "daily")
   → Time series: [{date: "2025-01-01", value: 121000}, ..., {date: "2025-01-18", value: 125000}]

2. compare_metric(name: "mrr", period_a: "2025-01", period_b: "2024-12")
   → {current: 125000, previous: 118000, change: +5.9%, direction: "up"}

3. breakdown_metric(name: "mrr", dimension: "plan")
   → [{plan: "enterprise", value: 75000}, {plan: "pro", value: 40000}, {plan: "free", value: 10000}]

4. generate_insight_summary(metrics: ["mrr", "churn_rate", "new_customers"])
   → "MRR grew 5.9% MoM driven by Enterprise upgrades. Churn stable at 3.2%. 12 new customers this month."
```

## Sequence: Funnel Optimization (3 calls)

```
1. analyze_funnel(steps: ["visit", "signup", "activation", "trial_end", "paid"], period: "last_30d")
   → {steps: [{name: "visit", count: 10000}, {name: "signup", count: 1200, rate: 12%}, {name: "activation", count: 800, rate: 67%}, {name: "trial_end", count: 600, rate: 75%}, {name: "paid", count: 180, rate: 30%}]}
   → Biggest leak: trial_end → paid (70% drop-off)

2. explain_change(metric: "trial_to_paid_conversion", period: "last_30d")
   → {attribution: [{dimension: "plan", segment: "enterprise", impact: -8%}, {dimension: "source", segment: "organic", impact: -3%}]}

3. breakdown_metric(name: "trial_to_paid", dimension: "plan")
   → [{plan: "enterprise", rate: 45%}, {plan: "pro", rate: 28%}, {plan: "free_trial", rate: 8%}]
```

## Sequence: Anomaly Detection + Alert (2-3 calls)

```
1. detect_anomalies(metrics: ["revenue", "signups", "churn_rate"], lookback: "7d")
   → {anomalies: [{metric: "signups", date: "2025-01-17", expected: 40, actual: 12, severity: "high"}]}

2. explain_change(metric: "signups", period: "2025-01-17")
   → {cause: "Landing page 500 error from 14:00-22:00 UTC", dimension: "source=organic"}

3. [Cross-MCP] SLACK: send_message(channel: "#growth", text: "🚨 Signup anomaly: 70% drop on Jan 17. Cause: landing page outage 14:00-22:00.")
```
