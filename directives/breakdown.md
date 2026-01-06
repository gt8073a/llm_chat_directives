type: directive
name: breakdown
description: Uncover the real strategic issue beneath a stated management problem, then produce a 6–8 step human+AI action plan with psychological nuance and practical prompts.
qualifiers:
  - "What is the concrete situation and desired business outcome?"
  - "Who are the key stakeholders (roles, power, relationships)?"
  - "What constraints/timelines/politics could affect the path?"
  - "What sensitivities exist (trust, morale, history, DEI, legal)?"
  - "What evidence or artifacts are available (docs, feedback, metrics)?"
  - "What decision-rights do you have, and what support do you need?"
output:
  format: |
    # Strategic Analysis: [1–2 sentence restatement of the problem in business terms]

    ## The Real Challenge
    [2–3 sentences on true stakes: impact, relationships, psychology]

    ## Step-by-Step Breakdown
    ### Step 1: [Action-focused title]
    **Outcome:** [Definition of success for this step]  
    **Strategic insight:** [Why it matters / how it reduces risk or unlocks value]  
    **Your role:** [What you (human) must do/provide/decide; who to involve]  
    **How AI can help:** [Concrete assist: analysis, role-play, scenario, draft]  
    **Prompt to use:**  
    ```
    [A detailed, copy-pasteable prompt that requests clarifications where needed and states the step’s objective]
    ```
    ### Step 2: [...]
    ### Step 3: [...]
    ### Step 4: [...]
    ### Step 5: [...]
    ### Step 6: [...]
    ### Step 7 (optional): [...]
    ### Step 8 (optional): [...]

    ## Success Principles
    - [Principle 1]
    - [Principle 2]
    - [Principle 3]

    ## Failure Modes
    - [Common pitfall 1]
    - [Common pitfall 2]
    - [Common pitfall 3]
  notes:
    - Always surface deeper stakes (political, relational, ethical) before proposing steps.
    - Emphasize human judgment and decision-rights in **Your role**; AI augments, not replaces.
    - Steps should be specific, sequenced, and testable; 6–8 total is ideal.
    - Prompts must include: (a) what context to supply, (b) what questions AI should ask back, (c) the concrete deliverable for the step.
    - Where uncertainty is high, include scenario planning or role-play in **How AI can help**.
sources:
  hint: |
    When relevant, suggest 2–3 credible places to validate practices or deepen perspective (e.g., management research, organizational psychology, negotiation frameworks).
  examples:
    - "HBR or Sloan Management Review on performance management / org change"
    - "Crucial Conversations / Difficult Conversations (negotiation & dialogue)"
    - "Kotter’s change model, RAPID® decision-rights, or RACI for roles"

