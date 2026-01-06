# Directive: --stargrade

**Purpose:**  
Evaluate any narrative (project summary, post-mortem, interview story, case study) using the **STAR** framework — *Situation, Task, Action, Result*.  
The goal is to test clarity, ownership, and outcome: can a reader easily see what happened, what you did, and what changed?

---

## 🧠 Output Structure

### 1. **Executive Summary**
- One short paragraph summarizing overall clarity and impact.  
- Example: “Clear problem and decisive actions, but results under-documented.”

### 2. **🧩 Situation**
- Does the story set context quickly?  
- Can we tell what was broken or at stake?  
- Grade how well the writer anchors the reader in time, place, and urgency.  
- Red flags: too vague, no stakes, or too much setup.  
- Example critique: “Context clear but lacks scale — how big was the issue?”

### 3. **🎯 Task**
- Is it clear what the person was responsible for?  
- Does it explain the objective and constraints (“what success meant”)?  
- Look for ownership words: *my role was*, *I was tasked with*, *I needed to*.  
- Weak if the reader can’t tell why this person was involved.  
- Example critique: “Good goal but unclear scope — was this solo or team work?”

### 4. **⚙️ Action**
- Are actions specific, sequential, and owned?  
- Look for strong verbs: *built, implemented, negotiated, designed, automated.*  
- Grade whether we can see the thinking behind choices.  
- Red flags: “helped with,” “participated in,” or passive language.  
- Example critique: “Actions concrete and believable; could show decision tradeoffs.”

### 5. **📈 Result**
- Are outcomes measurable? (%, $, time, users, risk reduced.)  
- Grade clarity of cause-and-effect — can we see how the actions produced the result?  
- Red flags: “improved things,” “was successful,” or outcomes without data.  
- Example critique: “Results clear but missing metrics or comparison baseline.”

### 6. **🧓 Sell It to My Grandma**
- One plain-English sentence describing the whole story.  
- Example: “We had broken dashboards, I fixed the data pipes, and now everyone trusts the numbers again.”  
- If this line sounds like fluff or confusion, the story itself needs simplification.

### 7. **⭐ Action Priorities**
- Suggest 2–4 bullet improvements.  
  - Add measurable outcomes or benchmarks.  
  - Clarify ownership and decision scope.  
  - Replace weak verbs with action verbs.  
  - Cut jargon and restate in one sentence for clarity.

---

## 🎯 Scoring Guide
- **9–10:** Complete STAR arc with clear causality and quantifiable results.  
- **7–8:** Strong clarity; small gaps in context or data.  
- **5–6:** Understandable but generic; limited metrics.  
- **3–4:** Disorganized or vague; unclear who did what.  
- **1–2:** Reads like fluff; no visible impact.

---

## 🧾 Example Output (Mock Evaluation)

**Executive Summary:**  
Strong context and clear actions; results implied but not measured. Excellent ownership tone.

**Situation:**  
Set up crisply — the system was failing weekly. Context makes stakes tangible. (9/10)

**Task:**  
Well-defined objective: rebuild pipeline stability. Could clarify success metric. (8/10)

**Action:**  
Detailed, sequential, and confident: rewrote Airflow DAGs, automated alerts, validated in staging. (9/10)

**Result:**  
Said “reliability improved,” but missing numbers (uptime %, incidents dropped). (6/10)

**Sell It to My Grandma:**  
“Our data jobs kept crashing, so I rebuilt them to run automatically, and now they stay up.”  

**Action Priorities:**  
- Add one concrete result metric.  
- Mention collaboration or cross-team coordination.  
- Tighten the opening to show impact faster.

---

**End of Directive**

