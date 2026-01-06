# Directives

Directives are **small, composable flags** you append to a prompt to control **how** an AI responds — not **what** it responds with.

Think of them as **behavior modifiers**, not instructions or prompts themselves.

---

## What is a Directive?

A directive is a short flag (like `--short` or `--assist`) that tells the assistant *how to behave* for **this message only**.

Examples:

* Be brief
* Be analytical
* Be calm and professional
* Give multiple examples
* Focus on next actions

They do **not** change the question.
They change the **style, depth, structure, and intent** of the answer.

---

## Grandma Explanation

Directives are polite sticky notes that say *how* you want help, not *what* you want help with.

“Explain this recipe”
vs
“Explain this recipe `--short`”

Same question. Different delivery.

---

## Basic Usage

Append one or more directives to the end of your message:

* Explain vector databases `--short`
* Help me plan this project `--assist`
* Give me ideas for a birthday gift `--3samples`

Directives apply **only to that message** unless otherwise specified.

---

## Core Principles

* **Scoped** – Apply to one message unless stated
* **Behavioral** – Affect tone, structure, and reasoning
* **Non-invasive** – Don’t rewrite or override the question
* **Human-legible** – Should make sense to a non-technical reader

---

## What Directives Are Not

Directives are **not**:

* Prompts
* Personas
* System instructions
* Memory
* Tools

They don’t add knowledge.
They shape **delivery and reasoning**.

---

## Example Directives

| Directive    | What it does                         |
| ------------ | ------------------------------------ |
| `--short`    | Minimal response, no fluff           |
| `--assist`   | Calm, high-IQ professional assistant |
| `--Xsamples` | Return X varied examples             |
| `--proscons` | Structured trade-off analysis        |
| `--debug`    | Step-by-step fault isolation         |
| `--outline`  | Clear hierarchical structure         |

(See individual directive files for exact behavior.)

---

## File Structure

Directives/

* short.md
* assist.md
* outline.md
* proscons.md
* debug.md
* README.md

Each directive lives in its own `.md` file and defines:

* Purpose
* Behavioral rules
* Tone
* Output format
* Edge cases

---

## Loading & Caching (Optional)

Some systems support **lazy-loading** directives:

* First use → fetch from repo
* Later uses → cached for the session

If a directive is missing:

`(directive --name not found, continuing)`

Execution should **never fail** because of a missing directive.

---

## Design Philosophy

* **Explicit over implicit**
* **Small over clever**
* **Behavior over verbosity**
* **Grandma-understandable**

If a directive can’t be explained in one sentence, it’s probably too big.

---

## Contributing

New directives should:

1. Do one thing well
2. Be understandable 
3. Avoid overlapping responsibilities
4. Define tone and structure clearly

---

## License

MIT — steal freely, improve loudly.

