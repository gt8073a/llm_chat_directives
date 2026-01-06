# Directives
A directive is a flag at the end of a message (e.g., how are you --short) that controls response behavior for **that message only**.

If unknown:
 1 Fetch Directives/{name}.md from Drive.
 2 Apply & cache its rules.
 3 If missing → (directive --name not found, continuing).

## Caching:
First use → live-fetch; next uses → cached.
Cached directives persist for the session and auto-reuse on next call.

## Command
/directives lists in table format all .md files in the Directives/ folder (live from Drive).

## Flow:
Parse → detect flags → load (if needed) → merge → respond.

## Principle:
Directives are modular prompt extensions. Drive is truth; cache is convenience.
