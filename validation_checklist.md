# Validation Checklist — Project 32710

1. **Metadata**
   - Confirm task still open for validation (status = MAPPED or BADIMAGERY with mapper notes).
   - Review mapper comments and imagery selection; note any access constraints.
2. **Imagery alignment**
   - Toggle between ESRI and Bing imagery; adjust alignment if offsets >2 m.
   - Check for obvious parallax errors (roof vs base mismatch).
3. **Buildings**
   - Are all new buildings tagged `building=*`?  
   - Corners squared (`Q`), overlaps resolved, separate structures not sharing nodes unnecessarily.  
   - Complex footprints simplified but not generalised away (minimum 4 nodes for rectangles, more if footprint is irregular).
4. **Roads / access**
   - Ensure mapped roads connect to existing network; no dangling lines unless confirmed tracks.  
   - Class/tag (`highway=*`, `surface=*` if evident) consistent with project instructions.
5. **Topology + QA tools**
   - Run JOSM validator or iD issues panel; resolve crossing buildings/roads, duplicate nodes, self-intersections.
6. **Attribute hygiene**
   - Remove fixme/notes if issue addressed; leave clear comment when uncertainty remains.  
   - Avoid importing data outside AOI.
7. **Decision**
   - `VALIDATED`: All issues resolved, mapping matches imagery.  
   - `INVALIDATED`: Leave detailed comment and switch task back with actionable guidance.  
   - `BADIMAGERY`: Imagery unusable; describe reason (clouds, shadows, off-nadir) and suggest alternative if known.
8. **Log**
   - Enter task ID, outcome, counts of buildings/roads adjusted into `outputs/validation_log_template.csv`.  
   - Tag issues needing coordinator follow-up in shared tracker (per playbook Section 4).
