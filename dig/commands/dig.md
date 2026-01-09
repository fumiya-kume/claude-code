---
description: "Clarify ambiguities in plans with structured questions"
allowed-tools:
  - Write
  - Edit
  - Read
  - Grep
  - Glob
  - TodoRead
  - TodoWrite
  - AskUserQuestion
---

Read the current plan file and interview me in detail using the AskUserQuestionTool about literally anything.
- Product Spec
- Technical detail
- UI/UX
- and anything

You will follow the phases

1. Clearfy unclear point
2. Ask user question for make dicision
4. Apply dicision to plan
5. Show the summary for user

Should be very in-depth and continue digging me until complete all of unclear point, then you will write the spec to the plan file.
After phase 3, you revisit to the plan file, and analyze them, you must to rise the unclear point with moving to phase 2.

### Phase 2: Generate Questions

<rules>
- Question count: **2-4** (adjust based on ambiguity level)
- Each question has **2-4 concrete options**
- Each option includes **pros/cons** briefly
- Avoid open-ended questions
- "Other" option is auto-added - don't include it
- Align options with existing patterns from CLAUDE.md (if available)
</rules>


### Phase 3: Post-Answer Processing

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

## Important Notes

- **Must use AskUserQuestion tool** - Not conversational questions
- **Language selection**:
  1. Check CLAUDE.md for language preference (e.g., "respond in Japanese")
  2. Fallback: Use English if no preference found
- Each option must include **pros/cons**
- Use multiSelect sparingly (default: false)
- Read CLAUDE.md before generating questions to align with project patterns
