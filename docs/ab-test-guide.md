# A/B Test Guide

This guide tests whether `xb` helps another model continue a task better than a normal summary.

## Setup

Prepare one long task history.

Create two versions:

- A: normal natural-language summary
- B: XiangCompress `xb`

Give A and B to two separate models or two separate fresh chats.

Ask both to continue the same task.

## Compare

Score each output on a 0-2 scale.

| Criterion | Question |
|---|---|
| Stage recognition | Did the model identify the current task stage? |
| Dropped path avoidance | Did it avoid repeating rejected/downshifted paths? |
| Gap awareness | Did it treat missing information as missing? |
| Task continuation | Did it directly continue the task? |
| Relation preservation | Did it preserve key dependencies? |
| Request following | Did it follow the next action? |
| Hallucination control | Did it avoid inventing missing information? |

## Interpretation

If `xb` wins mainly by reducing token count, that is useful but not required.

The main value of `xb` is:

- less regression;
- fewer repeated rejected ideas;
- better stage locking;
- clearer next action;
- better respect for unresolved gaps.

## Failure signals

The receiving model fails if it:

- treats `xb` as an ordinary summary;
- repeats dropped paths;
- marks gaps as completed;
- asks for information already present;
- ignores request;
- rewrites the handoff card instead of executing it.
