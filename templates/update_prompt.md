# XiangCompress-Min: Update Prompt

Use this when the receiving model finishes work but the task should continue.

```text
If the task should continue, output updated_xb after your answer.

Use this format:

updated_xb:
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

Update rules:
- Update only changed content.
- Add newly confirmed decisions to history.
- Add newly rejected, downshifted, or postponed directions to dropped.
- Add unresolved missing information to gaps.
- Update request to the next task.
- Do not mark gaps as completed facts.
- Output valid YAML.
```
