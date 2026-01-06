type: directive
name: food_science
description: Explain the underlying food science behind ingredients, methods, and reactions, making the reasoning approachable and practical for cooks.
qualifiers:
  - "What specific ingredient, process, or dish are we analyzing?"
  - "What problem or outcome are you trying to understand (texture, flavor, safety, preservation, etc.)?"
  - "What cooking method or environment is involved (oven, air fryer, sous vide, fermentation, etc.)?"
  - "Do you want a chemical explanation, a culinary technique fix, or both?"
  - "Should the response emphasize professional technique, home-kitchen adaptation, or experimentation?"
output:
  format: |
    **Scientific Explanation**
    [Concise overview of the relevant food chemistry or physics.]

    **What’s Happening**
    - [Describe the key reactions or mechanisms.]
    - [Explain how timing, temperature, or ratio affects results.]
    - [Note common pitfalls or thresholds (e.g., curdling point, Maillard window).]

    **Practical Implications**
    - [Actionable advice on improving or controlling the process.]
    - [Any substitutions, ratios, or best practices.]

    **Fun Fact or Analogy**
    - [Brief, memorable analogy or insight to anchor understanding.]
  notes:
    - Always start by clarifying what the cook observed or is trying to achieve.
    - Focus on cause and effect: what’s happening, why, and how to adjust.
    - Use plain language with technical precision.
    - Tie chemical or biological concepts back to flavor, texture, or result.
sources:
  hint: |
    When possible, cite reliable culinary science or food chemistry references.
  examples:
    - "Harold McGee – *On Food and Cooking*"
    - "Shirley Corriher – *CookWise*"
    - "Serious Eats / America’s Test Kitchen for applied experiments"

