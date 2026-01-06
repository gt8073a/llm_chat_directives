type: directive
name: blueprint
description: Create a clear, step-by-step implementation plan or system design that turns an idea, problem, or goal into a concrete sequence of actions and decisions.
qualifiers:
  - "What is the core goal or problem we’re solving?"
  - "Who are the key stakeholders or users affected?"
  - "What resources, constraints, or dependencies exist?"
  - "What’s the expected timeline or urgency for delivery?"
  - "What does success look like—what measurable outcome or impact?"
  - "Should this blueprint emphasize execution (how) or strategy (why)?"
output:
  format: |
    # Blueprint: [Title or Objective]

    ## Goal
    [1–2 sentences summarizing the desired outcome.]

    ## Strategic Context
    [Why this matters; key drivers, constraints, or success criteria.]

    ## Step-by-Step Plan
    1. **Step Title** — [Objective or deliverable for this step]  
       *Details / tasks / owners / dependencies / metrics*
    2. **Step Title** — [...]
    3. **Step Title** — [...]

    ## Key Risks & Mitigations
    - Risk: [description] → Mitigation: [solution]
    - Risk: [description] → Mitigation: [solution]

    ## Success Metrics
    - [Metric 1: definition + target]
    - [Metric 2: definition + target]

    ## Recommended Next Steps
    - [Immediate next action]
    - [Who should do what and by when]
  notes:
    - Ask all qualifiers first if context is ambiguous.
    - Keep each step action-oriented and outcome-driven.
    - Balance vision (why) with execution (how).
    - Use concise language; focus on clarity and accountability.
sources:
  hint: |
    Include 2–3 resources, playbooks, or frameworks relevant to planning or delivery.
  examples:
    - "McKinsey 7S, OKRs, or RACI models for execution alignment"
    - "HBR or Bain guides on strategic planning and project roadmaps"
    - "PMI or Agile frameworks for milestone structure"

