"""
Humanitarian Mapping Impact Analysis
Comprehensive assessment of mapping contributions and humanitarian value
"""

import json
import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
PROJECT_JSON = BASE_DIR / "project_32710.json"
OUTPUT_DIR = BASE_DIR / "outputs"


def load_project_data():
    """Load HOT Tasking Manager project data"""
    with open(PROJECT_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def calculate_mapping_metrics(data: dict) -> dict:
    """Calculate comprehensive mapping contribution metrics"""
    
    features = data.get("tasks", {}).get("features", [])
    
    # Task status breakdown
    status_counts = {}
    for feat in features:
        status = feat.get("properties", {}).get("taskStatus", "UNKNOWN")
        status_counts[status] = status_counts.get(status, 0) + 1
    
    total_tasks = sum(status_counts.values())
    mapped = status_counts.get("MAPPED", 0) + status_counts.get("VALIDATED", 0)
    validated = status_counts.get("VALIDATED", 0)
    
    # Completion metrics
    metrics = {
        "project_id": data.get("projectId"),
        "project_name": data.get("projectInfo", {}).get("name", ""),
        "organization": data.get("organisationName", ""),
        "priority": data.get("projectPriority", ""),
        "status": data.get("status", ""),
        "total_tasks": total_tasks,
        "mapped_tasks": mapped,
        "validated_tasks": validated,
        "invalidated_tasks": status_counts.get("INVALIDATED", 0),
        "ready_tasks": status_counts.get("READY", 0),
        "bad_imagery_tasks": status_counts.get("BADIMAGERY", 0),
        "percent_mapped": round((mapped / total_tasks * 100) if total_tasks > 0 else 0, 2),
        "percent_validated": round((validated / total_tasks * 100) if total_tasks > 0 else 0, 2),
        "active_mappers": data.get("activeMappers", 0),
        "total_mappers": len(data.get("contributors", [])) if "contributors" in data else 0,
        "created": data.get("created"),
        "last_updated": data.get("lastUpdated"),
        "due_date": data.get("dueDate"),
    }
    
    return metrics


def estimate_humanitarian_impact(metrics: dict) -> dict:
    """Estimate humanitarian impact of mapping efforts"""
    
    # Assumptions based on typical HOT project impact
    BUILDINGS_PER_TASK_AVG = 50  # Average buildings mapped per task
    PEOPLE_PER_BUILDING_AVG = 4  # Average occupancy
    ROAD_KM_PER_TASK_AVG = 2.5  # Average km of roads per task
    
    mapped_tasks = metrics["mapped_tasks"]
    
    impact = {
        "estimated_buildings_mapped": mapped_tasks * BUILDINGS_PER_TASK_AVG,
        "estimated_population_covered": mapped_tasks * BUILDINGS_PER_TASK_AVG * PEOPLE_PER_BUILDING_AVG,
        "estimated_road_km_mapped": mapped_tasks * ROAD_KM_PER_TASK_AVG,
        "humanitarian_applications": [
            "Flood risk assessment and evacuation planning",
            "Emergency response routing",
            "Infrastructure damage assessment",
            "Population density mapping",
            "Aid distribution planning"
        ]
    }
    
    return impact


def calculate_volunteer_efficiency(metrics: dict) -> dict:
    """Calculate volunteer contribution efficiency metrics"""
    
    total_mappers = max(metrics["total_mappers"], metrics["active_mappers"])
    mapped_tasks = metrics["mapped_tasks"]
    
    if total_mappers == 0:
        avg_tasks_per_mapper = 0
    else:
        avg_tasks_per_mapper = mapped_tasks / total_mappers
    
    efficiency = {
        "total_contributors": total_mappers,
        "active_recent_mappers": metrics["active_mappers"],
        "avg_tasks_per_contributor": round(avg_tasks_per_mapper, 2),
        "tasks_remaining": metrics["total_tasks"] - metrics["mapped_tasks"],
        "validation_backlog": metrics["mapped_tasks"] - metrics["validated_tasks"],
        "validation_completion_rate": round((metrics["validated_tasks"] / metrics["mapped_tasks"] * 100) if metrics["mapped_tasks"] > 0 else 0, 2)
    }
    
    return efficiency


def generate_campaign_insights(data: dict) -> list:
    """Generate insights for campaign management"""
    
    insights = []
    
    metrics = calculate_mapping_metrics(data)
    
    # Progress insights
    if metrics["percent_mapped"] >= 95:
        insights.append({
            "type": "SUCCESS",
            "insight": "Project nearly complete - excellent mapper engagement",
            "metric": f"{metrics['percent_mapped']}% mapped"
        })
    elif metrics["percent_mapped"] < 50:
        insights.append({
            "type": "ACTION_NEEDED",
            "insight": "Project needs more mapper attention",
            "metric": f"Only {metrics['percent_mapped']}% mapped"
        })
    
    # Validation insights
    validation_gap = metrics["mapped_tasks"] - metrics["validated_tasks"]
    if validation_gap > 100:
        insights.append({
            "type": "VALIDATION_NEEDED",
            "insight": "Significant validation backlog - organize validation clinic",
            "metric": f"{validation_gap} tasks awaiting validation"
        })
    elif metrics["percent_validated"] > 80:
        insights.append({
            "type": "SUCCESS",
            "insight": "Excellent validation coverage maintained",
            "metric": f"{metrics['percent_validated']}% validated"
        })
    
    # Community engagement
    if metrics["active_mappers"] > 20:
        insights.append({
            "type": "COMMUNITY",
            "insight": "Strong volunteer participation - active community",
            "metric": f"{metrics['active_mappers']} active mappers"
        })
    elif metrics["active_mappers"] < 5:
        insights.append({
            "type": "COMMUNITY",
            "insight": "Low mapper engagement - consider promotional campaign",
            "metric": f"Only {metrics['active_mappers']} active mappers"
        })
    
    # Priority and urgency
    if metrics["priority"] in ["URGENT", "HIGH"]:
        insights.append({
            "type": "URGENCY",
            "insight": "High-priority humanitarian project - rapid completion critical",
            "metric": f"Priority: {metrics['priority']}"
        })
    
    return insights


def generate_recommendations(metrics: dict, efficiency: dict) -> list:
    """Generate actionable recommendations"""
    
    recommendations = []
    
    # Mapping recommendations
    if metrics["ready_tasks"] > 50:
        recommendations.append({
            "priority": "HIGH",
            "area": "Mapping Campaign",
            "action": f"Organize focused mapping event - {metrics['ready_tasks']} tasks ready to map",
            "target": "Complete 30-50 tasks per session"
        })
    
    # Validation recommendations
    if efficiency["validation_backlog"] > 50:
        recommendations.append({
            "priority": "HIGH",
            "area": "Quality Assurance",
            "action": f"Schedule validation clinic - {efficiency['validation_backlog']} tasks awaiting QA",
            "target": "Achieve 80% validation rate"
        })
    
    # Community building
    if metrics["active_mappers"] < 10:
        recommendations.append({
            "priority": "MEDIUM",
            "area": "Community Engagement",
            "action": "Expand mapper recruitment through Missing Maps events",
            "target": "Increase active mapper count to 15+"
        })
    
    # Training needs
    if metrics["invalidated_tasks"] > 10:
        recommendations.append({
            "priority": "MEDIUM",
            "area": "Mapper Training",
            "action": f"Conduct training session on common issues ({metrics['invalidated_tasks']} invalidations)",
            "target": "Reduce invalidation rate below 5%"
        })
    
    # Bad imagery
    if metrics["bad_imagery_tasks"] > 5:
        recommendations.append({
            "priority": "LOW",
            "area": "Imagery Access",
            "action": f"Request alternative imagery sources for {metrics['bad_imagery_tasks']} tasks",
            "target": "Enable completion of all tasks"
        })
    
    # Completion strategy
    tasks_remaining = metrics["total_tasks"] - metrics["mapped_tasks"]
    if 0 < tasks_remaining <= 50:
        recommendations.append({
            "priority": "HIGH",
            "area": "Project Completion",
            "action": f"Final push needed - only {tasks_remaining} tasks remaining",
            "target": "Complete project within 1-2 weeks"
        })
    
    return recommendations


def generate_impact_report():
    """Generate comprehensive impact analysis report"""
    
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    print("=" * 80)
    print("HUMANITARIAN MAPPING IMPACT ANALYSIS")
    print("HOT Tasking Manager Project Assessment")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print()
    
    # Load project data
    print("Loading project data...")
    data = load_project_data()
    
    # Calculate metrics
    metrics = calculate_mapping_metrics(data)
    impact = estimate_humanitarian_impact(metrics)
    efficiency = calculate_volunteer_efficiency(metrics)
    
    # Project Overview
    print("-" * 80)
    print("PROJECT OVERVIEW")
    print("-" * 80)
    print(f"Project ID: {metrics['project_id']}")
    print(f"Name: {metrics['project_name']}")
    print(f"Organization: {metrics['organization']}")
    print(f"Priority: {metrics['priority']}")
    print(f"Status: {metrics['status']}")
    print(f"Created: {metrics['created']}")
    print(f"Last Updated: {metrics['last_updated']}")
    print(f"Due Date: {metrics['due_date']}")
    print()
    
    # Mapping Progress
    print("-" * 80)
    print("MAPPING PROGRESS")
    print("-" * 80)
    print(f"Total Tasks: {metrics['total_tasks']}")
    print(f"Mapped: {metrics['mapped_tasks']} ({metrics['percent_mapped']}%)")
    print(f"Validated: {metrics['validated_tasks']} ({metrics['percent_validated']}%)")
    print(f"Invalidated: {metrics['invalidated_tasks']}")
    print(f"Ready to Map: {metrics['ready_tasks']}")
    print(f"Bad Imagery: {metrics['bad_imagery_tasks']}")
    print()
    
    # Volunteer Engagement
    print("-" * 80)
    print("VOLUNTEER ENGAGEMENT")
    print("-" * 80)
    print(f"Total Contributors: {efficiency['total_contributors']}")
    print(f"Active Recent Mappers: {efficiency['active_recent_mappers']}")
    print(f"Avg Tasks per Contributor: {efficiency['avg_tasks_per_contributor']}")
    print(f"Tasks Remaining: {efficiency['tasks_remaining']}")
    print(f"Validation Backlog: {efficiency['validation_backlog']}")
    print(f"Validation Completion: {efficiency['validation_completion_rate']}%")
    print()
    
    # Humanitarian Impact
    print("-" * 80)
    print("ESTIMATED HUMANITARIAN IMPACT")
    print("-" * 80)
    print(f"Buildings Mapped: ~{impact['estimated_buildings_mapped']:,}")
    print(f"Population Covered: ~{impact['estimated_population_covered']:,} people")
    print(f"Road Network: ~{impact['estimated_road_km_mapped']:.1f} km")
    print("\nHumanitarian Applications:")
    for app in impact['humanitarian_applications']:
        print(f"  • {app}")
    print("\nNote: Estimates based on typical task completion patterns")
    print()
    
    # Campaign Insights
    print("-" * 80)
    print("CAMPAIGN INSIGHTS")
    print("-" * 80)
    insights = generate_campaign_insights(data)
    for insight in insights:
        print(f"[{insight['type']}] {insight['insight']}")
        print(f"  → {insight['metric']}")
        print()
    
    # Recommendations
    print("-" * 80)
    print("ACTIONABLE RECOMMENDATIONS")
    print("-" * 80)
    recommendations = generate_recommendations(metrics, efficiency)
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. [{rec['priority']}] {rec['area']}")
        print(f"   Action: {rec['action']}")
        print(f"   Target: {rec['target']}")
        print()
    
    # Save outputs
    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_csv(OUTPUT_DIR / "detailed_project_metrics.csv", index=False)
    
    efficiency_df = pd.DataFrame([efficiency])
    efficiency_df.to_csv(OUTPUT_DIR / "volunteer_efficiency_metrics.csv", index=False)
    
    impact_df = pd.DataFrame([{k: v for k, v in impact.items() if not isinstance(v, list)}])
    impact_df.to_csv(OUTPUT_DIR / "humanitarian_impact_estimates.csv", index=False)
    
    insights_df = pd.DataFrame(insights)
    insights_df.to_csv(OUTPUT_DIR / "campaign_insights.csv", index=False)
    
    recommendations_df = pd.DataFrame(recommendations)
    recommendations_df.to_csv(OUTPUT_DIR / "action_recommendations.csv", index=False)
    
    print("=" * 80)
    print(f"ANALYSIS COMPLETE - All outputs saved to: {OUTPUT_DIR}")
    print("=" * 80)


if __name__ == "__main__":
    generate_impact_report()
