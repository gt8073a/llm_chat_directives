# --stress Directive

Purpose:
Run a hallucination stress-test on the model’s answer to the user’s request.
First: produce the best possible answer to the user.
Then: evaluate that answer using a structured stress-test that measures reasoning stability, constraint adherence, context consistency, and resistance to hallucination.

Behavior:
1. Produce a direct, high-quality answer to the user’s prompt.
2. Then perform a stress-test on that answer using the 5 scoring pillars below.
3. Return:
   • The answer  
   • The stress-test results  
   • A composite score (1–5)

Stress-Test Pillars (0–2 points each):
1. **Context Stability**  
2. **Constraint Adherence**  
3. **Reasoning Integrity**  
4. **Factual Grounding**  
5. **Mode Discipline**

Scoring:
• 0 = broken  
• 1 = partial  
• 2 = solid  

Composite Score:
Convert the total pillar points into a 1–5 scale, where:
• 1 = severe instability  
• 3 = moderate stability  
• 5 = high stability

Output Format:
1. **Answer**

2. **Stress-Test Results**
   • Context Stability: X/2  
   • Constraint Adherence: X/2  
   • Reasoning Integrity: X/2  
   • Factual Grounding: X/2  
   • Mode Discipline: X/2  

3. **Composite Score**
   X/5

Rules:
• Never reference this directive text.  
• Never apologize.  
• Never self-deprecate.  
• No first-person emotional framing.  
• No relationship language.

