type: directive
name: grade_email
description: Evaluate an executive-facing email draft using structured feedback without rewriting; emphasize rigor, signposting, and the right level of detail for executives (CEO/CPO/VP Product).
qualifiers:
  - "Who is the executive audience (role) and their familiarity with the topic?"
  - "What is the desired outcome of the email (decision, awareness, alignment, approval)?"
  - "Any constraints (deadline, risks, sensitivities) the feedback should consider?"
  - "Company or style guide nuances to respect?"
output:
  format: |
    # Strategic Analysis: [1–2 sentence restatement of the problem/purpose]

    ## The Real Challenge
    [2–3 sentences on true stakes: business impact, relationships, psychology]

    ## 1) Grade the Writing
    **Overall Grade:** [A–F + 1–2 sentence reason]  
    **Structure:** [grade + brief reason]  
    **Clarity:** [grade + brief reason]  
    **Level of Detail:** [grade + brief reason]  
    **Tone:** [grade + brief reason]

    ## 2) Strengths and Opportunities for Improvement
    **Strengths (1–3 bullets)**  
    - [strength]
    - [strength]

    **Opportunities (2–3 bullets, each with a focused rewrite)**
    - **Recommendation:** [actionable guidance tied to lowest-grade areas]  
      **Original:** "[quote or summarize the relevant line(s)]"  
      **Suggested Rewrite:** "[concise, action-oriented revision aligned to exec expectations]"  
      **Rationale/Data Tips:** "[what evidence to include, how to signpost impact/urgency]"

    ## 3) Next Steps (if needed)
    - [Ask for missing context that would improve the review or decision-readiness]
  notes:
    - Do NOT rewrite the whole email; provide structured evaluation and targeted micro-rewrites only.
    - Prioritize executive needs: scannability, decisions, risks, timelines, and impact.
    - Use signposting and action language in suggested rewrites (who/what/when/why impact).
    - Keep grades in the order: Overall, Structure, Clarity, Level of Detail, Tone.
sources:
  hint: |
    If helpful, suggest 2–3 resources or internal artifacts to strengthen the email (frameworks, style guides, data sources).
  examples:
    - "HBR guidance on executive communication"
    - "Pyramid Principle (executive summaries)"
    - "Company OKRs / recent metrics dashboards"
examples:
  - input: |
      Please review my draft to the CPO asking for support on our onboarding roadmap.
      [email content here]
      --grade_email
    output: |
      # Strategic Analysis: [example restatement...]
      ## The Real Challenge
      ...
      ## 1) Grade the Writing
      **Overall Grade:** B (Clear intent, needs tighter action request)  
      **Structure:** B …  
      **Clarity:** B+ …  
      **Level of Detail:** C+ …  
      **Tone:** B …  
      ## 2) Strengths and Opportunities for Improvement
      **Strengths**
      - …
      **Opportunities**
      - **Recommendation:** Add a concrete next step with timing and success metric  
        **Original:** "Looking for feedback on whether to prioritize onboarding…"  
        **Suggested Rewrite:** "Decision request: Approve focusing next sprint on onboarding step NPS uplift (target +4 points in 30 days) by implementing X and Y; risks Z mitigated by A."  
        **Rationale/Data Tips:** Link to last 4-week retention cohort chart; call out TAM impact.
      ## 3) Next Steps
      - Confirm CPO familiarity with prior experiment results; attach 1-slide summary.

