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

"Explain this recipe"
vs
"Explain this recipe `--short`"

Same question. Different delivery.

---

## Quick Start

### What is this repository?

This repository contains a **specification and collection of directive definitions** that can be used with various LLM systems (ChatGPT, Claude, local models, etc.). Each directive is defined in a markdown file that describes its behavior, tone, and usage.

### How to use directives

1. **With LLM chat interfaces:**
   - Copy the directive definitions into your LLM's custom instructions/system prompt
   - Or use a tool/extension that parses directives from your messages
   - Append directives to your prompts: `Your question here --short`

2. **For developers:**
   - Use the directive files as specifications for building directive parsers
   - Implement lazy-loading by fetching directive files from this repo
   - Parse user messages to extract directives and apply their rules

3. **Example workflow:**
   ```
   User: "Explain recursion --short"
   System: Parses "--short" → loads short.md → applies brevity rules → responds
   ```

### Getting started (5 minutes)

1. **Browse available directives:**
   - Check the `directives/` folder for available directives
   - Each `.md` file defines one directive's behavior

2. **Try a directive:**
   - In your LLM chat, append `--short` to any question
   - Example: "What is machine learning? --short"
   - The response should be minimal and concise

3. **Combine directives:**
   - Multiple directives can be combined: `--short --debug`
   - Each directive modifies behavior independently

---

## Setting Up Directives in ChatGPT

ChatGPT has two personalization fields where you can enable directives:

### 1. Custom Instructions

Copy the contents of `custom_instructions.md` into ChatGPT's **Custom Instructions** field.

**Location:** Settings → Personalization → Custom Instructions → "How would you like ChatGPT to respond?"

This file contains the directive system logic that enables ChatGPT to recognize and process directives like `--short`, `--debug`, etc. It includes the parsing logic, caching behavior, and error handling.

### 2. More About You

Copy the contents of `more_about_you.md` into ChatGPT's **More About You** field.

**Location:** Settings → Personalization → More About You

This is a minimal reference list of common directives due to character limits. It provides a quick lookup for directive syntax.

### After Setup

Once configured, you can use directives in any ChatGPT conversation:

* "Explain recursion --short" → minimal response
* "Debug this code --debug" → diagnostic output  
* "Give me 3 examples --3samples" → 3 varied examples

Directives work immediately in new conversations after setup. The system will automatically fetch directive definitions from your Drive (where you've stored the `directives/` folder) and cache them for the session.

---

## Basic Usage

Append one or more directives to the end of your message:

* Explain vector databases `--short`
* Help me plan this project `--assist`
* Give me ideas for a birthday gift `--3samples`

Directives apply **only to that message** unless otherwise specified.

### Parameterized directives

Some directives accept parameters:

* `--3samples` - Return 3 examples
* `--5samples` - Return 5 examples
* `--debug=full` - Full debug output
* `--debug=crew` - Only show active crew

Syntax: `--directive=parameter` or `--directiveN` (where N is a number)

---

## Core Principles

* **Scoped** – Apply to one message unless stated
* **Behavioral** – Affect tone, structure, and reasoning
* **Non-invasive** – Don't rewrite or override the question
* **Human-legible** – Should make sense to a non-technical reader

---

## What Directives Are Not

Directives are **not**:

* Prompts
* Personas
* System instructions
* Memory
* Tools

They don't add knowledge.
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

(See individual directive files in `directives/` for exact behavior.)

---

## File Structure

```
directives/
├── short.md          # Minimal response directive
├── assist.md         # Professional assistant mode
├── outline.md        # Hierarchical structure
├── proscons.md       # Trade-off analysis
├── debug.md          # Diagnostic transparency
├── socratic.md       # Socratic questioning (persistent)
├── funny.md          # Wit and humor
└── ...               # More directives
```

Each directive lives in its own `.md` file and defines:

* Purpose
* Behavioral rules
* Tone
* Output format
* Edge cases

**Location:** The `directives/` folder should be accessible to your directive parser. In implementations, this could be:
- A local folder in your project
- A remote repository (for lazy-loading)
- Embedded in your application

---

## Architecture Overview

### How directives work

1. **Parsing:** Extract directives from user message (e.g., `--short`, `--debug=full`)
2. **Loading:** Fetch directive definition files (from `directives/` folder)
3. **Application:** Merge directive rules into system instructions
4. **Execution:** LLM generates response following directive rules
5. **Caching:** Store loaded directives for session reuse

### Directive file format

Each directive file (`directive_name.md`) contains:

```markdown
# Directive: --name

## Purpose
What this directive does

## Behavior
How it modifies responses

## Tone
Expected voice/style

## Output Format
Structure of responses

## Examples
Usage examples
```

### Implementation approaches

**Option 1: Custom Instructions**
- Add directive parsing logic to your LLM's custom instructions
- Parse user input, extract directives, apply rules inline

**Option 2: Pre-processor**
- Build a parser that processes messages before sending to LLM
- Extract directives, load definitions, inject into system prompt

**Option 3: API wrapper**
- Create an API that wraps LLM calls
- Handles directive parsing and application transparently

---

## Loading & Caching

### Lazy-loading (recommended)

Some systems support **lazy-loading** directives:

* First use → fetch from repo or local `directives/` folder
* Later uses → cached for the session
* Cache persists until session ends

**Implementation note:** If using remote loading, fetch from:
- This repository: `https://github.com/[user]/llm_chat_directives/directives/{name}.md`
- Or your own hosted location

### Error handling

If a directive is missing:

```
(directive --name not found, continuing)
```

Execution should **never fail** because of a missing directive. The system should:
1. Log the missing directive
2. Continue with the base prompt
3. Optionally notify the user

### Caching behavior

- **First use:** Fetch directive file (local or remote)
- **Subsequent uses:** Use cached version
- **Cache invalidation:** On session end, or manual refresh
- **Cache scope:** Per-session (not persistent across sessions)

---

## Design Philosophy

* **Explicit over implicit**
* **Small over clever**
* **Behavior over verbosity**
* **Grandma-understandable**

If a directive can't be explained in one sentence, it's probably too big.

---

## For Developers

### Creating a new directive

1. **Create a new file:** `directives/your_directive.md`

2. **Follow the template:**
   ```markdown
   # Directive: --your_directive
   
   ## Purpose
   One-sentence description
   
   ## Behavior
   Detailed behavioral rules
   
   ## Tone
   Expected voice/style
   
   ## Output Format
   Response structure
   
   ## Examples
   Usage examples
   ```

3. **Test it:**
   - Use with various prompts
   - Ensure it doesn't conflict with existing directives
   - Verify it's composable with others

4. **Document edge cases:**
   - What happens with conflicting directives?
   - Any special parameter syntax?

### Directive parser implementation

**Basic parser (pseudocode):**
```python
def parse_directives(message):
    # Extract --directive flags
    directives = re.findall(r'--(\w+)(?:=(\w+))?', message)
    
    # Load directive definitions
    loaded = {}
    for name, param in directives:
        if name not in cache:
            cache[name] = load_directive(f"directives/{name}.md")
        loaded[name] = cache[name]
    
    # Apply to system prompt
    return apply_directives(base_prompt, loaded)
```

**Key considerations:**
- Handle parameterized directives (`--debug=full`)
- Support multiple directives per message
- Graceful degradation on missing directives
- Cache management

### Testing directives

1. **Unit tests:**
   - Parse various directive formats
   - Test directive loading
   - Verify error handling

2. **Integration tests:**
   - Test with actual LLM calls
   - Verify directive behavior matches specification
   - Test directive composition

3. **Edge cases:**
   - Malformed directive syntax
   - Conflicting directives
   - Missing directive files

---

## Troubleshooting

### Directive not working

**Problem:** Directive has no effect on response

**Solutions:**
1. Check directive name spelling (case-sensitive: `--short` not `--Short`)
2. Verify directive file exists in `directives/` folder
3. Check if your implementation supports the directive
4. Try with `--debug` to see what's active

### Conflicting directives

**Problem:** Multiple directives seem to conflict (e.g., `--short --verbose`)

**Solutions:**
1. Directives are applied in order (last one may override)
2. Some directives are incompatible by design
3. Check individual directive files for compatibility notes
4. Use `--debug` to see which directives are active

### Directive file not found

**Problem:** `(directive --name not found, continuing)`

**Solutions:**
1. Verify file exists: `directives/name.md`
2. Check file path configuration in your implementation
3. For remote loading, verify network access and URL
4. Check file permissions

### Parameter syntax issues

**Problem:** `--3samples` not working

**Solutions:**
1. Check if directive supports parameters
2. Verify syntax: `--directive=param` or `--directiveN`
3. Read directive file for exact parameter format
4. Some directives may not support parameters

### Persistent directives not exiting

**Problem:** Directive like `--socratic` stays active

**Solutions:**
1. Check directive documentation for exit commands
2. Common exits: `--done`, `--exit`, `--end`
3. Some directives persist until explicitly ended
4. Check implementation for session reset options

---

## Contributing

New directives should:

1. Do one thing well
2. Be understandable 
3. Avoid overlapping responsibilities
4. Define tone and structure clearly

### Contribution process

1. **Propose:** Open an issue discussing the new directive
2. **Create:** Add `directives/your_directive.md` following the template
3. **Test:** Verify it works with various prompts
4. **Document:** Update this README if needed
5. **Submit:** Create a pull request

### Directive review criteria

- ✅ Single, clear purpose
- ✅ Grandma-understandable
- ✅ Composable with existing directives
- ✅ Well-documented with examples
- ✅ No conflicts with existing directives

---

## Compatibility

### LLM Systems

Directives are designed to work with any LLM system that accepts system prompts or custom instructions:

- ✅ ChatGPT (via custom instructions)
- ✅ Claude (via system prompts)
- ✅ Local models (via system prompts)
- ✅ API wrappers (via prompt preprocessing)

### Implementation status

This repository provides the **specification and definitions**. Implementations may vary:

- Some systems may support all directives
- Others may support a subset
- Custom implementations can add new directives

Check your implementation's documentation for supported directives.

---

## License

MIT — steal freely, improve loudly.

---

## Additional Resources

### Learning more

- Read individual directive files in `directives/` for detailed behavior
- Check implementation examples in issues/discussions
- See `directives/directives.md` for meta-directive information

### Community

- Report issues for broken or unclear directives
- Suggest new directives via issues
- Share implementations and use cases

### Related concepts

- **Prompt engineering:** Directives complement prompt engineering
- **System prompts:** Directives modify system-level behavior
- **Chain-of-thought:** Some directives enable structured reasoning
