---
description: "Deep exploratory interview to discover unknowns and strengthen plans"
version: "3.0.0"
allowed-tools:
  - Write
  - Edit
  - Read
  - Grep
  - Glob
  - TodoRead
  - TodoWrite
  - AskUserQuestion
context: fork
agent: General-purpose
---

# Deep Dig

Conduct a deep exploratory interview to uncover hidden assumptions, undiscovered risks, and unconsidered decisions in the current plan.

## Core Principle

Dig deep, not wide. Pursue lines of inquiry that reveal what the user has not considered:
- **Depth over breadth** — follow a thread until it yields no more insights
- **Challenge assumptions** — question premises, not just details
- **Surface the implicit** — make hidden decisions explicit
- **Provoke thought** — the best questions make the user say "I hadn't thought of that"

## Process

### Phase 1: Context Gathering

Read and analyze before asking any questions:
- Plan file (if it exists), CLAUDE.md, related docs/PRDs
- Recent conversation context

Identify: stated goals, stated constraints, implicit assumptions, missing topics.

### Phase 2: Assumption Mapping

Categorize and rank assumptions by risk (how badly things go wrong if incorrect):
- **Feasibility** — "This can be built with X technology"
- **User** — "Users will behave this way"
- **Scope** — "This feature does/doesn't include X"
- **Dependency** — "Service X will be available/reliable"
- **Architectural** — "The current architecture supports this"

Start investigation with the highest-risk assumptions.

### Phase 3: Deep Investigation

Conduct iterative rounds using AskUserQuestion tool.

<rules>
- 2–3 questions per round (fewer questions, deeper focus)
- Each question has 2–4 concrete options with brief pros/cons
- "Other" option is auto-added — do not include it
- Align options with existing patterns from CLAUDE.md (if available)
</rules>

<question_focus>
- **Assumptions** — "The plan assumes X. Is this actually the case?"
- **Trade-offs** — "You chose X, but have you considered the trade-off with Y?"
- **Scale** — "This works for N users. What happens at 10N?"
- **Failure modes** — "What happens when X goes wrong?"
- **Dependencies** — "This depends on X. What's the fallback?"
- **Security** — "Who has access to this data?"
- **Migration** — "How do you get from current state to target state safely?"
</question_focus>

After each answer round:
1. Analyze the answer for new assumptions it reveals
2. Follow up on the most interesting thread (go at least 2 levels deep per topic)
3. Track which assumption categories remain unexplored

### Phase 4: Apply and Integrate

After each round, output a discovery summary:

```markdown
## Discoveries (Round N)

### Assumptions Challenged
| Assumption | Finding | Impact | Decision |
|------------|---------|--------|----------|

### Decisions Made
| Topic | Decision | Rationale | Risk Level |
|-------|----------|-----------|------------|

### New Questions Surfaced
- [Questions discovered for next iteration]
```

Update the plan file with confirmed decisions.

### Phase 5: Completeness Evaluation

Check all criteria before stopping:
- [ ] All high-risk assumptions explicitly addressed
- [ ] At least 2 levels of depth on each major topic
- [ ] No unresolved "New Questions Surfaced" from Phase 4
- [ ] Trade-offs explicitly acknowledged
- [ ] Failure modes for critical paths discussed
- [ ] Plan file reflects all decisions

**If any unchecked**: return to Phase 3.
**If all checked**: generate the final summary.

### Final Summary

```markdown
## Dig Summary

### Investigation Overview
- Rounds completed: [N] | Questions asked: [N]
- Assumptions challenged: [N] | Decisions made: [N]

### Key Discoveries
1. [Most impactful finding]
2. [Second most impactful finding]

### All Decisions
| Topic | Decision | Rationale | Risk | Notes |
|-------|----------|-----------|------|-------|

### Remaining Risks
- [Acknowledged but unresolved risks]

### Recommended Next Steps
1. [First action]
2. [Second action]
```
