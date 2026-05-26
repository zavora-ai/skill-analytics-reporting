# Analytics Skill Examples

## Example 1: "How's our MRR doing?"

**User says:** "What's our MRR looking like this month?"

**Tool calls:**
```
1. query_metric(name: "mrr", period: "last_30d") → trend data
2. compare_metric(name: "mrr", period_a: "this_month", period_b: "last_month")
   → {current: 125000, previous: 118000, change_pct: 5.9}
3. breakdown_metric(name: "mrr", dimension: "plan")
   → [{plan: "Enterprise", value: 75000}, {plan: "Pro", value: 40000}, {plan: "Starter", value: 10000}]
```

**Response:**
```
## MRR: $1,250 (+5.9% MoM) ↗️

| Plan | MRR | Share | Growth |
|------|-----|-------|--------|
| Enterprise | $750 | 60% | +8% |
| Pro | $400 | 32% | +3% |
| Starter | $100 | 8% | +1% |

**Insight:** Enterprise driving growth (+8%). Pro stable. Starter flat — consider activation campaign.

**Forecast:** At current growth, hitting $1,320 MRR by end of Q1.
```

## Example 2: "Where are we losing users in the signup funnel?"

**User says:** "Analyze our conversion funnel"

**Tool calls:**
```
1. analyze_funnel(steps: ["visit", "signup", "activation", "paid"])
   → {steps: [{name: "visit", count: 10000}, {name: "signup", count: 1200, rate: 12%}, {name: "activation", count: 800, rate: 67%}, {name: "paid", count: 180, rate: 22.5%}]}

2. explain_change(metric: "activation_rate", period: "last_30d")
   → {cause: "New onboarding flow reduced activation by 5% for mobile users"}
```

**Response:**
```
## Conversion Funnel

| Step | Users | Rate | Drop-off |
|------|-------|------|----------|
| Visit | 10,000 | — | — |
| Signup | 1,200 | 12% | 88% |
| Activation | 800 | 67% | 33% ⚠️ |
| Paid | 180 | 22.5% | 77.5% 🚨 |

**Biggest leak:** Activation → Paid (77.5% drop-off)
**Root cause:** New onboarding flow hurting mobile users (-5% activation)

**Revenue impact:** If we recover 5% activation: +40 activated users → ~9 more paid = +$450/mo

**Recommendation:** A/B test reverting mobile onboarding flow. Quick win: add progress indicator.
```

## Example 3: "Something's wrong with signups today"

**User says:** "Signups seem way down. What happened?"

**Tool calls:**
```
1. detect_anomalies(metrics: ["signups"], lookback: "3d")
   → {anomalies: [{metric: "signups", date: "today", expected: 42, actual: 11, severity: "critical"}]}

2. explain_change(metric: "signups", period: "today")
   → {attribution: [{dimension: "source", segment: "organic", impact: -85%}, {dimension: "device", segment: "all", impact: -73%}]}
```

**Response:**
```
🚨 Signup Anomaly Detected

**Today:** 11 signups (expected: 42) — **74% below normal**

**Root cause:** Organic traffic dropped 85%. Affects all devices.
**Likely issue:** Landing page or SEO problem.

**Recommended actions:**
1. Check landing page for errors (500s, broken forms)
2. Verify Google Search Console for indexing issues
3. Check if recent deploy broke the signup flow

**Revenue impact:** At current conversion, losing ~7 paid customers/day = ~$350/day revenue loss.

Want me to alert #engineering on Slack?
```
