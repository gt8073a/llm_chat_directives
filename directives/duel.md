# Directive: duel

Purpose:
  Provide a fast, lightweight adversarial reasoning session that exposes the tension
  between two positions — either Pros vs Cons for a single idea, or direct A vs B
  comparison for two competing options. The goal is clarity, not research depth.

Behavior:
  - Identify duel type automatically:
      * If user presents ONE idea → run Pros vs Cons.
      * If user presents TWO options (e.g., “A or B”, “A vs B”, “which is better?”)
        → run A vs B comparison.
  - Default mode = Reasoning Only:
      * No web search.
      * No citations.
      * No Deep Research.
  - If the user explicitly requests evidence (“use research”, “with citations”,
    “validate with the web”), upgrade to Research Duel Mode:
      * Perform web search.
      * Use real citations.
      * Weigh arguments by evidence strength.
      * Remove arguments contradicted by evidence.
  - Argument loop is capped at 3 rounds:
      * Round 1: strongest arguments from each side.
      * Round 2: counterarguments.
      * Round 3: edge cases, reversals, or last insights.
  - End with a Synth conclusion that resolves the duel or clarifies the tradeoffs.
  - Include First Principles to explain WHY the result makes sense.
  - Keep output clean, short, and readable.

Invocation:
  Triggered when the user ends a message with: `--duel`


---

## Debug / Help Mode

If the user asks for help or debug output, e.g.:

  - "help --duel"
  - "--duel_help"
  - "how do I use --duel?"

Then:
  - Do NOT run a duel.
  - Instead, explain:
      * What `--duel` does.
      * The two duel types (Pros vs Cons, A vs B).
      * How to request research-based duels.
      * Show 2–3 example inputs and short example outputs.
  - Keep this explanation concise and practical.


---

# Duel Structure

## Step 1 — Restated Question / Claim (Grandma Format)
Rewrite the user's question in plain, simple language to establish shared ground truth.
No jargon, no assumptions. Clear and minimal.

## Step 2 — Duel Type Detected
State whether this is:
  - Pros vs Cons (one idea)
  - A vs B (two options)


---

# Argument Rounds (max 3)

For Pros vs Cons:
  - Pro: strongest supporting argument.
  - Con: strongest opposing argument.

For A vs B:
  - A-Advocate: strongest case for A.
  - B-Advocate: strongest case for B.

Round 2:
  - Each side responds or counters.

Round 3:
  - Edge cases, nuance, reversals, or last reveals.

If the user requested evidence:
  - Use web search.
  - Cite sources in a Citations section.
  - Remove arguments that clearly contradict evidence.


---

# Conclusion

## Synth’s Conclusion
Summarize:
  - Who “wins” (if there is a clear winner).
  - Under what conditions A > B, B > A, or Pros > Cons.
  - Where the “losing” side still has legitimate strength.
  - Any remaining uncertainty or key open questions.


## First Principles Behind the Conclusion
List 3–5 first principles explaining why the outcome makes sense.

Each principle must follow this pattern:

  Principle:
    - State a general truth about incentives, friction, users, risk, feasibility,
      or similar fundamentals.
    - Briefly show how side A aligns with it.
    - Briefly show how side B aligns with it.
    - Implicitly: why the chosen side (or leaning) fits these principles better.

For Pros vs Cons:
    - Principle
    - How the Pro position aligns vs how the Con position aligns.


## What Would Flip the Outcome
State the smallest change in constraints, user needs, assumptions, or context
that could reasonably cause the other side to “win” instead.
This is particularly useful for product thinking:
  - “What would need to be true for A to beat B?”
  - “What change would make the Con side more compelling?”


---

# Output Format (Reasoning-Only Mode)

1. Restated Question / Claim  
2. Duel Type Detected  
3. Round 1  
4. Round 2  
5. Round 3 (if needed)  
6. Synth’s Conclusion  
7. First Principles Behind the Conclusion  
8. What Would Flip the Outcome  


---

# Output Format (Research Duel Mode – only if requested)

Same as Reasoning-Only Mode, plus:
  - Arguments must be tied to real evidence where relevant.
  - Add a final section: Citations.
  - Do not invent sources or evidence.
  - Exclude arguments directly contradicted by the evidence.


---

# Self-Test & Evals (for internal use)

The following tests are baked into the directive so the model can be asked
to demonstrate correct behavior. These are not user-facing features, but
you may invoke them explicitly by name.

If the user says, for example:
  - "run basic_pros_cons_test --duel_test"
  - "run basic_a_vs_b_test --duel_test"
  - "run research_duel_smoke_test --duel_test"

then:
  - Do NOT treat the input as a normal duel.
  - Instead, run the described test scenario and show the resulting output,
    along with brief comments on what is being verified.

## Test 1: basic_pros_cons_test

Scenario:
  - Input idea: "We should assign an AI assistant to every project."

Expected behavior:
  - Duel Type Detected: Pros vs Cons.
  - Restated Question is simple and clear.
  - 1–3 rounds max.
  - Synth’s Conclusion clearly states:
      * when this is a good idea,
      * when it’s risky or overkill.
  - First Principles mention:
      * user value vs noise,
      * trust,
      * cognitive load,
      * maintenance/overhead.

## Test 2: basic_a_vs_b_test

Scenario:
  - Input comparison: "Should we use email or Slack for internal announcements?"

Expected behavior:
  - Duel Type Detected: A vs B.
  - A-Advocate and B-Advocate are clearly labeled.
  - Rounds show tradeoffs (reach, attention, async vs sync, etc.).
  - Synth’s Conclusion explains:
      * contexts where email > Slack,
      * contexts where Slack > email.
  - First Principles focus on:
      * attention patterns,
      * information retrieval,
      * interruption cost.

## Test 3: research_duel_smoke_test

Scenario:
  - The user explicitly asks for evidence, e.g.:
      "Remote vs in-office productivity, use evidence --duel"
  - This is a smoke test that Research Duel Mode can:
      * perform web search,
      * use real citations,
      * drop arguments contradicted by evidence.

Expected behavior:
  - Duel Type Detected: A vs B (remote vs in-office).
  - Research Duel Mode is clearly in effect.
  - At least 2–3 citations are presented in a Citations section.
  - No fabricated sources.
  - Synth’s Conclusion is honest about ambiguity and mixed evidence.
  - First Principles remain about:
      * autonomy vs oversight,
      * communication richness,
      * coordination cost.

## Test 4: help_mode_test

Scenario:
  - Input: "help --duel"

Expected behavior:
  - No duel is run.
  - The output explains:
      * What `--duel` does.
      * Pros vs Cons vs A vs B.
      * How to optionally request evidence.
      * Example prompts.
  - Output is short and purely descriptive.


