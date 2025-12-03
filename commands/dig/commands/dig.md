---
description: "Clarify ambiguities in plans with structured questions"
allowed-tools:
  - Read
  - Grep
  - Glob
  - TodoRead
  - AskUserQuestion
---

# 🔍 Plan Dig Mode (/dig)

<purpose>
Analyze the current plan or discussion, identify unclear points, and ask
structured questions using the AskUserQuestion tool.
</purpose>

## Execution Phases

### Phase 1: Context Gathering

**Auto-load these files first:**
1. `CLAUDE.md` - Project architecture, patterns, commands
2. `prd.md` or `README.md` (if exists) - Requirements/overview
3. Plan file (if exists via Read tool)
4. Current task status via TodoRead

**Important:** Read these files before generating questions to understand project-specific patterns and conventions.

### Phase 2: Identify Ambiguities

<categories>
| Category | Examples |
|----------|----------|
| **Architecture** | Layering strategy, component boundaries, design patterns |
| **Data** | Storage choice, data modeling, caching strategy |
| **API/Integration** | Protocol choice, error handling, versioning |
| **UI/UX** | Component structure, state management, styling approach |
| **Testing** | Test scope, mocking strategy, coverage goals |
| **DevOps** | Build process, deployment strategy, environment config |
| **Scope** | Feature boundaries, priorities, phased rollout |
</categories>

### Phase 3: Generate Questions

<rules>
- Question count: **2-4** (adjust based on ambiguity level)
- Each question has **2-4 concrete options**
- Each option includes **pros/cons** briefly
- Avoid open-ended questions
- "Other" option is auto-added - don't include it
- Align options with existing patterns from CLAUDE.md (if available)
</rules>

**AskUserQuestion format:**

```json
{
  "questions": [
    {
      "question": "Which data persistence approach should we use?",
      "header": "Data Storage",
      "multiSelect": false,
      "options": [
        {
          "label": "Database (SQL/NoSQL)",
          "description": "Pros: Queryable, scalable / Cons: Setup overhead"
        },
        {
          "label": "File-based",
          "description": "Pros: Simple, portable / Cons: Limited querying"
        },
        {
          "label": "In-memory only",
          "description": "Pros: Fast, no persistence logic / Cons: Data lost on restart"
        }
      ]
    }
  ]
}
```

### Phase 4: Post-Answer Processing

<output_format>
After receiving user answers, output:

## Decisions

| Item | Choice | Reason | Notes |
|------|--------|--------|-------|
| Data storage | Database | Scalability needs | Consider migration strategy |

## Next Steps

1. **First task**
   - Details...
2. **Second task**
   - Details...
</output_format>

---

## Question Templates by Task Type

### New Feature

```
1. Architecture pattern (MVC / MVVM / Clean Architecture / etc.)
2. Data persistence (Database / File / In-memory / External API)
3. State management (Local state / Global store / Server state)
```

### Refactoring

```
1. Split granularity (Module-based / Layer-based / Feature-based)
2. Testing strategy (Tests first / After refactor / Parallel)
3. Migration approach (Gradual / All-at-once / Feature flags)
```

### Bug Fix

```
1. Root cause hypothesis (State bug / Logic error / Race condition / External dependency)
2. Fix approach (Minimal fix / Include surrounding cleanup)
3. Verification method (Unit test / Integration test / Manual QA)
```

### API/Integration

```
1. Protocol choice (REST / GraphQL / gRPC / WebSocket)
2. Error handling (Retry / Fail-fast / Circuit breaker)
3. Authentication (API key / OAuth / JWT / Session)
```

### Performance Optimization

```
1. Bottleneck hypothesis (CPU / Memory / I/O / Network)
2. Optimization strategy (Caching / Lazy loading / Parallelization)
3. Measurement approach (Profiling / Benchmarks / APM)
```

---

## Guidelines to Avoid Over-Questioning

<constraints>
- **Skip obvious decisions** - Don't ask about already-decided or self-evident choices
- **Focus on high-impact decisions** - Prioritize architecture-level choices
- **Respect project conventions** - If CLAUDE.md covers it, don't ask
- **Check conversation history** - Exclude already-mentioned topics
- **Max 4 questions** - Too many hurts user experience
</constraints>

---

## Important Notes

- **Must use AskUserQuestion tool** - Not conversational questions
- **Language selection**:
  1. Check CLAUDE.md for language preference (e.g., "respond in Japanese")
  2. Fallback: Use English if no preference found
- Each option must include **pros/cons**
- Use multiSelect sparingly (default: false)
- Read CLAUDE.md before generating questions to align with project patterns
