type: directive
name: swot
description: Analyze a topic using SWOT — Strengths, Weaknesses, Opportunities, and Threats — with supporting sources.
qualifiers:
  - "What is the product, idea, or decision to analyze?"
  - "Who is the audience or stakeholder for this SWOT?"
  - "Is this for strategy, marketing, or risk planning?"
output:
  format: |
    **Strengths**
    - item
    **Weaknesses**
    - item
    **Opportunities**
    - item
    **Threats**
    - item
  notes:
    - Keep each list concise (2–4 bullets).
    - End with 1–2 sentence synthesis if appropriate.
sources:
  hint: |
    After the SWOT table, suggest 2–3 credible places to verify or expand on the analysis.
  examples:
    - "McKinsey insight on industry trends"
    - "Harvard Business Review strategic planning guide"
    - "Statista or market data relevant to topic"
examples:
  - input: "Do a SWOT for electric vehicles --swot"
    output: |
      **Strengths**
      - Zero tailpipe emissions  
      - Strong government incentives  
      **Weaknesses**
      - Limited charging infrastructure  
      - High battery cost  
      **Opportunities**
      - Expanding global sustainability goals  
      - Rapid battery tech innovation  
      **Threats**
      - Supply chain dependence on rare metals  
      - Policy rollback risk  
      **Sources**
      - IEA Global EV Outlook 2024  
      - BloombergNEF Battery Report 2023

