# HOT Tasking Manager Mapathon Playbook (Project 32710 — Mingora City Part 2)

**Focus project.** Pakistan Monsoon Floods 2025 – MAP building footprints for Mingora City Part 2 (HOT TM #32710, priority “URGENT”).  
**Reference materials.**
- Missing Maps “Host a Mapathon” guide: https://www.missingmaps.org/host/  
- Tasking Manager mapping walkthrough: https://learnosm.org/en/coordination/tasking-manager/  
- Validation best practices (HOT): https://docs.hotosm.org/validation/validation_guide/

## 1. Pre-event setup
- Review the project instructions and imagery stack (`project_32710.json` → `projectInfo.description`).
- Prepare a 10-minute onboarding deck highlighting: project goals, HOT Code of Conduct, mapping tool choice (iD vs JOSM).
- Create sign-in sheet (name, OSM username, editor choice, experience level). Template provided in `templates/mapathon_signin.xlsx` (create new if needed).
- Configure live comms (Jitsi + Slack #pakistan-floods channel) and queue `Task boundaries` in HOT TM for screen share.

## 2. 60-minute mapper induction (repeat for each cohort)
1. **00:00–00:10** — Welcome, safety briefing, why Mingora needs building footprints (link to NDMA flood risk bulletins).
2. **00:10–00:25** — Live demo: pick random task, show iD workflow, emphasise tracing footprints, avoiding overlaps, use of imagery offset.
3. **00:25–00:45** — Supervised mapping sprint. Facilitators circulate (via chat + breakout rooms) to unblock participants.
4. **00:45–01:00** — Group recap, flag tasks needing validation, log blockers in shared pad.

## 3. Validation micro-sprint (45 minutes)
1. Pull tasks flagged via comment or mapathon lead.  
2. Apply HOT Validation Checklist (see `validation_checklist.md`).  
3. Record task IDs + outcomes in `outputs/validation_log_template.csv` (columns: task_id, validator, decision, notes, buildings_fixed, roads_fixed).  
4. Push summary comment to Tasking Manager after each batch (cite imagery, note unresolved issues).

## 4. Stats tracking
- Before first session: export the baseline summary (`outputs/project_32710_summary.csv`).
- After each session: capture Tasking Manager “Stats” tab screenshots + copy counts for tasks mapped/validated, buildings mapped, roads added (visible in TM UI). Store filenames `evidence/stats_YYYYMMDD_sessionN.png`.
- Supplement with HOT Humanitarian OSM Stats dashboard (https://analytics.hotosm.org/ — filter by project 32710) to extract km of roads and building counts. Record values in `outputs/impact_tracker.csv` (columns already provided).

## 5. Community follow-up
- Email project owners (Open Mapping Hub Asia-Pacific) with quick wins, blockers, requests for additional imagery.  
- Share Missing Maps feedback form with volunteers within 24 h.  
- Schedule refresher validation clinic for experienced contributors (use Validation Hub materials).
