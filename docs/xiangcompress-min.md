# XiangCompress-Min v0.1

## Definition

XiangCompress-Min is a minimal protocol for turning long AI task history into a short handoff card called `xb`.

The handoff card is intended for another model, chat, or agent that has not seen the original history.

## xb format

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

## Required fields

Required:

- `t`
- `history`
- `state`
- `relations`
- `request`

Conditional but strongly recommended:

- `dropped`, when there are rejected, downshifted, postponed, or not-to-repeat paths
- `gaps`, when there are unresolved items or missing information

## Principles

### 1. Handoff, not summary

The goal is not to summarize everything.

The goal is to preserve what another model needs in order to continue correctly.

### 2. Preserve stage

The next model must know the current stage of the task.

### 3. Preserve rejected paths

Many model handoff failures happen because a new model repeats already rejected ideas.

Use `dropped` to prevent that.

### 4. Preserve gaps

Many models hallucinate completion when information is missing.

Use `gaps` to make unknowns explicit.

### 5. Preserve reasoning relations

Use `relations` to preserve a small number of reasoning dependencies.

## Minimal reading behavior

A model reading `xb` should:

1. identify current stage from `t` and `state`;
2. use `history` to understand prior decisions;
3. use `relations` to preserve reasoning structure;
4. avoid `dropped` paths;
5. treat `gaps` as unresolved;
6. execute `request`.

## Success criteria

A successful handoff means the receiving model:

- understands the current task stage;
- does not repeat dropped paths;
- respects gaps;
- follows request;
- can continue the task without the full history.
