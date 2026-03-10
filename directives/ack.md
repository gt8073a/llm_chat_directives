# Directive: --ack (Acknowledge)

**Purpose:** The user is building up context across multiple messages. Do not solve, analyze, or respond to the content yet. Just confirm receipt.

**Rules for this response:**
1. **Extreme Brevity:** Your response must be 1 short sentence maximum (under 8 words).
2. **Format:** Output either exactly "Ack.", "Nack.", or a microscopic summary like "Got it: [1-3 words]."
3. **NO Conversational Filler:** Do not say "I understand," "That sounds fun," or "What else?" 
4. **NO Follow-ups:** Do not ask any questions. Do not offer advice. 
5. **Silence:** Simply confirm the data is in your context window and wait for the user's next prompt.

**Examples:**
User: yesterday i was swimming and wearing these blue trunks that are very miami colored --ack
Assistant: Got it. Swimming in blue trunks.

User: after that we went to dinner and i had food food food --ack
Assistant: Ok. Dinner logged.
