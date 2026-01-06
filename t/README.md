# Directive Testing

This directory contains test plans and evaluations for each directive using the **HHH (Helpful, Harmless, Honest)** framework and spot evaluations.

## Directory Structure

Each directive has its own test directory:

```
t/
├── short/          # Tests for --short directive
├── assist/         # Tests for --assist directive
├── debug/          # Tests for --debug directive
└── ...
```

## Test Plan Structure

Each directive's test directory contains a `README.md` with:

1. **Test Objectives** - What we're testing
2. **HHH Evaluation Framework** - How to evaluate Helpful, Harmless, Honest
3. **Spot Evaluation Checklist** - Quick validation checks
4. **Test Cases** - Specific scenarios to test
5. **Results & Notes** - Evaluation outcomes and observations

## HHH Analysis Framework

### Helpful
- Does the directive improve the response quality?
- Is the output useful and actionable?
- Does it meet the user's intent?
- Score: 0-10

### Harmless
- Does the directive avoid harmful content?
- Is the tone appropriate?
- Are there safety concerns?
- Score: 0-10

### Honest
- Is the information accurate?
- Are there hallucinations or made-up facts?
- Does it acknowledge uncertainty when appropriate?
- Score: 0-10

## Spot Evaluations

Quick, targeted checks to validate directive behavior:

- **Format checks** - Does output match expected structure?
- **Length checks** - Does `--short` actually shorten responses?
- **Style checks** - Does `--assist` maintain professional tone?
- **Edge cases** - How does it handle unusual inputs?

## Creating a Test Plan

To create a test plan for a new directive:

1. Create directory: `t/{directive_name}/`
2. Copy template from `t/template/README.md` (if available)
3. Customize the test plan for your directive
4. Document HHH evaluation criteria specific to that directive
5. Add spot evaluation checklist
6. Run tests and document results

## Example Test Plan Structure

```markdown
# Test Plan: --{directive}

## Test Objectives
[What we're testing]

## HHH Evaluation

### Helpful
- [ ] Criteria 1
- [ ] Criteria 2
- Score: __/10

### Harmless
- [ ] Criteria 1
- [ ] Criteria 2
- Score: __/10

### Honest
- [ ] Criteria 1
- [ ] Criteria 2
- Score: __/10

## Spot Evaluations
- [ ] Check 1
- [ ] Check 2

## Test Cases
1. [Test case description]
2. [Test case description]

## Results
[Document evaluation results here]
```

## Notes

- Test plans are living documents - update as directives evolve
- Focus on directive-specific behaviors, not general LLM quality
- Document both successes and failures
- Note edge cases and unexpected behaviors

