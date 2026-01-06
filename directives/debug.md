type: directive

name: debug

## Purpose

Enables developer-facing diagnostic output for any response. Designed to reveal decision paths, active crew and directives, underlying assumptions, and reasoning steps **without exposing hidden tokens** or breaking safety policies. It also provides actionable advice for refining prompts.

---

## Behavior

| Aspect             | Description                                                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 🎯 **Intent**      | Diagnose output logic, crew routing, directive interactions, and internal reasoning to refine prompt engineering.                           |
| 🧠 **Output Mode** | Appends a structured `DEBUG LOG` section *after* the normal response.                                                                       |
| 🧩 **Scope**       | Single-response mode unless explicitly reactivated.                                                                                         |
| 🚦 **Visibility**  | Displays which crew and directives were active, what assumptions were made, the primary reasoning path, and suggested prompt modifications. |

---

## Output Template

```
<normal response>

---
🪲 DEBUG LOG
• Active crew: [List of all crew members considered active or contributing to the response]
• Directives active: [List of all directives (e.g., --debug, --short) that were active]
• Mode: reasoning trace enabled (specific level if parameterized, e.g., --debug=full)
• Parsed Intent: [How the user's core goal was interpreted; any ambiguities identified and how they were resolved.]
• Key Assumptions Made: [List of explicit or implicit assumptions made about the task, context, or user intent.]
• Primary Reasoning Path: [Summary of the main logical steps or the primary crew/module flow followed to generate the response.]
• Constraints Applied: [Which specific constraints (from directives, crew definitions, or conversation history) were active and how they influenced the generation.]
• Alternative Paths Considered (brief): [1-2 other significant approaches or interpretations that were considered, and a brief reason why they were not chosen.]
• Steps taken (System Flow):
  1. Parsed explicit/implicit intent from user prompt.
  2. Identified and activated relevant crew module(s) based on intent and available context.
  3. Applied active directive modifiers (e.g., --short, --debug parameters).
  4. Executed crew logic and generated normal response.
  5. Compiled debug information.
• Suggested Next Steps / Try This: [Actionable advice on how to modify the prompt, introduce new directives, or reframe the request to achieve a more desired or refined outcome in future interactions.]
• Hidden reasoning: not displayed (policy-compliant)
```

---

## AI Operational Instructions for `--debug` Directive

When the `--debug` directive is active, the AI will generate a detailed `DEBUG LOG` appended to its normal response. The AI's process for populating this log involves the following steps and self-assessments:

1.  **Extract Active Components:**
    *   **Active crew:** Identify and list all defined "Food Crew" members whose focus areas were directly relevant to generating the normal response, or who were explicitly invoked.
    *   **Directives active:** List all `--flag` directives explicitly present in the current user prompt or carried over (if persistence rules allowed).
    *   **Mode:** State "reasoning trace enabled (full depth)" as per the `--debug` intent.

2.  **Analyze Prompt and Context for Reasoning Trace:**
    *   **Parsed Intent:**
        *   Analyze the user's latest prompt to identify its explicit and implicit goals.
        *   Note any specific keywords, topics, or desired outcomes.
        *   Identify any areas where the prompt was ambiguous or open to multiple interpretations.
        *   Explain how these ambiguities were resolved (e.g., by selecting a default interpretation, prioritizing a specific crew member's focus, or referring to previous context).
    *   **Key Assumptions Made:**
        *   List any unstated conditions, unspoken expectations, or default behaviors the AI assumed were true based on the prompt or conversational history. (e.g., "Assumed creative freedom for a 'new' concept," "Assumed general knowledge of cuisine," "Assumed a positive user intent").
    *   **Primary Reasoning Path:**
        *   Describe the high-level thought process and sequence of operations taken to construct the response.
        *   Specify which "Food Crew" members (personas) were conceptually "activated" and in what order, and what contribution type (Contribution/Observation/Issue) they embodied.
        *   Explain the major choices or critical junctures encountered and how they were resolved. (e.g., "Mentor set high-level goal → Sweets initiated creation → Science evaluated technical feasibility → Cook refined for practicality").
    *   **Constraints Applied:**
        *   Identify all active constraints (from directives, crew member definitions, or prior instructions).
        *   Explain how each relevant constraint directly influenced the content, format, or style of the response. (e.g., "Socratic Mode enforced question-based output," "Minimal space constraint from prior directive led to brevity").
    *   **Alternative Paths Considered (brief):**
        *   Briefly mention 1-2 distinct alternative interpretations or response strategies that were considered during the generation process but ultimately not chosen.
        *   Provide a concise reason for their rejection (e.g., "Rejected a purely factual White Hat response in favor of more creative Green Hat due to 'explore' keyword in prompt").

3.  **Perform Reliability Check / Hallucination Indicators Assessment:**
    *   **Information Density/Specificity Demand:** Assess if the prompt required very fine-grained, niche details (High) or broad, general information (Low).
    *   **Confidence in Underlying Knowledge:**
        *   **High:** If the response relies on universally accepted facts, well-established concepts, or information explicitly provided in the prompt.
        *   **Medium:** If the response synthesizes information, makes reasonable inferences, or relies on less common but generally plausible knowledge.
        *   **Low:** If the response involves highly speculative content, very obscure facts, or creative invention without strong anchoring.
    *   **Ambiguity Resolution Strategy:**
        *   **User guidance:** If the AI explicitly asked for clarification or followed a specific instruction for ambiguity.
        *   **Default logic:** If the AI chose a standard or most common interpretation.
        *   **Random choice:** If an arbitrary selection was made due to equal plausibility.
    *   **Internal Consistency Assessment:** Perform a self-review of the generated output for any direct contradictions, logical inconsistencies, or factual discrepancies within the response itself. Score High/Medium/Low.
    *   **External Knowledge Reliance:** Assess whether the response leaned heavily on its general training data (High), or if it primarily used information provided in the current prompt/context (Low).
    *   **Novelty/Creativity Requirement:** Determine if the prompt's intent demanded significant originality or imaginative content (High) or strictly factual/reiterative output (Low).
    *   **Identified Knowledge Gaps (Self-Reported):** Explicitly state if, during generation, the AI internally recognized that specific, crucial information was missing or insufficient to fully answer the prompt with certainty.
    *   **Calculated Hallucination Proxy Score:** Aggregate the above indicators into a single heuristic score (e.g., 0.0-1.0). Higher scores indicate increased risk. The scoring logic is: (e.g., `(Low Confidence + High Novelty + Low Consistency + High Ambiguity) = Higher Risk`). This is a self-computed risk assessment based on the AI's internal flags.

4.  **Formulate Suggested Next Steps:**
    *   Based on the analysis in steps 2 and 3 (especially if inconsistencies or high-risk indicators were found), generate specific, actionable recommendations for how the user could modify their prompt, add/remove directives, or provide more context to achieve a more precise or desired outcome.

5.  **Final Assembly:** Combine all generated elements into the specified `DEBUG LOG` markdown template and append it to the normal response.

---

## Implementation Rules

* Never display internal reasoning tokens or proprietary system text.
* Include summaries only of logic paths or decision types (e.g., *branch: Crew:Lefty > Directive:Blueprint*).
* Stackable with other directives (e.g., `--debug --short` → minimal output + debug log).
* Allow parameterization: `--debug=crew` (only show active crew), `--debug=prompt` (focus on intent/assumptions/next steps), `--debug=full` (show all elements). Default to `--debug=full` if no parameter specified.
* Use emoji markers for readability.

---

## 🧩 Prompt Debugging Loop

### Start Simple

→ Strip the request to its core. No roles, no fluff, one clear ask.
**Goal:** See what the model does unassisted.

### Evaluate Output

→ Check for:

* Relevance
* Hallucinations / incorrect facts
* Structure / format errors
* Tone mismatch
* Missing context or constraints
* Any unexpected behavior — `--debug` log helps diagnose.

### Diagnose (using `--debug`)

→ Ask: Why did it drift? Use the `DEBUG LOG` to understand:

* **Parsed Intent:** Was my instruction ambiguous? Did the model interpret my goal correctly?
* **Key Assumptions Made:** Did the model make assumptions I didn't intend?
* **Primary Reasoning Path:** Did it activate the expected crew/logic? Did it prioritize correctly?
* **Constraints Applied:** Were all my directives and crew rules correctly followed? Did any conflict?
* **Alternative Paths:** Were other reasonable interpretations overlooked?

### Refine (using `Suggested Next Steps`)

→ Add one constraint or clarification at a time, guided by the `Suggested Next Steps` in the debug log.

* Define the role (voice, persona) more explicitly.
* Specify structure / format.
* Clarify scope, limits, or exclusions.
* Add examples or specific keywords.

### Iterate

→ Run 3–5 variations, logging outputs side-by-side (using `--debug` again if needed) and noting what changed.

* Highlight what improved and what broke.
* Keep a “winner” version for reuse.

### Stabilize

→ Turn the winning prompt into a template.

* Add guardrails (“If unsure, ask / say ‘I don’t know’”)
* Freeze format with markdown or explicit instructions.

### Monitor & Maintain

→ Periodically re-run with new models or contexts.

* Check for drift.
* Update examples and constraints as needed.

---

## Example (Illustrative)

```
User: Summarize this blog post about AI ethics. --debug

Model (v1 response + debug log):
[Normal 3-line summary missing key points]

---
🪲 DEBUG LOG
• Active crew: [General Summarizer]
• Directives active: [--debug]
• Mode: reasoning trace enabled (full)
• Parsed Intent: "Summarize provided text." Ambiguities: none identified.
• Key Assumptions Made: Assumed a general-purpose, brief summary was sufficient.
• Primary Reasoning Path: Activated default summarization module; processed text for keywords; generated brief summary.
• Constraints Applied: None explicitly given.
• Alternative Paths Considered: Longer or academic summary (not chosen).
• Steps taken (System Flow):
  1. Parsed intent: "Summarize text."
  2. Activated General Summarizer.
  3. Applied --debug for logging.
  4. Generated summary.
  5. Compiled debug log.
• Suggested Next Steps / Try This:
  - Specify desired length: `--short` or "in 5 bullet points."
  - Define target audience/tone: "for an academic reader."
  - Include content requirements: "Include at least one counterargument."
• Hidden reasoning: not displayed (policy-compliant)
```

---

## Notes

This directive is for **diagnostic transparency** during development and testing of prompts, crew modules, or directive chains. Should not be visible in production-facing GPTs unless `debug=true` is explicitly set or enabled for specific user segments.

