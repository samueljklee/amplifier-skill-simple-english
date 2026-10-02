# Review checklist

This is an original review aid, not a complete STE audit or a replacement dictionary.
Apply the meaning gate in [SKILL.md](../SKILL.md) before changing words.
For strict findings, verify the relevant entry or rule in [the official source](standard-reference.md).

## 1. Preserve the source

- Retain actor, recipient, global scope, time, state, conditions, and approval boundaries.
- Retain recommendation, permission, uncertainty, and the difference between fact and hypothesis.
- Keep reported evidence separate from independently established evidence.
- Retain quantities, approximations, and hazards. Do not invent a cause or a remedy.
- Compare all protected content byte for byte: code, identifiers, commands, quotes, names, and diagrams.

An unclear actor can stay unclear. A shorter sentence is not safer if it asserts more.
If the source cannot support a rewrite, label the ambiguity or unsupported claim.

## 2. Classify before searching

Identify reader instructions, descriptive passages, notes, and assistant-owned plans.
Decide whether each finding is a clarity suggestion, an official requirement, or a GR recommendation.
The patterns below locate candidates, not automatic violations.

| Candidate | Question before editing |
|---|---|
| Contractions; perfect or progressive forms | Is this protected text? Would a simpler form change time, completion, or continuity? In strict mode, consult Sections 3 and 4. |
| “should”, “would”, “may”, “might”, “could” | Is this recommendation, expectation, permission, possibility, or hypothesis? Verify strict vocabulary; do not strengthen intent. |
| “-ing” words or clauses | Is this a verb, adjective, technical noun, or part of a name? Consult the relevant rule and entry. |
| Semicolons | Can the sentence split without losing its relationship? Check Rule 8.1 in strict mode. |
| Latin abbreviations | Would expansion preserve meaning? Treat GR-6 as a recommendation, not a mandatory rule. |
| “simply”, “robust”, “aims to”, “reported” | Does the word carry a claim, state, or evidence boundary? Delete only meaning-free filler. |
| Mid-sentence “if” or “when” | Is a required condition after a reader instruction? Rule 5.4 does not force every descriptive condition to the front. |
| Repeated “check”, “validate”, “run”, “execute” | Are these the same operation? Do not merge different operations to reduce vocabulary. |

An apostrophe can mark possession rather than a contraction.
Search results do not establish a word's grammatical role or dictionary approval.

## 3. Count and inspect structure

In strict mode, verify these checks against the primary text and the passage's role:

| Check | Lookup and scope |
|---|---|
| Sentence length | Rules 5.1 and 6.3: 20 words per procedural sentence; 25 per descriptive sentence, including notes |
| Multiple instructions | Rule 5.2: check the exception for simultaneous actions before splitting |
| Required conditions | Rule 5.4: condition before the reader's instruction; not a mandate for descriptive prose |
| Multi-word nouns | Rules 2.1 and 2.2: check the established longer-name exception rather than renaming every noun |
| Parentheses | Rule 8.5: count parenthetical text as one word in the outer sentence and count its contents separately |
| Special counting categories | Rule 8.6: verify the actual category; a generic multi-word name is not automatically one word |
| Hyphenated units | Rule 8.7: verify counting and valid hyphenation; do not add hyphens just to reduce a count |

Count every sentence in the declared audit scope, not only the three longest.
A whitespace count is a rough screen, not an implementation of official STE counting.
In pragmatic mode, sentence-length targets serve clarity; they do not override semantic preservation.
Check notes, paragraphs, voice, warnings, and vocabulary against relevant source sections as needed.
Do not invent an actor to replace a passive construction.
Do not insert “then” or “because” if the source does not establish sequence or causation.

## 4. Verify disputed vocabulary selectively

Read the actual dictionary entry, including part of speech, meaning, forms, and restrictions.
Check technical nouns in context and technical verbs against Rule 1.12.
For “delete” or any other domain verb, assess eligibility and whether an approved alternative is accurate.
Do not assume that “erase” describes removal of every software object.
Keep a configuration file, an option, and a panel distinct.
Keep validation, execution, authentication, and authorization distinct.
Restructure only when both wording and preserved meaning can be verified.

## 5. Report the scope honestly

Give each finding a label: **clarity suggestion**, **verified strict finding**, **GR recommendation**, or **unverified strict item**.
For a verified finding, identify the official issue, section/rule or dictionary entry, and passage reviewed.
Give the offending text and a meaning-preserving rewrite when one is verified.
An unresolved semantic ambiguity is not a compliant rewrite.
If the primary text or dictionary is unavailable, name the unverified checks and give only a bounded clarity review.
A partial review is not a full audit, certification, or a claim of compliance.