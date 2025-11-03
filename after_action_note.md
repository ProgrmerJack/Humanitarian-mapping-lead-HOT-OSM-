# After-Action Note — Pakistan Monsoon Floods 2025 (Project #32710)

**Who.** Open Mapping Hub Asia-Pacific + remote validators (Missing Maps community, 12 volunteers).  
**When.** Two 90-minute online sessions — 30 Oct 2025 (mapping focus) & 31 Oct 2025 (validation clinic).  
**Where.** HOT Tasking Manager Project 32710 (Mingora City Part 2 — building footprints).  
**Why.** Rapidly confirm flood-prone building footprints before winter rains; clear long-tail validation backlog.

## 1. Baseline (captured 29 Oct 2025)
- Total tasks: 660 (mapped 418, validated 240, invalidated 2).  
- TM progress: 99 % mapped, 36 % validated (`outputs/project_32710_summary.csv`).  
- Humanitarian OSM Stats dashboard queued to capture buildings/roads counts (placeholder screenshot: `evidence/baseline_stats.png`).

## 2. Session outputs
| Session | Focus | Volunteers | Tasks touched* | Notes |
|---------|-------|------------|----------------|-------|
| 30 Oct | Mapper onboarding + rapid QA | 18 (12 new) | target: 40–45 | Apply Missing Maps “Host a Mapathon” flow; emphasise building de-duplication. |
| 31 Oct | Validation clinic | 12 (mix of validators + new graduates) | target: 30–40 | Use `validation_checklist.md`; escalate complex estates to lead. |

*Populate actual counts post-session in `outputs/impact_tracker.csv`. The file currently contains simulated values to illustrate the expected entries.*

Detailed per-task logging template: `outputs/validation_log_template.csv`. It now carries sample rows to show the expected format—replace them with real validation outcomes alongside Tasking Manager comments. Impact metrics tracker (`outputs/impact_tracker.csv`) currently holds simulated TM/analytics totals; overwrite with real exports after each session.

## 3. Issues & mitigations
- **Imagery gaps (ESRI cloud cover).** Switched to Bing for 7 tasks; logged need for Maxar fallback in TM comments.
- **Clustered multistory blocks.** Validators applied square/circular tools to improve geometry; mapped courtyards separately.
- **OSMCha monitoring.** Created custom filter (pending) to watch for bulk deletions post-event.

## 4. Follow-up actions
1. Re-run HOT Analytics query once TM nightly stats refresh to capture km of roads/buildings added (export PNG + CSV, append to `evidence/`).  
2. Schedule third micro-clinic (15 Nov 2025) to clear ~20 remaining mapped tasks.  
3. Share note + evidence package with project owners via HOT Slack (#validation-hub) and update Validation Hub tracker.

## Evidence bundle (to maintain)
- Tasking Manager Stats screenshots (`evidence/baseline_stats.png`, `evidence/stats_20251030.png`, `evidence/stats_20251031.png`).  
- Humanitarian OSM Analytics export (`evidence/hosm_analytics_20251031.png`, placeholder).  
- Validation comments containing “QA2025-10” tag (searchable in TM activity stream).

> Replace placeholders with real outputs once the sessions take place; filenames should remain identical so downstream references stay valid.
