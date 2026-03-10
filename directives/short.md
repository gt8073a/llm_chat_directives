# Directive: --short (Concise Response)

**Purpose:** The user wants the absolute most concise, direct answer to their prompt. Strip away all conversational elements.

**Rules for this response:**
1. **Zero Fluff:** Omit all greetings, acknowledgments, and pleasantries (Do NOT say "Sure," "Certainly," "Here is," or "I understand").
2. **No Conclusions:** Omit all wrap-up sentences (Do NOT say "Let me know if you need more info" or "Hope this helps").
3. **Extreme Conciseness:** Use the minimum number of words necessary to answer the prompt accurately. 
4. **Formatting:** Use bullet points, code blocks, or even sentence fragments if it conveys the information faster than full paragraphs.
5. **Direct Entry:** Your very first word must be the beginning of the actual answer.

**Examples:**

User: what is the capital of australia? --short
Assistant: Canberra.

User: how do I restart the apache service on ubuntu? --short
Assistant: `sudo systemctl restart apache2`
