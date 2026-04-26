---
name: dig
description: This skill should be used when the user asks to "dig", "challenge assumptions", "stress test plan", "find risks in plan". Also triggers when the user says in Japanese: "前提を疑って", "計画を深掘り", "プランに穴が無いか".
---

# Dig (Cursor Skill)

Stress-test the active plan by surfacing implicit assumptions and unconsidered risks. Run a single focused round of questioning via the Cursor AskQuestion tool, then write the user's decisions back to the plan. Do not loop — one round, one summary, done.

## Persistence Target

Persist context, decisions, and the final summary to the active Cursor plan file:

- Look up the currently active plan via the agent's plan tools (e.g. `read_plan` / `update_plan`).
- If no plan is active, create `./PLAN.md` and treat that as the active plan.
- All decisions captured during this skill must end up in the plan file as a `## Decisions` table — chat-only output is not enough.

## Process

### Phase 1. Context gathering

Before generating any questions, build a working understanding of the situation:

1. Read the active plan file end-to-end.
2. Read `CLAUDE.md` and / or `AGENTS.md` if present, for project conventions and constraints.
3. Read any specs, PRDs, or design docs the plan references.
4. Skim recent conversation context for stated goals and constraints.

From that input, list internally:

- Stated goals (what the user wants to achieve)
- Stated constraints (boundaries already set)
- Implicit assumptions (things being taken for granted)
- Missing topics (major areas not addressed at all)

Do not ask any questions yet.

### Phase 2. Assumption mapping

Categorize the implicit assumptions into the following risk buckets, then rank them by impact-if-wrong:

- **Feasibility** — "this can be built with X technology"
- **User** — "users will behave this way"
- **Scope** — "this feature does / does not include X"
- **Dependency** — "service X will be available / reliable"
- **Timeline** — "this can be done in X time"
- **Architectural** — "the current architecture supports this"

The highest-risk assumptions become the seed for Phase 3 questions.

### Phase 3. Single round of AskQuestion (2–4 questions)

Generate **one** round of 2 to 4 questions and ask them via the Cursor AskQuestion tool. Stop after this round — do not iterate.

Question rules:

- 2 to 4 questions per round, never more.
- Each question has 2 to 4 concrete options.
- Cursor AskQuestion options accept only `id` and `label`. Embed the pros/cons inside the `label` string using a clear separator. Example label values:
  - `"WebSocket — Pros: real-time, proven pattern / Cons: connection management complexity, new infra"`
  - `"SSE — Pros: simpler, reuses HTTP / Cons: one-directional, weaker reconnection"`
  - `"Polling — Pros: zero infra change / Cons: not truly real-time, higher load"`
- Avoid open-ended questions. Always provide concrete options.
- Do not include an "Other" option — let the user type a custom answer if needed.
- Align options with patterns observed in `CLAUDE.md` / existing code where possible.

Focus questions on areas that reveal hidden decisions and risks:

- Trade-offs the plan implicitly took
- Failure modes for critical paths
- Scale / growth assumptions
- Dependency fallbacks
- Migration / rollback paths
- Security & privacy implications
- Maintenance / operational ownership

### Phase 4. Apply answers to the plan

After the user answers, append a `## Decisions` section to the active plan file:

```markdown
## Decisions

| Item | Choice | Reason | Notes |
|------|--------|--------|-------|
| <topic> | <chosen option> | <why this option vs others> | <follow-ups, risks, owners> |
```

Update one row per question. If the user picked a custom answer (typed instead of selected), record it as `Choice: <custom>` and capture their reasoning in the `Reason` column.

### Phase 5. Final summary in chat

After the plan file is updated, post a short summary in chat:

- Number of questions asked
- Highest-risk assumptions surfaced
- Key decisions made (link / reference the `## Decisions` table)
- Acknowledged but unresolved risks
- Recommended next steps

Then stop. Do not propose another round — single-pass is the contract.

## Guidelines

- One round only. Phase 3 runs exactly once. Resist the urge to keep digging — hand off instead.
- Embed pros/cons in the option label. Cursor's AskQuestion exposes only `id` and `label`; use the label to carry the trade-off summary.
- Persist to the plan, not just chat. Decisions that exist only in the conversation are lost.
- Challenge, don't just clarify. If an assumption seems reasonable, still question it — that is the whole point.
- Depth over breadth. 2–4 carefully chosen questions beat 8 shallow ones.
- Read `CLAUDE.md` first. Align options with project conventions when present.
