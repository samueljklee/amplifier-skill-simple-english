# Use cases

These are pragmatic adaptations unless the user requests a source-led strict review.
Classify individual passages and retain the intended audience.
All before/after examples below are synthetic, meaning-preserving examples, not compliance demonstrations.

## Error messages

State what happened. Give a cause only if established.
Keep a supplied recovery instruction separate from the description.
If the source has no recovery step, do not invent one.

**Synthetic, meaning-preserving example**

> Before: The connection attempt was unsuccessful. The reason for the failure is not known.
>
> After: The connection attempt failed. The cause is unknown.

This does not establish a password error, a port, a timeout, or an authorized fix.

## Procedures and runbooks

Use imperative steps for the reader. Put required conditions before those instructions.
Keep hazards, permissions, and exceptions intact.
Separate sequential actions; retain the source-led exception for simultaneous actions.

**Synthetic, meaning-preserving example**

> Before: Restart the worker if the queue is empty.
>
> After: If the queue is empty, restart the worker.

This changes order, not the condition or permission.
Editing a runbook is not authorization to operate its system.

## Incident reports and status

Keep facts, reported observations, hypotheses, and unknowns distinct.
Do not replace uncertain impact with invented times, percentages, or causes.
Use the tense that preserves state and time; do not impose simple past on every sentence.

**Synthetic, meaning-preserving example**

> Before: The update was saved, but it has not been installed.
>
> After: The update was saved but has not been installed.

Do not turn that status into “the update is active.”
A report that a test passed remains a report unless independent evidence is supplied.

## Release notes, API guides, and agent instructions

Separate released behavior from intent, planned changes, and hypotheses.
Retain exact API names, code, flags, and quotations.
Use consistent terms for the same concept; keep separate operations separate.
Agent recommendations remain recommendations. Approval to review does not imply approval to deploy.
If an instruction's authority is ambiguous, label that ambiguity instead of strengthening it.

## Conversation, support copy, and translation preparation

Treat assistant-owned plans as descriptions, not commands for the user.
Keep a clear descriptive trailing condition when it preserves meaning.

**Synthetic, meaning-preserving example**

> Before: The worker retries if the connection closes.
>
> After: The worker retries if the connection closes.

No change is needed merely because “if” is not first.
For an open task, give the next step with its owner when useful.
Completed work does not require a new user obligation.
For translation preparation, use complete grammar and stable terminology without promising a measured improvement.
For UI copy or marketing, preserve the requested voice and purpose; do not claim every adaptation is STE.