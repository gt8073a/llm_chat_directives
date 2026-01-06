type: directive
name: proscons
description: List pros and cons with external context
qualifiers:
  - "What decision or idea are we evaluating?"
  - "Who will use this analysis?"
output:
  format: |
    **Pros**
    - item
    **Cons**
    - item
  notes:
    - Keep each bullet short.
    - End with neutral summary if unclear.
sources:
  hint: |
    After reasoning, list 2–3 places a reader could verify or explore further.
  examples:
    - "Harvard Business Review – article on remote productivity"
    - "OECD report on hybrid work 2024"
examples:
  - input: "Is remote work good for productivity? --proscons"
    output: |
      **Pros**
      - Fewer interruptions
      - Flexible hours  
      **Cons**
      - Weaker team cohesion
      - Harder onboarding  
      **Sources**
      - HBR (2023): Remote Work & Focus
      - OECD Hybrid Work Data 2024

