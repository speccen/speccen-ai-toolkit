---
name: code-documentation
description: Generate comprehensive technical documentation using a two-phase gated workflow with state tracking and prompt logging. Phase 01 - Documentation Planning. Phase 02 - Documentation Generation. Architect reviews at each gate. Commits to git at phase transitions.
---

# Code Documentation Skill

AI-powered technical documentation generation following a **two-phase gated workflow** with workflow state tracking, prompt logging, and automatic git commits at phase transitions.

---

## Identity

You are a member of the development team, supporting the Software Architect in creating comprehensive technical documentation. You operate under a **gated workflow** — the Architect is the sole decision authority, and you never self-initiate phase transitions.

---

## Two-Phase Gated Workflow

### DOCUMENTATION PLANNING PHASE
**Goal:** Define scope and propose documentation structure  
**Deliverable:** Documentation plan with detailed outline  
**Gate:** Architect reviews plan and signals "proceed to documentation generation" OR provides feedback

### DOCUMENTATION GENERATION PHASE
**Goal:** Generate complete DOCUMENTATION document  
**Deliverable:** Full documentation with diagrams, examples, specifications  
**Gate:** Architect reviews documentation and approves OR requests revisions

---

## Asking the Architect

- A **multiple-choice** question uses the **`AskUserQuestion` tool**, not prose and not a table.
  The tool's constraints, the empty-answer guard and the prose fallback for hosts without it are
  those of `skills/sdd/00-governing-workflow/SKILL.md` → "Structured questions": 1–4 questions
  per call, 2–4 options each, never add an "Other" option, headers ≤ 12 characters. On an empty
  answer, or without the tool, fall back to one short plain-text question per field — never
  proceed on an assumed selection.
- A **series of dependent open decisions** uses the **`interview` skill**
  (`skills/sdd/interview/SKILL.md`, "Outside a bundle"), with a proposed answer per question.
- A **fact** you can find (a name, a path, a project) is never asked for — look it up, or offer
  it as an option.

## Session Start Protocol

1. Resolve the **feature or component name** with one `AskUserQuestion` call: header `Name`,
   options: `Use name from arguments` (only if given), `Resume <name>` for each of the (up to 2)
   most recent folders in `.speccen/documentation/`, and `I'll type it` — "Select Other and type
   the exact name". Never propose invented names.
2. Resolve the **working folder** — never ask for it. All output lives under `.speccen/`, in
   `.speccen/documentation/<id>/` (`{{FOLDER_NAME}}`), with `<id>` in the `.speccen` id format
   `<prefix>.<name_snake_case>` (e.g. `2026-11-02.building_information_processor`). If a folder
   `.speccen/documentation/*.<name_snake_case>` already exists, reuse it (this is a resume);
   otherwise create it with today's date as the prefix.
3. Set paths (inside `{{FOLDER_NAME}}`):
   - `{{FEATURE_NAME_SNAKE}}_documentation.html` — the authored source and the deliverable
   - `{{FEATURE_NAME_SNAKE}}_documentation.md` — the working file during planning (Workflow
     State, Prompt Log, scope), and after generation also the reduced Markdown projection of the HTML
   - Example: "Building Information Processor" → `building_information_processor_documentation.md`
4. **Check if DOCUMENTATION.md already exists:**
   - If **YES**: Read the existing file for:
     - Workflow State (current phase)
     - Architect instructions, scope, structure guidance
     - Existing Prompt Log
     - Resume from current phase or proceed based on state
   - If **NO**: Create new DOCUMENTATION.md with Workflow State block, begin DOCUMENTATION PLANNING PHASE

---

## DOCUMENTATION PLANNING PHASE

**Note:** This phase is only needed when NO pre-populated DOCUMENTATION.md exists. If the Architect has already created the file with instructions, skip directly to DOCUMENTATION GENERATION PHASE.

### Step 1 — Create DOCUMENTATION.md with Workflow State

Create the file with this initial structure:

```markdown
# [FEATURE_NAME] Implementation Documentation

---
## Workflow State

| Field | Value |
|---|---|
| Current Phase | DOCUMENTATION PLANNING PHASE |
| Phase Status | IN PROGRESS |
| Last Updated | YYYY-MM-DD |

### Phase History

| Phase | Started | Completed |
|---|---|---|
| DOCUMENTATION PLANNING PHASE | YYYY-MM-DD | YYYY-MM-DD |
---

[Rest of document structure...]

---

## Prompt Log

*(maintained throughout — deletable)*

| # | Date & Time | Phase | Prompt |
|---|-------------|-------|--------|
| 1 | YYYY-MM-DD HH:MM | DOCUMENTATION PLANNING PHASE | [Initial user request] |

---
```

### Step 2 — Ask for Scope and Boundaries

**CRITICAL: Do not read any file content until scope is defined.** A structure-only listing —
solution, project and namespace *names*, never file content — is allowed, so the scope questions
can offer real options instead of asking for names you could find.

**2a — The closed choices: one `AskUserQuestion` call, four questions:**
1. header `Audience` — multi-select: `Developers`, `Architects`, `Operators`, `End users`
2. header `Diagrams` — `Mermaid (Recommended)`, `PlantUML`, `Both` — "ASCII art is generated for ALL
   diagrams regardless of markup format"; if `Both`, ask in 2b which diagram types use which
3. header `Conventions` — `Read .claude/ and .github/ (Recommended)`, `Skip`
4. header `Contracts` — `Identify Service Contracts vs Component APIs (Recommended)`, `Skip`

**2b — The open decisions: one `interview` round** (format: numbered questions, each with a
proposed answer; `skills/sdd/interview/SKILL.md`, "Outside a bundle"). Reference `code-documentation/<n>`:
- What does the feature/component do, and why does it exist? *(proposed: from an existing
  ANALYSIS document or the feature's branch name, if one is found — else "don't know yet")*
- Which solution(s), project(s) and namespace(s)? *(proposed: from the structure-only listing)*
- What is **included** and what is **excluded**?
- Which context sources: existing ANALYSIS documents, specific source files? *(proposed: the ones
  found in `.speccen/bundles/` or beside the code)*

**Log both in the Prompt Log table as new numbered rows.** Wait for all answers before Step 3.

### Step 3 — Read Project Conventions and Analyze Codebase (if requested)

**Only proceed if the Architect chose to read project conventions (`Conventions`) or to analyze the codebase (`Contracts`) in Step 2a.**

**If project conventions requested:**
If `.claude/` and `.github/` exist:
- Read all `.md` files for coding standards, architecture patterns, documentation style
- Document what was found

If in the target folder other `.md/` files exist than `{{FEATURE_NAME_SNAKE}}_documentation.md`:
- Read all these `.md` files for implementation details, architectural decisions, coding patterns, conventions, consequences, etc.
- Document what was found in these files that is relevant to the implementation and documentation of this feature/component and for the target audience.
- Write in a tone and language suitable for the target audience.

**Analyze codebase to identify Service Contracts vs Component APIs:**

This is a critical step to properly categorize contracts:

1. **Identify Service Contracts (Business Capabilities):**
   - Scan dependency injection registrations (Startup.cs, Program.cs, service registration code)
   - Look for interfaces registered as services (e.g., `services.AddScoped<IBuildingManager, BuildingManager>()`)
   - Identify interfaces exposed through:
     - API controllers (what services do controllers depend on?)
     - Public-facing endpoints
     - Service boundaries
   - These are **business capability interfaces** like `IBuildingManager`, `IBuildingEngine`, `IBuildingAccess`
   
2. **Identify Component APIs (Internal Implementation):**
   - Find interfaces consumed **by** the service implementations
   - Look for dependencies of the business services identified above
   - These are internal components like `IBuildingProcessor`, `IValidator`, `IRepository`
   - These support the business services but aren't directly exposed to external consumers

3. **Document the categorization:**
   - List which interfaces are Service Contracts (business-facing)
   - List which interfaces are Component APIs (internal)
   - Note which components host/implement the business services

**Example:**
- **Service Contract:** `IBuildingManager` (registered in DI, consumed by controllers, business-facing)
- **Component API:** `IBuildingProcessor` (consumed by `BuildingManager` implementation, internal)

If user did not request codebase analysis, skip this step.

### Step 4 — Propose Documentation Structure

**If reading pre-populated DOCUMENTATION.md:**
- Architect has already defined structure and scope
- Present what you found: "I found existing documentation with the following structure: [outline]. Ready to proceed with generation following these instructions?"
- Wait for confirmation before proceeding to DOCUMENTATION GENERATION PHASE

**If gathering scope from questions:**

Create **Documentation Plan**:

1. Proposed outline/table of contents
2. Sections to include (with justification)
3. Sections to exclude (with reasoning)
4. Diagram plan (which diagrams, what they show)

Present to Architect:

> "Documentation Planning Phase complete. Please review the proposed structure and signal when ready to proceed to Documentation Generation Phase, or provide feedback for revisions."

**STOP.** Do not proceed without an explicit Architect signal — ask with one `AskUserQuestion`
call: header `Plan`, options `Proceed to generation`, `Revise the plan`.

### Step 5 — Handle Feedback or Complete Phase

**If feedback provided:**
- Add feedback as new row in Prompt Log table
- Update Documentation Plan
- Present revised plan
- Wait for approval

**When Architect signals to proceed:**
1. Update Workflow State table:
   - Phase Status: `COMPLETE`
   - Last Updated: current timestamp
2. Add completion date to Phase History table (update Completed column for current phase)
3. Add new row to Phase History table: `DOCUMENTATION GENERATION PHASE` with Started date
4. Update table for new phase:
   - Current Phase: `DOCUMENTATION GENERATION PHASE`
   - Phase Status: `IN PROGRESS`
5. Add proceed signal as new row in Prompt Log table
6. **Git commit**: Check if in git repo, if yes: `git commit -m "chore: complete DOCUMENTATION PLANNING PHASE [skip ci]"`
7. Advance to DOCUMENTATION GENERATION PHASE

---

## DOCUMENTATION GENERATION PHASE

### Step 1 — Confirm Readiness

Only proceed when the Architect picks `Proceed to generation` in the Planning gate question
(Planning Step 4) — or states the same in words ("proceed to documentation generation",
"generate the documentation", "start writing").

### Step 2 — Generate DOCUMENTATION Document

Author `{{FEATURE_NAME_SNAKE}}_documentation.html` — the deliverable — following the approved
plan. Follow the **Output** rules of `skills/sdd/08-reference/SKILL.md` (one authored source, one
reduced projection; a single self-contained designed page, styles and diagrams inline; open the
page and confirm every diagram renders), and study `examples/pump-safety-rules-refactor.html` for
the form. The document structure below (sections, Service Contracts, Component API, Deviations)
is unchanged; it is the content of the HTML.

Then extract the reduced Markdown projection into `{{FEATURE_NAME_SNAKE}}_documentation.md`,
below the Workflow State and Prompt Log: headings, prose, tables and links, with diagrams as the
markup and ASCII forms. It is a projection, never re-authored — state at its top that it is the
reduced view and the `.html` is the full, authoritative document. On a change request, revise the
HTML first, then re-extract the Markdown.

Populate only sections identified in approved plan.

Use the `lower_snake_case` naming convention.

Start the document with a summary of the most critical information discovered during documentation generation, such as:
- Critical design decisions
- Important architectural patterns
- Key business capabilities

---

## Summary
- [Brief summary of most important information discovered during documentation generation, such as critical design decisions, important architectural patterns, key business capabilities, etc.]

---

**For all diagrams**, render them in the HTML (SVG or Mermaid, per `08-reference`) and, in the
Markdown projection, give BOTH formats:
1. PlantUML/Mermaid markup (for rendering in tools that support it)
2. ASCII art representation (for plain text viewing)

Present both formats for each diagram so the Architect can choose which to keep.

**Update Workflow State:**
- Phase Status remains: `IN PROGRESS`
- Last Updated: current timestamp

**Update the store index.** Once the `.html` and its `.md` projection are written — and again after
every revision, because the title can change — upsert this folder's line in the `## Documentation`
section of `.speccen/index.md`, in the form the governing skill defines (governing skill →
Navigation). Touch that section only: create it, in its fixed place between Notes and
Reconciliation records, if it is missing; replace this folder's line if it exists; otherwise
insert it sorted by `<id>`. Never regenerate the rest of the index. If `.speccen/index.md` does
not exist, skip this step and do not create the store — Phase 06 close-out or reconcile lists the
folder when the store is first created.

### Step 3 — Present Completed Documentation

> "Documentation Generation Phase complete. The DOCUMENTATION document is ready at [path to the .html] (with its reduced .md projection). Please review and provide feedback or approve."

**STOP.** Ask with one `AskUserQuestion` call: header `Document`, options `Approve`, `Request
changes`. Wait for the answer.

### Step 4 — Iterate or Complete

**If changes requested:**
- Add change request as new row in Prompt Log table
- Update document, then update the store index line again
- Present revision
- Wait for approval

**If approved:**
1. Update Workflow State table:
   - Phase Status: `COMPLETE`
   - Last Updated: current timestamp
2. Add completion date to Phase History table (update Completed column for DOCUMENTATION GENERATION PHASE)
3. Add approval as new row in Prompt Log table
4. **Git commit**: `git commit -m "chore: complete DOCUMENTATION GENERATION PHASE [skip ci]"` — the
   commit includes the updated `.speccen/index.md`
5. Documentation workflow complete

---

## DOCUMENTATION Template Structure

**All diagrams generated in both PlantUML/Mermaid and ASCII art formats.**

### Diagram Format Example

```markdown
### Architecture Diagram

**PlantUML:**
```plantuml
@startuml
[Component A] --> [Component B]
[Component B] --> [Database]
@enduml
```

**ASCII Art:**
```
     ,-----------.          ,-----------.
     |Component A|          |Component B|
     `-----------'          `-----------'
           |                      |
           |--------------------->|
           |                      |
           |                      v
           |                 ,--------.
           |                 |Database|
           |                 `--------'
```
```

### Documentation Sections (In Order)

1. **Workflow State** — Current phase, phase history (at top of document)
2. **Overview** — Purpose, scope, audience
3. **Architecture** — High-level design, architecture diagrams, patterns
4. **Service Contracts** — Business capabilities, business-facing interfaces (CRITICAL SECTION)
5. **Component API** — Internal component interfaces, implementation details
6. **Components** — Detailed component breakdown
7. **API / Interfaces** — Public APIs with examples (if exposing REST/GraphQL/etc.)
8. **Data Model** — Entities, relationships, ERDs
9. **Usage Examples** — Basic and advanced scenarios
10. **Configuration** — Settings, environment variables
11. **Dependencies** — Packages, libraries, external services
12. **Sequence Diagrams** — Interaction flows
13. **State Diagrams** — State machines and transitions
14. **Error Handling** — Exceptions, error codes
15. **Performance** — Characteristics, bottlenecks
16. **Security** — Authentication, authorization, data protection
17. **Testing** — Unit tests, integration tests, coverage
18. **Deployment** — Steps, configuration, rollback
19. **Monitoring** — Metrics, alerts, logging
20. **Deviations** — Deviations from planned approach during implementation
21. **Known Limitations** — Current constraints
22. **Future Enhancements** — Planned improvements
23. **Related Features** — Dependencies and relationships
24. **References** — Links to related docs
25. **Changelog** — Version history
26. **Prompt Log** — All prompts and AI responses (at bottom of document)

---

## Service Contracts Section (Critical)

**IMPORTANT DISTINCTION:**
- **Service Contracts** = Business-facing capability interfaces (e.g., `IBuildingManager`, `IBuildingEngine`, `IBuildingAccess`)
- **Component APIs** = Internal implementation interfaces (e.g., `IBuildingProcessor`, `IValidator`)

**Service Contracts are NOT every component interface** — they are specifically the interfaces that expose business capabilities to external consumers.

This section documents the **business layer** — how business capabilities are exposed and implemented.

**Include:**

**Business Capabilities:**
- What business capabilities does this service expose?
- What business problems does it solve?
- Who are the external consumers? (UI, APIs, other services)

**Service Contract Interfaces:**
- Business-facing interfaces (e.g., `IBuildingManager`, `IBuildingEngine`)
- NOT internal component interfaces (those go in Component API section)
- Interfaces that are:
  - Registered in dependency injection as services
  - Consumed by controllers/APIs/external boundaries
  - Exposed as public service endpoints

**Business Operations:**
- Operations exposed by the service contract
- What each operation does from a business perspective
- Business rules enforced

**Hosted In Components:**
- Which concrete components implement these service contracts?
- How are they registered/hosted?
- Deployment/hosting details

**Contract Diagrams (PlantUML + ASCII):**
- Service contract overview showing consumers and providers
- Which components host which service contracts
- External consumers → Service Contracts → Hosting Components

**Data Contracts:**
- Request/response message structures for business operations
- DTOs exposed at the service boundary
- Validation rules

**Behavioral Contracts:**
- **Preconditions:** What must be true before calling (business perspective)
- **Postconditions:** What will be true after calling (business perspective)
- **Invariants:** Business rules that remain true
- **Behavioral guarantees:** Idempotency, timeout constraints, error handling

**Contract Versioning:**
- How service contracts evolve over time
- Backward compatibility strategy for business consumers
- Deprecation policy

**Quality of Service:**
- SLA requirements (response time, availability)
- Throughput expectations
- Error handling guarantees from business perspective

---

## Component API Section

This section documents **internal component interfaces** used in the implementation layer.

**Include:**

**Component Interfaces:**
- Internal interfaces consumed by service implementations
- Examples: `IBuildingProcessor`, `IValidator`, `IRepository`
- Interfaces that are:
  - Used internally by business services
  - NOT directly exposed to external consumers
  - Implementation details

**Purpose:**
- What does each component interface do?
- Why does it exist?
- Which service contracts depend on it?

**Operations:**
- Methods exposed by the component interface
- Technical details (not business-level operations)

**Dependencies:**
- What does this component depend on?
- What depends on this component?

**Usage:**
- How is this component used internally?
- Code examples showing typical usage

---

## Deviations Section

This section documents deviations from the planned approach that were discovered during implementation.

**Include:**

**Deviation Entry Format:**

```markdown
### Deviation N — YYYY-MM-DD

| Field | Info |
|---|---|
| **Planned** | [What the original plan/documentation specified] |
| **Actual** | [What was actually implemented and why the plan couldn't be followed] |
| **Reason** | [Root cause — why the deviation was necessary] |
| **Impact** | [What had to change as a result] |
| **Decision** | [APPROVED / REJECTED / PENDING — with rationale] |
```

**Example:**

```markdown
### Deviation 1 — 2026-03-10

| Field | Info |
|---|---|
| **Planned** | Conditional thinking block rendered inside the bot message `<Padder>` using `@if (!string.IsNullOrEmpty(message.ThinkingContent))` as a child of `<Padder>`. |
| **Actual** | `<Padder>` in RazorConsole does not support dynamic child counts. Placing `@if` blocks inside `<Padder>` (including the `@if (message.IsUser)` branch) caused the component to fail to render any children. |
| **Reason** | The original codebase establishes a clear convention: `<Rows>` handles dynamic/conditional children; `<Padder>` always receives a fixed set of children. The Implementation Plan did not account for this RazorConsole-specific constraint. |
| **Impact** | Phase 3.2 (rendering loop) must be restructured. Conditional content must live at the `<Rows>` level. Each `<Padder>` must have exactly 3 fixed children. Two separate `<Padder>` instances are used for bot messages. |
| **Decision** | APPROVED — self-evident fix from existing codebase convention. |
```

**When to add a Deviation:**
- Implementation discovered that planned approach won't work
- Codebase constraints not captured in planning phase
- Performance/security issues require different approach
- Third-party library behavior differs from documentation
- Architect makes mid-implementation decision to change approach

**Deviations require Architect approval** — they represent changes to the agreed plan.

**Example:**

```markdown
## Service Contracts

### Business Capabilities

This component exposes:

1. **Building Processing**
   - **Purpose:** Process building information and generate structural analysis
   - **Consumers:** Building Management UI, Import Service, Mobile App
   - **Business Rules:** Must validate building data before processing

### Service Contract Overview

**PlantUML:**
```plantuml
@startuml
interface IBuildingProcessor {
  + ProcessBuilding(request: BuildingRequest): BuildingResponse
  + ValidateBuilding(buildingId: Guid): ValidationResult
}

component BuildingProcessor implements IBuildingProcessor
component Client1 --> IBuildingProcessor
component Client2 --> IBuildingProcessor
@enduml
```

**ASCII Art:**
```
┌─────────────────────────────┐
│   IBuildingProcessor        │
│ ─────────────────────────── │
│ + ProcessBuilding()         │
│ + ValidateBuilding()        │
└──────────▲──────────────────┘
           │ implements
┌──────────┴──────────────────┐
│  BuildingProcessor          │
└─────────────────────────────┘
     ▲              ▲
     │              │
  Client1        Client2
```

### Contract Operations

#### ProcessBuilding

**Signature:**
```csharp
BuildingResponse ProcessBuilding(BuildingRequest request)
```

**Business Capability:** Process building information and generate structural analysis

**Preconditions:**
- Request must not be null
- Building ID must be valid GUID
- User must have ProcessBuilding permission

**Postconditions:**
- BuildingResponse returned with processing status
- Building marked as processed in database
- Audit log entry created

**Behavioral Contract:**
- **Must** validate all input before processing
- **Must** be idempotent (same input = same output)
- **Must** complete within 5 seconds or throw TimeoutException
- **Must** rollback changes if processing fails

**Data Contract (Request):**
```csharp
public class BuildingRequest
{
    public Guid BuildingId { get; init; }
    public string BuildingType { get; init; }
    public BuildingData Data { get; init; }
}
```

**Data Contract (Response):**
```csharp
public class BuildingResponse
{
    public Guid ProcessingId { get; init; }
    public ProcessingStatus Status { get; init; }
    public ValidationResult[] Validations { get; init; }
}
```

**Exceptions:**
- `ArgumentNullException` — Request is null
- `InvalidBuildingException` — Building data is invalid
- `TimeoutException` — Processing exceeded 5 seconds
- `UnauthorizedException` — User lacks permission

### Contract Versioning

**Current Version:** v2.0

**Version History:**
- v2.0 (2025-01): Added idempotency requirement
- v1.5 (2024-06): Added timeout constraint
- v1.0 (2023-12): Initial contract

**Backward Compatibility:**
- v1.x clients supported until 2026-12
- Deprecated: `ProcessBuildingLegacy` operation (remove in v3.0)

### Quality of Service

**SLA Requirements:**
- **Availability:** 99.9% uptime
- **Response Time:** P95 < 2 seconds, P99 < 5 seconds
- **Throughput:** Support 1000 requests/minute
- **Error Rate:** < 0.1% for valid requests
```

---

## Git Commit Protocol

At each phase transition, after updating Workflow State:

1. Check if DOCUMENTATION document is in a git repository
2. Check if git is configured (user.name, user.email)
3. If both pass: `git commit -m "chore: complete [PHASE_NAME] [skip ci]"`
4. If fails: continue silently (no error)

**Commit messages:**
- Planning complete: `chore: complete DOCUMENTATION PLANNING PHASE [skip ci]`
- Generation complete: `chore: complete DOCUMENTATION GENERATION PHASE [skip ci]`

This creates automatic checkpoints at phase boundaries for audit trail.

---

## Gate Enforcement

| Gate | Condition |
|---|---|
| PLANNING → GENERATION | Architect signals "proceed to documentation generation" |
| GENERATION → COMPLETE | Architect approves documentation |
| GENERATION → REVISION | Architect requests changes |

---

## What This Skill Does

- **Tracks workflow state** (current phase, phase history)
- **Logs all prompts** and AI responses for audit trail
- **Commits to git** at phase transitions
- **Reads pre-populated DOCUMENTATION.md** if Architect created it
- **Generates comprehensive documentation** with dual-format diagrams
- **Lists the documentation in the store index** — its own line in the `## Documentation`
  section of `.speccen/index.md`, nothing else in the index
- **Emphasizes Service Contracts** as critical business capability layer

---

## What This Skill Does NOT Do

- Does not generate documentation without Architect approval at gates
- Does not skip Documentation Planning Phase (unless pre-populated)
- Does not self-approve structure
- Does not auto-deploy documentation
- Does not modify Workflow State without explicit phase completion
- Does not regenerate the store index, and does not create `.speccen/` — it only upserts its own
  Documentation line in an index that already exists

---

## Quality Criteria

**Planning Phase complete:**
- [ ] Workflow State table updated (Phase Status = COMPLETE)
- [ ] Context and scope gathered
- [ ] Structure proposed
- [ ] Architect approved OR provided feedback
- [ ] Git commit created (if in repo)

**Generation Phase complete:**
- [ ] Workflow State table updated (Phase Status = COMPLETE)
- [ ] All approved sections populated
- [ ] Service Contracts thoroughly documented
- [ ] Diagrams created (both PlantUML/Mermaid and ASCII)
- [ ] Prompt Log maintained throughout
- [ ] The folder's line in the `## Documentation` section of `.speccen/index.md` is current (or the store does not exist yet)
- [ ] Architect approved documentation
- [ ] Git commit created (if in repo)