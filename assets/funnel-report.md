# Funnel Analysis Report

---

## Conversion Funnel — {period}

### Funnel Overview

| Step | Users | Conversion | Drop-off | vs. Prior |
|------|-------|-----------|----------|-----------|
| {step_1} | {count} | 100% | — | — |
| {step_2} | {count} | {rate}% | {drop}% | {trend_emoji} {delta}% |
| {step_3} | {count} | {rate}% | {drop}% | {trend_emoji} {delta}% |
| {step_4} | {count} | {rate}% | {drop}% | {trend_emoji} {delta}% |

**Overall conversion:** {first_to_last}%
**Biggest leak:** {worst_step} ({drop}% drop-off)

### Revenue Impact

- Users lost at {worst_step}: {lost_count}
- Estimated revenue lost: ${lost_count × avg_deal_value}
- If we improve {worst_step} by 5%: +${revenue_gain}/month

### Breakdown by Dimension

| {dimension} | Step 1→2 | Step 2→3 | Step 3→4 | Overall |
|-------------|----------|----------|----------|---------|
| {segment_a} | {rate}% | {rate}% | {rate}% | {rate}% |
| {segment_b} | {rate}% | {rate}% | {rate}% | {rate}% |

### Recommendations

1. **{worst_step}:** {specific_action} — expected impact: +{x}% conversion
2. **{second_worst}:** {specific_action}
3. **Quick win:** {low_effort_high_impact_action}

---

*Generated from mcp-analytics | {timestamp}*
