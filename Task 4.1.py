import json
def task() -> float:
    with open("input.json", "r", encoding="utf-8") as json_file:
        inf = json.load(json_file)
    control_sum = sum(entry.get("score", 0) * entry.get("weight", 0) for entry in inf)
    return round(control_sum, 3)
print(task())