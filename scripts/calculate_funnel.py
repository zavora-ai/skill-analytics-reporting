#!/usr/bin/env python3
"""Calculate funnel conversion rates and identify biggest leak."""
import json, sys

def analyze(data):
    steps = data.get("steps", [])
    if len(steps) < 2:
        return {"error": "Need at least 2 steps"}
    results = []
    biggest_leak = {"step": "", "drop": 0}
    for i in range(len(steps)):
        step = {"name": steps[i]["name"], "count": steps[i]["count"]}
        if i == 0:
            step["rate"] = 100.0
            step["drop"] = 0
        else:
            step["rate"] = round(steps[i]["count"] / steps[i-1]["count"] * 100, 1) if steps[i-1]["count"] > 0 else 0
            step["drop"] = round(100 - step["rate"], 1)
            if step["drop"] > biggest_leak["drop"]:
                biggest_leak = {"step": f"{steps[i-1]['name']} → {steps[i]['name']}", "drop": step["drop"]}
        results.append(step)
    overall = round(steps[-1]["count"] / steps[0]["count"] * 100, 1) if steps[0]["count"] > 0 else 0
    return {"steps": results, "overall_conversion": overall, "biggest_leak": biggest_leak}

if __name__ == "__main__":
    print(json.dumps(analyze(json.loads(sys.argv[1])), indent=2))
