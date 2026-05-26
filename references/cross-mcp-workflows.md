# Analytics Cross-MCP Workflows

## Analytics + Slack: Revenue Alerts

### Daily revenue digest
```
ANALYTICS: query_metric(name: "mrr") → {value: 125000}
ANALYTICS: compare_metric(name: "mrr", period_a: "today", period_b: "yesterday") → {change: "+0.3%"}
ANALYTICS: detect_anomalies(metrics: ["revenue", "churn"]) → {anomalies: []}
SLACK: send_message(channel: "#revenue", text: "📊 *Daily Revenue*\nMRR: $1,250 (+0.3%)\nNew customers: 3\nChurn: 0\nAnomalies: None ✅")
```

### Anomaly detected → Alert team
```
ANALYTICS: detect_anomalies(metrics: ["signups"]) → {anomalies: [{severity: "critical", actual: 11, expected: 42}]}
ANALYTICS: explain_change(metric: "signups") → {cause: "organic traffic -85%"}
SLACK: send_message(channel: "#growth", text: "🚨 *Signup Anomaly*\nToday: 11 (expected 42) — 74% below normal\nCause: Organic traffic collapsed\nRevenue impact: ~$350/day\n@engineering please investigate landing page")
```

## Analytics + CRM: Funnel → Sales Action

### Low conversion segment → Target with sales
```
ANALYTICS: analyze_funnel(steps: ["trial", "paid"]) → {enterprise_conversion: 12%, down from 20%}
ANALYTICS: explain_change(metric: "enterprise_trial_to_paid") → {cause: "no sales touch in first 7 days"}
CRM: search_deals(stage: "Trial", segment: "enterprise") → [{name: "Acme", value: 50000, days_in_trial: 10}]
CRM: create_activity(type: "task", subject: "URGENT: Reach out to Acme trial — enterprise conversion dropping")
```

## Analytics + Email: Scheduled Reports

### Weekly executive summary
```
ANALYTICS: get_profit_loss(period: "this_week") → revenue data
ANALYTICS: analyze_funnel(steps: [...]) → conversion data
ANALYTICS: forecast_metric(name: "mrr", horizon: 30) → forecast
EMAIL: email_send(to: "exec-team@company.com", subject: "Weekly Revenue Report", body: formatted_report)
```

## Analytics + Finance: Revenue Reconciliation

### Verify analytics revenue matches books
```
ANALYTICS: query_metric(name: "revenue", period: "2025-01") → {value: 125000}
FINANCE: get_profit_loss(period: "2025-01") → {revenue: 122000}
→ Gap: $30 (analytics counts at booking, finance at recognition)
→ Flag if gap > 5% for investigation
```
