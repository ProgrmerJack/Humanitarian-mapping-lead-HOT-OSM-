import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_JSON = BASE_DIR / "project_32710.json"
OUTPUT_DIR = BASE_DIR / "outputs"


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    data = json.loads(PROJECT_JSON.read_text(encoding="utf-8"))
    features = data.get("tasks", {}).get("features", [])

    status_counts = {}
    for feat in features:
        status = feat.get("properties", {}).get("taskStatus", "UNKNOWN")
        status_counts[status] = status_counts.get(status, 0) + 1

    total_tasks = sum(status_counts.values())
    percent_mapped = data.get("percentMapped")
    percent_validated = data.get("percentValidated")
    percent_bad = data.get("percentBadImagery")

    csv_lines = [
        "metric,value",
        f"project_id,{data.get('projectId')}",
        f"title,{data.get('projectInfo', {}).get('name')}",
        f"organisation,{data.get('organisationName')}",
        f"status,{data.get('status')}",
        f"priority,{data.get('projectPriority')}",
        f"total_tasks,{total_tasks}",
        f"mapped_tasks,{status_counts.get('MAPPED', 0)}",
        f"validated_tasks,{status_counts.get('VALIDATED', 0)}",
        f"invalidated_tasks,{status_counts.get('INVALIDATED', 0)}",
        f"percent_mapped,{percent_mapped}",
        f"percent_validated,{percent_validated}",
        f"percent_bad_imagery,{percent_bad}",
        f"active_mappers,{data.get('activeMappers')}",
        f"last_updated,{data.get('lastUpdated')}",
        f"due_date,{data.get('dueDate')}",
        f"campaigns,{';'.join(c.get('name', '') for c in data.get('campaigns', []))}",
    ]

    (OUTPUT_DIR / "project_32710_summary.csv").write_text(
        "\n".join(csv_lines), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
