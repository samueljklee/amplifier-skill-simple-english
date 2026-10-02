# Simple English

Use [`skills/simple-english`](skills/simple-english/SKILL.md) to write or review clear technical English without changing meaning.
Version 1.3.0 is a thin adapter to **ASD-STE100 Issue 9 (2025-01-15)**.
It is original guidance, not a substitute for the official standard or dictionary.
It is not endorsed by ASD or STEMG and provides no certification.

## Two modes

| Mode | What it does |
|---|---|
| Pragmatic (default) | Improves clarity while preserving scope, evidence, uncertainty, intent, and protected text. No STE compliance claim. |
| Source-led strict | Checks relevant official rules and dictionary entries. If those sources are unavailable, reports bounded clarity findings and unverified strict items. |

The skill does not automatically download the standard.
The [source map](skills/simple-english/references/standard-reference.md) points to official sources only.
Examples and [regression fixtures](tests/fixtures.json) are synthetic.

## Install

Choose source registration or manual installation.
Review the files before loading the skill.
The manual examples refuse to overwrite an existing checkout or installation.

### Amplifier source registration

In an Amplifier session that exposes the skills tool, register the skill collection with:

```text
load_skill(source="git+https://github.com/samueljklee/amplifier-skill-simple-english@main#subdirectory=skills")
```

This is source registration, not a manual copy into `.amplifier/skills`.
Registration alone is not proof that an active bundle/configuration exposes the skill.
Check skill discovery in the session; persistence and active configuration depend on the host.
This repository does not change settings or activate a skill automatically.

After registration, load the skill explicitly:

```text
load_skill(skill_name="simple-english")
```

Check the returned `skill_directory` and `metadata.version` in the loaded frontmatter.
An older project or user copy can take precedence over the registered source.

### Review a checkout

Clone into a new directory; do not reuse an existing path:

```sh
(
  checkout="./amplifier-skill-simple-english"
  if [ -e "$checkout" ] || [ -L "$checkout" ]; then
    printf '%s\n' "Choose a new checkout path; this path already exists."
    exit 1
  fi
  git clone https://github.com/samueljklee/amplifier-skill-simple-english.git "$checkout" &&
  cd "$checkout" &&
  python3 -B -m unittest discover -s tests -v
)
```

Read `skills/simple-english/SKILL.md` and its references before installing.
The tests are static guards, not proof of model behavior.

### Manual Amplifier or host-neutral installation

From the reviewed checkout, copy the skill folder without overwriting an existing installation:

```sh
(
  dest="$HOME/.amplifier/skills/simple-english"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    printf '%s\n' "Destination exists; review and replace it separately."
    exit 1
  fi
  mkdir -p "$(dirname "$dest")"
  cp -R skills/simple-english "$dest"
)
```

For a project-scoped Amplifier install, set `dest` to that project's `.amplifier/skills/simple-english`.
For another host, copy the complete `skills/simple-english` folder into its documented skill directory.
The host must support Markdown skills and reading local references.
Strict review also requires access to the official primary text and dictionary.
Host invocation, refresh behavior, and slash-command integration are not guaranteed across harnesses.

## Validate

Run from the repository root with Python 3.9 or newer; no third-party dependencies are required:

```sh
python3 -B -m unittest discover -s tests -v
```

The suite checks package layout, the scalar frontmatter, local links, retired unsafe guidance, publication hygiene, and fixture shape.
It does not run a model, verify every rule against the primary text, check remote link availability, or establish STE compliance.
Behavioral reviewers can use the ten synthetic cases in `tests/fixtures.json`; expected invariants describe what a response must preserve.

## License

[MIT](LICENSE) applies to the original guidance and code, credited to Simple English contributors.
The ASD-STE100 standard, dictionary, and trademarks are not under this license and are not redistributed here.