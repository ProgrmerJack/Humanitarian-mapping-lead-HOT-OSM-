# Humanitarian Mapping — Uzbekistan (HOT / OSM)

Welcome to the Humanitarian Mapping Lead repository for Uzbekistan. This project supports humanitarian and resilience efforts by coordinating, creating, and validating OpenStreetMap (OSM) data for Uzbekistan. The repository collects guidance, processes, and resources for mappers, validators, and project leads working with the Humanitarian OpenStreetMap Team (HOT) methodologies in Uzbekistan.

> NOTE: This README provides guidance to contributors and project leads. If you're here to start mapping, read the "Quick start" and "Mapping workflow" sections first.

Table of contents
- Project overview
- Objectives & scope
- Who should use this repo
- Quick start (for new mappers)
- Mapping workflow (high level)
- Tools & setup
- Data model & tagging guidance
- Imagery, data sources & licensing
- Tasking Manager & task lifecycle
- QA & validation checklist
- Exporting and using OSM data
- Contribution guidelines
- Code of conduct
- Contacts & acknowledgements
- Roadmap & next steps
- Useful links & references

## Project overview
---------------
This project centralizes mapping guidance and coordination for humanitarian mapping efforts in Uzbekistan. It is intended for:
- HOT/OSM mapping leads and coordinators
- Remote volunteers and local mappers
- Validators and GIS analysts preparing datasets for humanitarian response or development
- Trainers running mapping workshops in-country

The repository should contain (or link to) project-specific mapping guides, tasking manager projects, validation rules, export instructions, and any scripts/templates used to process or analyze OSM data.

## Objectives & scope
------------------
Primary objectives:
- Produce high-quality OSM baseline datasets for priority humanitarian use cases (shelter, population estimation, critical infrastructure, road accessibility, public services).
- Support rapid mapping and validation workflows (Tasking Manager → remote mapping → validation → export).
- Provide clear, consistent tagging and mapping guidance aligned with HOT and OSM best practices and local context.
- Train and support local mappers and volunteers.

Geographic scope:
- The official scope for mapping tasks will be defined per Tasking Manager project(s). This repo focuses on Uzbekistan at national and sub-national levels (as specified in project metadata).

## Who should use this repo
------------------------
- New mappers looking for step-by-step instructions.
- Experienced mappers seeking project-specific tagging and validation rules.
- Validators who need checklists and QA criteria.
- Project leads coordinating tasking manager projects, imagery procurement, and local partnerships.

## Quick start (for new mappers)
-----------------------------
1. Sign up for an OpenStreetMap account: https://www.openstreetmap.org
2. Get familiar with the map editors:
   - Web editor iD: https://www.openstreetmap.org/edit
   - JOSM (desktop advanced editor): https://josm.openstreetmap.de
   - RapiD (AI-assisted editor): https://improve.openstreetmap.org/ (or via Tasking Manager)
3. Join the project communication channel (Slack/Telegram/Matrix) — check Contacts below.
4. Find a Tasking Manager project for Uzbekistan (linked in this repo or in project metadata) and claim a task.
5. Follow the task instructions and the project-specific tagging guide in this repo.
6. When finished, mark the task as "mapped" and request validation according to the project workflow.

## Mapping workflow (high level)
-----------------------------
1. Project setup (lead): Define objectives, AOI, priority features, imagery, and tagging rules. Create Tasking Manager project.
2. Remote mapping: Volunteers trace buildings, roads, POIs, landuse and other features per mapping instructions.
3. Validation: Trained validators review mapped tasks, flag errors, and mark tasks as validated.
4. Export & analysis: After validation, exports (e.g., .osm, .shp, GeoJSON) are produced for humanitarian partners.
5. Maintenance: Ongoing updates and local engagement to keep data current.

## Tools & setup
-------------
Editors:
- iD: simple in-browser editing, good for beginners.
- JOSM: powerful desktop editor, required for complex edits, validators, and bulk changes. Recommended plugins: ImageryOffsets, BuildingTools, UtilsPlugin2.
- RapiD: integrates machine learning suggestions — useful for increasing productivity but still requires human review.

Utilities:
- HOT Tasking Manager: https://tasks.hotosm.org — for tasking and workflow management.
- OSM website: https://www.openstreetmap.org
- Overpass Turbo: https://overpass-turbo.eu — query OSM data.
- QGIS: https://qgis.org — analyze and visualize OSM exports.
- osmosis / osmium-tool: for processing large OSM files.
- OSMCha / osm-check-changeset: for monitoring changes and quality.

## Data model & tagging guidance
-----------------------------
Use standard OSM tags wherever possible. Project-specific conventions (examples):
- Buildings: `building=yes` or specific type `building=house`, `building=commercial`, `building=apartments`.
- Residential address mapping: `addr:housenumber`, `addr:street`, `addr:city` (only if data is reliable and allowed).
- Roads: map geometry and set `highway=` values (`residential`, `secondary`, `primary`, `service`, etc.). Add `surface=` where known and `oneway=yes` if applicable.
- Public services: `amenity=school`, `amenity=hospital`, `amenity=police`, `amenity=place_of_worship`, etc.
- Health facilities: include `healthcare=*` tags and `operator=*`/`name=*` when available.
- Shops & markets: `shop=*`, `marketplace` or `amenity=marketplace`.
- Water & sanitation: `waterway=*`, `drainage`, `toilets=`, `amenity=toilets`.
- Landuse: `landuse=residential`, `landuse=forest`, `landuse=industrial`, etc.

Always consult the OSM wiki and HOT mapping guidance for tag selection:
- HOT Mapping Guidelines: https://wiki.hotosm.org/
- OSM Wiki: https://wiki.openstreetmap.org/

## Imagery, data sources & licensing
--------------------------------
Imagery:
- Project Tasking Manager metadata will state the imagery source and any offset issues.
- Common imagery providers include Bing, Maxar/Worldview (via HOT agreements), Mapbox, and others.
- If imagery has known offsets, follow the offset instructions in Tasking Manager or project README.

Data sources:
- Official government datasets (use only where licensing allows editing OSM).
- Crowd-sourced datasets, local surveys (with permission).
- Avoid copying proprietary data into OSM unless the license explicitly allows it and it is documented.

Licensing:
- Contributions to OSM are licensed under the ODbL (Open Database License). Ensure any derived or uploaded data is compatible with OSM licensing.
- Do not import data that would violate copyright or the project's license agreements.

## Tasking Manager & task lifecycle
-------------------------------
- Projects are created in HOT Tasking Manager. The task lifecycle typically has statuses: Ready → Mapped → Validated.
- Roles:
  - Mapper: traces features and marks tasks as mapped.
  - Validator: reviews tasks and marks as validated.
  - Project Lead: sets project boundaries, tagging rules, provides imagery notes, and monitors progress.

When creating tasks, include:
- Clear brief and priority features.
- Mapping instructions (what to map, what to ignore).
- Validation guidance and examples of good/bad mapping.

## QA & validation checklist
-------------------------
Validators should check mapped tasks against a checklist:
- Completeness: Are all priority features mapped within the task area?
- Accuracy: Do geometries align with imagery and local knowledge?
- Duplicates: No duplicated buildings, roads, or POIs.
- Topology: Roads connect appropriately, buildings don’t overlap incorrectly.
- Tagging: Features use correct tags and attributes.
- Imagery offset: Are mapped features aligned with reference imagery or is an offset applied?
- Logical attributes: Building types, highway types, amenities make sense for the area.

Example quick validation checklist:
1. Are all buildings traced and roof shapes reasonable?
2. Are roads present and classified? Are service roads mapped as `service`?
3. Are critical POIs (hospitals, schools) present and correctly tagged?
4. Are there any obvious mis-traces (trees traced as buildings, etc.)?
5. Does the task use local naming or address information only when verified?

## Exporting and using OSM data
---------------------------
After validation:
- Use Tasking Manager exports or Overpass to extract AOI data.
- Convert exports to shapefiles or GeoJSON for partner consumption using osmium-tool or OGR.
- Document coordinate reference system and ensure metadata accompanies datasets.
- Note licensing: data derived from OSM inherits ODbL; provide attribution as required.

## Contribution guidelines
-----------------------
- All contributions should follow the project's mapping guidance.
- For repo contributions (scripts, docs): fork → branch → pull request with a clear description.
- Provide references for any external data or methodologies used.
- When making mapping edits in OSM, include descriptive changeset comments referencing the project (e.g., "Mapped buildings for HOT Uzbekistan project: task #12345").

## Code of conduct
---------------
We follow a respectful, inclusive code of conduct. Be professional, constructive, and mindful of local communities' sensitivities. Harassment or abusive behavior is not tolerated.

## Contacts & acknowledgements
---------------------------
- Project lead / maintainer: (provide contact info here - email/telegram/slack)
- HOT: https://www.hotosm.org
- OSM community volunteers and local partners in Uzbekistan

If you want to add local contacts or partner NGOs, include them in the CONTRIBUTORS or CONTACTS file.

## Roadmap & next steps
--------------------
Planned items:
- Populate this repo with project-specific tasking manager links, stylesheets, validation rules, and example exports.
- Add training slides, recorded workshops, and onboarding materials for new mappers.
- Create automated QA scripts and Overpass queries for frequent checks.

## Useful links & references
-------------------------
- HOT Tasking Manager: https://tasks.hotosm.org
- HOT Wiki & Mapping Guidelines: https://wiki.hotosm.org
- OSM Wiki (Mapping standards): https://wiki.openstreetmap.org
- JOSM editor: https://josm.openstreetmap.de
- RapiD editor: https://improve.openstreetmap.org
- Overpass Turbo: https://overpass-turbo.eu
- QGIS: https://qgis.org

## License
-------
This repository is documentation and coordination material. The README and other repo files should be licensed permissively (for example, CC-BY-4.0) unless specified otherwise. Data produced and uploaded to OSM will be governed by ODbL.

## Appendix: Add project-specific files
------------------------------------
To make this repo actionable, consider adding:
- TASKING_MANAGER_PROJECTS.md — list of active projects and links
- VALIDATION_CHECKLIST.md — detailed validator checklist and screenshots
- TAGGING_GUIDE.md — project-specific tag exceptions and examples
- TRAINING/ — folder containing slides, videos, and exercises
- CONTACTS.md — up-to-date list of local leads and communication channels
