# XiangCompress-Min: Compress Prompt

Use this prompt with Model A.

```text
You will perform a XiangCompress-Min compression task.

Goal:
Compress the long conversation/task record below into an xb handoff card so that another model that has never seen the original record can understand the current task state, confirmed facts, unresolved items, dropped paths, key relations, and next action.

Important rules:
1. Do not write a normal summary.
2. Do not restate the full background.
3. Do not invent information not present in the record.
4. Do not mark unresolved items as completed.
5. If the raw task record is missing, or only a placeholder is shown, output missing_raw_history. Do not infer from memory or prior context.
6. Put in gaps anything the receiving model must not pretend to know.
7. request must tell the next model exactly what to do next. Do not write vague instructions such as "continue".
8. If the next task is checking, confirming, or verifying something, do not ask the next model to claim it has confirmed it. Ask it to produce a checklist or ask the user for confirmation.
9. Output valid YAML only.
10. Every item under history, relations, dropped, and gaps must use "-" list format.
11. Output only xb. Do not add explanations.

Use this exact format:

xb:
  t: ""
  history:
    - ""
  state: >
    ""
  relations:
    - [source, relation, target]
  dropped:
    - [item, reason]
  gaps:
    - ""
  request: >
    ""

Field rules:

t:
Current task stage in one line.

history:
Only keep key history needed for handoff:
- confirmed decisions or conclusions;
- important tests;
- important corrections;
- rejected, downshifted, or postponed directions;
- why the task is now at this stage.
Do not include full background.

state:
Current task state in 2-5 sentences.
Clearly separate:
- known facts;
- completed items;
- unresolved items;
- current problem.
Do not turn gaps into completed facts.

relations:
Keep only relation triples that help the next model continue reasoning.
Use [source, relation, target].
Prefer relations that:
- support the current request;
- explain the current stage;
- prevent repeating old mistakes;
- express exceptions, boundaries, risks, or dependencies.
Drop:
- relations that only repeat state;
- pure object definitions;
- old background;
- relations unrelated to the next step.

dropped:
Record rejected, refused, downshifted, postponed, or not-to-repeat directions with reasons.
Omit this field if none exist.
dropped is not ordinary history. It prevents the next model from going backward.

gaps:
Record unresolved or unavailable information that the next model must not pretend to know.
Items in gaps must be treated as unresolved by the next model.
Omit this field if none exist.

request:
Tell the next model exactly what to do.
If a checklist is needed, explicitly say "produce a checklist".
If something must be avoided, say so.
request should be directly executable.

Now compress the following raw conversation/task record into xb:

[PASTE RAW TASK HISTORY HERE]
```
