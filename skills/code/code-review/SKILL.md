---
name: code-review
description: Review code implementations against ANALYSIS documents, project conventions, and security standards. Use when reviewing PRs, validating implementations, or auditing code quality. Produces structured Review Reports for human and AI review. Optionally creates GitHub Issues for actionable findings.
---

# Code Review Skill

AI-augmented code review that validates implementations against blueprints, conventions, and best practices. Works standalone or integrated with Analysis-Gated Workflow.

---

## When to Use This Skill

- Reviewing pull requests, human or AI-authored
- Validating implementations against ANALYSIS documents
- Auditing code for security issues and convention compliance
- Final review gate before merging to main
- Post-implementation quality checks
- Creating GitHub Issues for actionable findings directly from the review

---

## How It Works

This skill performs **state-based review** — it reviews the current codebase state, not authorship. The code may have been written by AI, human, or both. The review assesses whether the current state meets requirements and quality standards.

### Skill Invocation Protocol

At the start of every review session:

0. A **multiple-choice** question uses the **`AskUserQuestion` tool**, not prose and not a table.
   The tool's constraints, the empty-answer guard and the prose fallback for hosts without it
   are those of `skills/sdd/00-governing-workflow/SKILL.md` → "Structured questions": 1–4
   questions per call, 2–4 options each, never add an "Other" option, headers ≤ 12 characters.
   On an empty answer, or without the tool, fall back to one short plain-text question per
   field — never proceed on an assumed selection. A fact you can find is never asked for —
   look it up, or offer it as an option.
1. Resolve the **feature or refactoring name** (same as used in ANALYSIS document, if present)
   and the **review scope** with one `AskUserQuestion` call, two questions:
   - header `Name` — `Use name from arguments` (only if given), `Review <name>` for each (up to
     2) feature name found in `.speccen/reviews/`, `.speccen/bundles/` or an `*_ANALYSIS.md`,
     and `I'll type it` — "Select Other and type the exact name". Never propose invented names.
   - header `Scope` — `This branch vs the base branch (Recommended)` (name the detected base),
     `Uncommitted changes`, `Whole working directory`; "Select Other to name files/folders or a
     base commit SHA"
2. Resolve the **working folder** where the Review Report is stored — never ask for it. All
   output lives under `.speccen/`, in `.speccen/reviews/<id>/`, with `<id>` in the `.speccen` id
   format `<prefix>.<name_snake_case>` (e.g. `2026-11-02.building_information_processor`). If a
   folder `.speccen/reviews/*.<name_snake_case>` already exists, reuse it (repeat reviews of the
   same feature accumulate there, told apart by the timestamp); otherwise create it with today's
   date as the prefix.
3. Set:
   - `{{FEATURE_NAME}}` = the name provided (use as-is, no normalisation)
   - `{{FOLDER_NAME}}` = the folder resolved in step 2
   - `{{FEATURE_NAME_UPPERCASE}}` = feature name converted to SCREAMING_SNAKE_CASE
   - Review Report path = `{{FOLDER_NAME}}/{{FEATURE_NAME_UPPERCASE}}_REVIEW_{{ISO_TIMESTAMP}}.md`
     where `{{ISO_TIMESTAMP}}` is the current date and time in ISO 8601 format: `YYYYMMDD_HHMMSS`
   - Example: "Building Information Processor" → `BUILDING_INFORMATION_PROCESSOR_REVIEW_20260218_143022.md`
4. Look for an ANALYSIS document: first `{{FOLDER_NAME}}/{{FEATURE_NAME_UPPERCASE}}_ANALYSIS.md`,
   then the matching speccen bundle under `.speccen/bundles/`, then a path the user names
   - If present, use it as the review blueprint
   - If absent, review against project conventions only

### Review Process

1. **Gather Context**
   - Locate ANALYSIS document (if present)
   - Read project conventions (.claude/, .github/)
   - Identify git changes since implementation started
   
2. **Perform Review**
   - Cross-reference code against ANALYSIS document
   - Check compliance with project conventions
   - Scan for security issues, such as null checks, input validation, error handling
   - Identify deviations from Implementation Plan
   - Flag code quality issues
   
3. **Produce Review Report**
   - Categorize findings by severity (CRITICAL, HIGH, MEDIUM, LOW, INFO)
   - Document what changed between implementation and current state
   - Provide actionable recommendations
   
4. **Human Decision**
   - Architect reviews findings
   - Approves, requests changes, or rejects

5. **GitHub Issues (Optional)**
   - After the Review Report is saved, ask the user if they want to create GitHub Issues
   - If yes, follow the [GitHub Issues Creation Protocol](#github-issues-creation-protocol) below

---

## GitHub Issues Creation Protocol

After the Review Report is saved, ask the user if they want to create GitHub Issues for the findings. Only **Must Fix (Blocking)** and **Should Fix (Non-blocking)** items are eligible.

### Step 1 — Ask if the user wants to create issues

Ask with one `AskUserQuestion` call: header `Issues`, question "The Review Report has been saved.
Create GitHub Issues for the findings?", options `No`, `Yes — create GitHub Issues`.

If **No**, skip the rest of this protocol and summarize the review session.

### Step 2 — Collect required information

One `AskUserQuestion` call, three questions:

1. header `Repository` — the repo detected from `git remote get-url origin`, as `owner/repo
   (Recommended)`; "Select Other to type a different `owner/repo`". If no remote is found, ask in
   plain text.
2. header `Findings` — `All Must Fix and Should Fix (Recommended)`, `Must Fix only`, `Should Fix
   only`, `Pick individually` — with the counts of each. On `Pick individually`, list the
   eligible findings as a numbered list in chat and take the numbers as the answer.
   - Must Fix items → will be created as Bug issues
   - Should Fix items → will be created as Task issues
3. header `Label` — `review-finding only (Recommended)`, `tech-debt`; "Select Other to add another
   common label to all issues"

### Step 3 — Map findings to issue types

| Recommendation Category | GitHub Issue Type | Label        |
|------------------------|-------------------|--------------|
| Must Fix (Blocking)    | Bug               | `bug`        |
| Should Fix (Non-blocking) | Task           | `task`       |

Always add the label `review-finding` automatically in addition to any user-specified labels.

### Step 4 — Generate issue content

For each selected finding, generate:

**Issue Title:**
```
[SEVERITY] <Finding Title>
```
Example: `[CRITICAL] Missing null check in UserService.GetById`

**Issue Body:**
```markdown
## Review Finding

**Severity:** {{SEVERITY}}
**File:** {{FILE_PATH}}:{{LINE}}
**Review Report:** {{FOLDER_NAME}}/{{FEATURE_NAME_UPPERCASE}}_REVIEW_{{ISO_TIMESTAMP}}.md

## Description

{{FINDING_DESCRIPTION}}

## Evidence

{{CODE_SNIPPET_OR_REFERENCE}}

## Recommendation

{{RECOMMENDATION}}

---
*Generated by Code Review Skill from review report `{{FEATURE_NAME_UPPERCASE}}_REVIEW_{{ISO_TIMESTAMP}}.md`*
```

### Step 5 — Present confirmation summary

Before executing anything, present a clear summary of what will be created and ask for final approval:

```
I'm ready to create N GitHub Issues in {{GITHUB_REPO}}:

  [BUG]  [CRITICAL] <Finding Title 1>
  [BUG]  [HIGH]     <Finding Title 2>
  [TASK] [HIGH]     <Finding Title 3>

Labels: bug / task + review-finding{{, USER_LABEL}}

```

Then ask with one `AskUserQuestion` call: header `Create`, options `Create now`, `Edit the
list`, `Cancel`. Wait for the answer. Do not execute any commands until the user picks `Create now`.

### Step 6 — Execute gh CLI commands

Once the user confirms, check whether `gh` is available and authenticated:

```bash
gh auth status
```

**If `gh` is available and authenticated** — execute each issue creation directly:

```bash
gh issue create \
  --repo "{{GITHUB_REPO}}" \
  --title "[CRITICAL] <Finding Title>" \
  --body "<issue body>" \
  --label "bug,review-finding{{,USER_LABEL}}"
```

After each successful creation, report the issue URL returned by `gh`. When all issues are created, summarize:

```
✅ Created 3 GitHub Issues in {{GITHUB_REPO}}:
  #42 [BUG]  [CRITICAL] Missing null check in UserService.GetById
  #43 [BUG]  [HIGH] No error handling in OrderController.Submit
  #44 [TASK] [HIGH] Missing input validation on CreateOrder endpoint
```

**If `gh` is not available or not authenticated** — fall back to outputting all commands in a single fenced code block for the user to run manually, followed by a collapsible markdown fallback for manual creation in GitHub:

```markdown
<details>
<summary>GitHub Issues — Manual Creation</summary>

### Issue 1: [CRITICAL] <Finding Title>
**Type:** Bug | **Labels:** `bug`, `review-finding`

[issue body]

---

### Issue 2: [HIGH] <Finding Title>
**Type:** Task | **Labels:** `task`, `review-finding`

[issue body]

</details>
```

### Rules

- Only include findings the user confirmed in Step 2
- Never execute `gh` commands without the explicit confirmation in Step 5
- If no Must Fix or Should Fix findings exist, inform the user and skip this protocol
- If no repository can be detected or was given, ask before proceeding
- Do not generate issue content for MEDIUM, LOW, or INFO findings
- If `gh` execution fails for any individual issue, report the error and continue with the remaining issues

---

## Inputs (Flexible)

### Required
- **Current codebase** — the working directory being reviewed

### Optional (Auto-detected)
- **ANALYSIS document** — blueprint for the implementation (searches common paths)
- **Implementation Plan** — within ANALYSIS document
- **Project conventions** — .claude/ and .github/ folders
- **Git history** — to identify delta between implementation commit and current HEAD
- **Feature branch** — to compare against base branch

### User-Specified
- Path to ANALYSIS document if not in standard location
- Base commit SHA for comparison (set through "Other" on the `Scope` question)
- Specific files/folders to review, or a different base (set through "Other" on the `Scope` question)

---

## Invocation

### Standalone Usage

The skill will prompt you for:
1. Feature or refactoring name
2. Folder for storing the Review Report

Then it will:
- Check for an ANALYSIS document at the standard path
- Review the current codebase state
- Produce a Review Report

```bash
# Review current working directory
/code-review

# The skill will ask for the feature name; the output folder is always .speccen/reviews/<id>/
```

### Integrated with Analysis-Gated Workflow

When invoked from Phase 06 of the workflow, the skill automatically uses:
- Feature name from the ANALYSIS document
- The review folder `.speccen/reviews/<id>/` (always under `.speccen/`)
- Existing ANALYSIS document as the review blueprint

---

## Review Checklist

The skill evaluates the current codebase against these criteria:

### Functional Requirements
- [ ] Does the implementation satisfy the original feature request?
- [ ] Are all acceptance criteria met?
- [ ] Does it align with the Implementation Plan intent (if ANALYSIS document exists)?

### Project Conventions Compliance
- [ ] CRITICAL/MANDATORY rules from .claude/ and .github/ followed?
- [ ] Naming conventions respected?
- [ ] Architecture boundaries respected?
- [ ] Technology constraints followed (e.g., .NET version restrictions)?
- [ ] Critical workflows followed (migrations, code generation)?

### Code Quality
- [ ] **Simplicity First** — is the solution as simple as possible?
- [ ] **Minimal Impact** — only necessary code changed?
- [ ] **No Temporary Fixes** — no TODOs, placeholders, or "fix later" code?
- [ ] **Senior Developer Standards** — production-ready quality?
- [ ] No unnecessary comments or over-documentation?

### Security & Safety
- [ ] Input validation present and correct?
- [ ] Null safety — all code paths checked for null dereference?
- [ ] Error handling appropriate?
- [ ] No hardcoded secrets or sensitive data?
- [ ] Authentication/authorization checks in place where needed?

### Deviations & Scope
- [ ] Were there unauthorized deviations from the Implementation Plan?
- [ ] Was scope creep introduced (unrelated refactoring, style changes)?
- [ ] Were new dependencies added without approval?

### Change Delta (if git available)
- [ ] What changed between implementation commit and current HEAD?
- [ ] Were changes made by humans after AI implementation?
- [ ] Do human changes introduce issues?

---

## Review Report Format

The skill produces a structured **Review Report** saved as:
`{{FOLDER_NAME}}/{{FEATURE_NAME_UPPERCASE}}_REVIEW_{{ISO_TIMESTAMP}}.md`

Example: `BUILDING_INFORMATION_PROCESSOR_REVIEW_20260218_143022.md`

This naming convention:
- Matches the ANALYSIS document convention (if present)
- Uses SCREAMING_SNAKE_CASE for feature name
- Includes ISO 8601 timestamp for multiple reviews of the same feature
- Makes Review Reports easy to locate together under `.speccen/reviews/`

### Report Structure

Filename: `{{FEATURE_NAME_UPPERCASE}}_REVIEW_{{ISO_TIMESTAMP}}.md`

```markdown
# [FEATURE_NAME] Implementation Review 

**Date:** YYYY-MM-DD HH:MM  
**Reviewer:** [Reviewer name — never the AI] (with [AI model name] co-review)  
**Branch/Commit:** [branch name or commit SHA]  
**ANALYSIS Document:** [path or "None"]

---

## Summary

**Overall Assessment:** [APPROVED / CHANGES REQUESTED / REJECTED]  
**Critical Issues:** [count]  
**High Priority Issues:** [count]  
**Medium Priority Issues:** [count]  
**Low Priority Issues:** [count]  

**Key Findings:**
- [Brief summary of most important findings]

---

## Findings by Category

### CRITICAL Issues

#### [Issue Title]
**Severity:** CRITICAL  
**File:** path/to/file.cs:line  
**Description:** [What the issue is]  
**Evidence:** [Code snippet or reference]  
**Recommendation:** [How to fix]  
**Reference:** [ANALYSIS doc section or convention rule that was violated]

---

### HIGH Priority Issues
[Same format as CRITICAL]

---

### MEDIUM Priority Issues
[Same format]

---

### LOW Priority Issues
[Same format]

---

### INFO / Observations
[Same format, for non-issues worth noting]

---

## Compliance Assessment

### Project Conventions
- ✓ CRITICAL/MANDATORY rules followed
- ✓ Naming conventions respected
- ⚠ [Any violations]

### Implementation Plan Alignment
- ✓ All planned phases completed
- ✓ No unauthorized deviations
- ⚠ [Any deviations documented]

### Code Quality Standards
- ✓ Simplicity First principle followed
- ✓ Minimal Impact maintained
- ⚠ [Any violations]

---

## Change Delta Analysis

**Implementation Commit:** [SHA]  
**Current HEAD:** [SHA]  
**Changes Since Implementation:** [file count]

### Modified by Humans Post-Implementation
| File | Lines Changed | Type of Change | Issues Introduced? |
|---|---|---|---|
| path/to/file.cs | +25 / -10 | Refactoring | None |
| path/to/other.cs | +5 / -0 | Bug fix | ⚠ Missing null check |

---

## Recommendations

### Must Fix (Blocking)
1. [Issue that must be resolved before merge]
2. [Another blocking issue]

### Should Fix (Non-blocking but important)
1. [Issue that should be addressed]
2. [Another important issue]

### Consider (Optional improvements)
1. [Suggestion for improvement]
2. [Another suggestion]

---

## Approval Status

**Status:** [APPROVED / CHANGES REQUESTED / REJECTED]

**Rationale:**
[Why this status was assigned]

**Next Steps:**
[What should happen next]
```

---

## What This Skill Does

- **Scans the current codebase state** (not just AI-written code)
- **Cross-references against ANALYSIS document** (if present)
- **Validates project conventions** from .claude/ and .github/
- **Identifies security issues** (null safety, input validation, error handling)
- **Flags deviations** from Implementation Plan
- **Documents change delta** (what changed since implementation)
- **Produces actionable Review Report** for human and AI consumption
- **Categorizes findings by severity** (CRITICAL → INFO)
- **Creates GitHub Issues** for Must Fix and Should Fix findings (optional) — executes via `gh` CLI after confirmation, falls back to commands + markdown if `gh` is unavailable

---

## What This Skill Does NOT Do

- Does not auto-approve implementations
- Does not fix issues automatically (reports only)
- Does not assume AI authorship (reviews all code equally)
- Does not replace human judgment (augments it)
- Does not gate workflow without human decision

---

## Integration Points

### With Analysis-Gated Workflow
- Can be invoked automatically at Phase 06
- Uses ANALYSIS document as review blueprint
- Respects Implementation Plan structure

### With Standard PR Review
- Works on any branch without ANALYSIS document
- Reviews against project conventions only
- Produces same Review Report format

### With AI Review Agents
- Review Report is structured for AI consumption
- Another AI model (e.g., Opus) can analyze findings
- AI can categorize, summarize, or deep-dive on specific issues

---

## Configuration (Optional)

Create `.claude/review-config.json` to customize review behavior:

```json
{
  "severity_thresholds": {
    "null_safety_violations": "CRITICAL",
    "missing_input_validation": "HIGH",
    "style_violations": "LOW"
  },
  "auto_detect_analysis_document": true,
  "analysis_document_paths": [
    "docs/*_ANALYSIS.md",
    "*_ANALYSIS.md"
  ],
  "exclude_patterns": [
    "**/node_modules/**",
    "**/bin/**",
    "**/obj/**"
  ],
  "require_human_approval": true
}
```

---

## Quality Criteria

A review is complete when:

- [ ] All configured checks have been performed
- [ ] Review Report is generated and saved
- [ ] Findings are categorized by severity
- [ ] Recommendations are actionable
- [ ] Human reviewer has visibility into findings
- [ ] Approval status is clearly stated