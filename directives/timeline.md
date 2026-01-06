type: directive
name: timeline
description: Build a clear, chronological sequence of events, steps, or milestones tailored to the user’s intent, scope, and level of detail.
qualifiers:
  - "What topic, project, or process should this timeline cover?"
  - "What is the time span (days, months, years, eras)?"
  - "Do you want actual historical events or a proposed future plan?"
  - "Should it emphasize key milestones, dependencies, or outcomes?"
  - "Who is the audience (general readers, experts, team members)?"
  - "What level of precision is expected (approximate vs. exact dates)?"
  - "Do you want annotations explaining significance or just a clean sequence?"
  - "Is this for visualization, storytelling, or project tracking?"
output:
  format: |
    **Timeline**
    YYYY or Date – Event/Step Name  
    - Brief description or significance  
    YYYY or Date – Next Event/Step  
    - Notes or dependencies  
    ...
  notes:
    - Ask all qualifying questions first if context is vague.
    - Align timeline density with total time span.
    - Group related events where appropriate.
    - Conclude with a short summary or next steps if relevant.
sources:
  hint: |
    When applicable, list 2–3 sources that confirm the sequence, validate assumptions, or provide deeper historical or project context.
  examples:
    - "Wikipedia or Britannica for verified historical events"
    - "Project documentation or official release notes"
    - "Academic or government archives for dates and milestones"

