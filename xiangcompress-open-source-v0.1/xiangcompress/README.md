# XiangCompress

**XiangCompress** is a minimal handoff-card method for transferring long-running AI task state between models, chats, or agents.

It is not a normal summary.  
It is not a full memory system.  
It is not a knowledge graph.  
It is not Xiang Language itself.

XiangCompress is a lightweight pre-tool for preserving enough task state so another model can continue the task without reading the full history.

It preserves:

- current task stage
- key history
- reasoning relations
- dropped paths
- missing gaps
- next request

The default output is an `xb` handoff card.

```yaml
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
```

## Why this exists

Long conversations and multi-step AI tasks often fail at handoff.

A new model may:

- repeat already rejected ideas
- miss the current task stage
- treat unresolved items as completed
- summarize instead of continuing
- lose reasoning dependencies
- ask for information that was already decided
- ignore what is still unknown

XiangCompress is designed to reduce those failures.

It converts long task history into a short structured handoff card that tells the next model:

1. where the task is now;
2. what history matters;
3. which reasoning relations must be preserved;
4. what has been dropped or rejected;
5. what information is still missing;
6. what to do next.

## Core idea

Normal summaries answer:

> What happened?

XiangCompress answers:

> What does the next model need in order to continue correctly?

## Minimal workflow

### 1. Compress

Give a long task history to Model A with the compression prompt.

Model A outputs `xb`.

### 2. Read

Give `xb` to Model B with the read prompt.

Model B continues the task.

### 3. Update

If the task continues, Model B outputs `updated_xb`.

Model C can then continue from `updated_xb`.

```text
long history → Model A → xb
xb → Model B → result + updated_xb
updated_xb → Model C → continuation
```

## Quick start

Use the prompts in:

- [`templates/compress_prompt.md`](templates/compress_prompt.md)
- [`templates/read_prompt.md`](templates/read_prompt.md)
- [`templates/update_prompt.md`](templates/update_prompt.md)

Or use the short version below.

### Compress prompt

```text
Use XiangCompress-Min to compress the following task history into xb.
Do not write a normal summary.
Keep only what another model needs to continue the task correctly.
```

### Read prompt

```text
Read the following xb handoff card and continue the task.
Treat gaps as unresolved.
Do not repeat dropped paths.
Follow request directly.
```

## Fields

| Field | Meaning |
|---|---|
| `t` | Current task stage in one line |
| `history` | Key turns, decisions, tests, rejected paths |
| `state` | Current task state in 2-5 sentences |
| `relations` | Important triples needed for reasoning continuity |
| `dropped` | Rejected, downshifted, or postponed directions with reasons |
| `gaps` | Missing information the next model must not pretend to know |
| `request` | Exactly what the next model should do next |

## What to keep

Keep:

- stage changes
- confirmed decisions
- rejected paths
- important corrections
- dependencies needed for reasoning
- risks and gaps
- next action

Drop:

- full background
- repeated explanations
- decorative structure
- object definitions not needed for continuation
- old context not relevant to the next request

## Relation rule

Use relation triples:

```yaml
relations:
  - [source, relation, target]
```

Good relations:

```yaml
- [history, prevents, repeating_rejected_paths]
- [gaps, prevents, false_completeness]
- [XiangBrief, transfers, task_state]
```

Weak relations:

```yaml
- [XiangBrief, is, a_format]
- [old_topic, related_to, current_topic]
```

A relation should help the next model continue reasoning. It should not merely define an object.

## Reading rule

When reading `xb`, the next model should:

1. reconstruct the current task stage;
2. use `relations` for reasoning structure;
3. avoid repeating `dropped` paths;
4. treat `gaps` as unresolved;
5. follow `request` directly;
6. avoid pretending missing information is known.

## When to use

Use XiangCompress for:

- long conversations
- cross-model handoff
- project continuation
- agent-to-agent task transfer
- recurring research or writing tasks
- tasks with rejected paths and important decisions

Do not use it for:

- simple one-turn questions
- short summaries
- tasks with no state to preserve
- purely human-facing prose summaries

## Project status

This is an experimental minimal protocol/tooling package.

The current version is:

```text
XiangCompress-Min v0.1
```

It is intentionally small.

## Relationship to Xiang Language

XiangCompress is not Xiang Language itself.

It is a small pre-tool for preserving task state while developing, testing, and using broader Xiang-based representations.

## License

MIT License.
