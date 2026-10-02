---
name: simple-english
description: "Write, rewrite, or review clear technical English. Use for documentation, procedures, status updates, or requests for STE or ASD-STE100."
license: MIT
compatibility: "Requires Markdown skill loading and local reference reading; strict review also requires access to the official standard and dictionary."
metadata:
  version: "1.3.0"
  standard: "ASD-STE100 Issue 9 (2025-01-15)"
---

# Simple English

Write plain technical English without changing what the source says.
This is a thin, unofficial adapter to ASD-STE100, not a replacement standard or dictionary.
Use it inline in the current task. It does not require a separate agent or a specific tool.
All illustrations are synthetic and preserve meaning; they are not compliance demonstrations.

## Choose the mode

| Mode | Use | Boundary |
|---|---|---|
| Pragmatic (default) | Clear documentation, messages, and conversation | Apply clarity guidance with judgment. Do not claim STE compliance. |
| Source-led strict | The user explicitly requests STE, ASD-STE100, or a compliance review | Read the applicable official rules and dictionary entries before judging them. |

In strict mode, use [the selective source map](references/standard-reference.md).
Read only relevant sections and entries, not the whole standard for each response.
Keep official requirements, general recommendations (GR), and this skill's chat adaptations distinct.
If the primary text or dictionary is unavailable, give a bounded clarity review.
Name unverified strict items. Do not guess rule IDs, word approvals, or compliance.
Cite a rule only after checking its official text against the passage.

## Meaning gate: before any substitution

Compare the source and proposed rewrite on these five dimensions:

1. **Actor, recipient, and scope.** Retain who acts, who receives the instruction, and what it covers.
   An unknown actor does not permit invention. “Files are unchanged” is not “I changed no files.”
2. **State and time.** Preserve completed, ongoing, planned, and hypothetical actions.
   Saved is not installed; recorded is not applied; an aim is not implemented behavior.
3. **Evidence and quantities.** Keep facts separate from reports, assumptions, and hypotheses.
   Reported success is not independent verification. Retain exact quantities and approximations.
4. **Intent and uncertainty.** Preserve recommendation, requirement, permission, possibility, and confidence.
   Do not make a recommendation a fact or obligation. Do not make a possible result certain.
5. **Conditions, risk, and authority.** Retain exceptions, prerequisites, hazards, and approval scope.
   Editing an instruction does not authorize execution. Ambiguous approval remains ambiguous.

Do not add causes, credentials, times, measurements, or fixes that the source does not establish.
Rewrite safely when possible. Otherwise label the unsupported claim or ambiguity.
Ask a focused question only when the missing information changes the task or a safe rewrite.

## Classify each passage and its reader

Reader instructions are **procedural**. Explanations, status, notes, and assistant-owned plans are **descriptive**.
A document can contain both; classify each passage rather than imposing one role on the whole document.
“I will inspect the log” describes the assistant's plan. It is not an instruction for the user.

For instructions, put a required condition before the reader's command.
This is the scope of Rule 5.4; it is not a rule for every occurrence of “if” or “when.”
A descriptive trailing condition can stay when it is clear and accurate.
Use one instruction per sentence, with the simultaneous-action exception in Rule 5.2.

Strict sentence limits are 20 words for procedural text and 25 for descriptive text.
Apply them per sentence using the official counting rules, including descriptive notes.
In pragmatic mode these are targets, not permission to delete meaning.
Split sentences without losing their relationships, qualifiers, or necessary grammar.

## Preserve intent when handling modals

Classify meaning before choosing words. There is no automatic modal substitution table.

| Source intent | Pragmatic treatment | Source-led strict treatment |
|---|---|---|
| Recommendation: “should” | Keep a meaningful recommendation | Look up the entry and restructure only if the same recommendation survives |
| Possibility: “may”, “might”, “could” | Retain uncertainty | Verify a formulation with the same uncertainty; do not assert certainty |
| Permission: “may”, “can” | Retain who permits what and under which conditions | Verify vocabulary without granting new authority |
| Requirement: “must”, sometimes “should” | Keep the established strength; flag ambiguity | Verify meaning and wording; do not infer a requirement from a suggestion |
| Hypothesis or expectation: “would”, “should” | Keep the premise and level of confidence | Restructure only when the same hypothetical or expected result is verified |

Keep meaningful “may” and “should” in pragmatic mode.
In strict mode, consult the relevant dictionary entry and verb rules.
If no verified, meaning-preserving rewrite is available, leave the issue explicitly unresolved.

## Vocabulary: same concept, same term

Use one term for the **same concept**, not one term for different operations or objects.
Keep a configuration file, an option, and a settings panel distinct.
Keep validation, execution, authentication, and authorization distinct.
Do not force an expression such as “operate recipe” to satisfy a replacement list.

In strict mode, verify each disputed word's part of speech, meaning, and allowed forms.
Technical nouns and technical verbs are contextual categories, not blanket vocabulary exemptions.
For a proposed technical verb, consult Rule 1.12 and its restrictions.
This includes “delete”: evaluate the actual technical operation and any approved, accurate alternative.
Do not assume either that every software verb qualifies or that an alternative means the same thing.

Remove filler only when it carries no meaning. Prefer familiar words when they remain accurate.
“Aims to”, “designed to”, and “reported” can carry essential state or evidence.
Do not delete them merely because they match a pattern.

## Protected content

Keep code, identifiers, command strings, flags, paths, exact quotes, names, and diagrams unchanged.
Modify them only when the user explicitly requests that modification.
Simplify surrounding prose instead. Preserve names even when a shorter generic noun looks easier.
Do not assume that a generic multi-word name counts as one word.
For strict counting, use Rules 8.5 and 8.6 and verify the applicable category.
Count parenthetical text as one word in the outer sentence and count its contents separately.
Check established longer technical names against the exception in Rule 2.2.

## Review before delivery

1. Compare the rewrite with the source using the meaning gate.
2. Check passage roles, audience, conditions, terminology, and protected content.
3. Use [the checklist](references/checklist.md) for candidate patterns and strict counting.
4. In strict mode, record which official rules and dictionary entries you actually checked.
5. Deliver the rewrite or findings with any unresolved meaning or verification limits.

Pattern hits are candidates, not violations. Classify their role and passage before judging them.
Checking only the three longest sentences is a sample, not a full sentence audit.
For a strict finding, give the source location, offending text, and a verified safe rewrite if available.
Label clarity suggestions, GR recommendations, and unverified strict items separately.
Do not describe a rewrite as certified or fully compliant on the strength of a partial review.

## Adapt to the task

Use [the use cases](references/use-cases.md) for errors, procedures, reports, and conversational updates.
Chat adaptations are not extra STE rules. Retain the user's audience, purpose, and requested format.
When relevant work remains open, end with one concrete next step and name who owns it.
Do not add an action request to every message or transfer assistant-owned work to the user.

The original guidance is MIT licensed. The standard, dictionary, and trademarks are not covered by that license.
This skill is not endorsed by ASD or STEMG and does not provide certification.