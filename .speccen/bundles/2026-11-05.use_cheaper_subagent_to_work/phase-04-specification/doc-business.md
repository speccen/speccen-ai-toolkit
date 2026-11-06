---
type: Doc
audience: business
expandable: true
status: COMPLETE
description: The main session corrects common errors in the bundle files before it starts the verifier
---

# Use cheaper subagent to work — Business Process & Experience (intent, seed)

## Capability
- The Architect sets the model tier for search questions in each phase, from Code Analysis to Implementation.
- A worker on that model tier answers each search question with evidence. The main session makes every decision.
- The main session corrects common errors in the bundle files before it starts the verifier.

## Business Process (end to end, intended)
1. The Architect starts a bundle. New projects get `model: economy` for the Specification and Implementation phases.
2. An existing project keeps its old behaviour. Its settings file gets the new keys with the value `inherit`.
3. During a phase, the main session sends a search question to a worker on the model tier of the phase.
4. The worker returns evidence: file locations and quotes only. The worker does not draw conclusions.
5. The main session opens each file location again before it uses the evidence.
6. At the end of an autonomous phase, the main session does five self-checks. The main session writes the results in the phase summary.
7. The verifier checks the gate.
8. If the main session must fix a row, the verifier does a second run. The second run checks only the failed rows and the rows that cite a changed file.

## Where It Will Surface (UI/UX)
- No screen. The feature shows in three places:
  - the project settings file `.speccen/speccen-config.yaml`;
  - the `log.md` lines that name the model of each worker and each verifier run;
  - the gate table in each phase summary.

## What Will Change For The User
- Before: every search question used the session model. After: each search question uses the model tier that the Architect sets.
- Before: a failed gate meant a full second verifier run. After: the second run checks only the failed rows and the rows that cite a changed file.

## Not Included
- The verifier stays on the session model.
- No separate setting for search questions. Search questions use the model tier of the phase.
- No default model for every worker on the host.
- The cost measurement on the next bundle is a follow-up.
