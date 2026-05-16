# XiangCompress-Min: Read Prompt

Use this prompt with Model B.

```text
Read the following xb handoff card and follow request.

Reading rules:
1. You have not seen the original long conversation. Use only xb.
2. Do not treat xb as a normal summary.
3. First reconstruct the current task stage, then execute request.
4. Items in gaps are unresolved. Do not mark them as completed facts.
5. Do not repeat directions listed in dropped unless you explicitly explain why they must be reconsidered.
6. If request is a checking, confirming, or verification task, you cannot claim you have confirmed it. Produce a checklist or ask the user for confirmation.
7. If xb is insufficient, say exactly what is missing. Do not invent missing information.
8. Execute request directly. Do not regenerate xb unless asked.

xb:
[PASTE XB HERE]
```
