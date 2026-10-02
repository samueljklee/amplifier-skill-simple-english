"""Static package guards only: no model execution or STE compliance assessment."""

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/simple-english/SKILL.md"
EXPECTED_FILES = {
    ".gitignore",
    "AGENTS.md",
    "LICENSE",
    "README.md",
    "skills/simple-english/SKILL.md",
    "skills/simple-english/references/checklist.md",
    "skills/simple-english/references/use-cases.md",
    "skills/simple-english/references/standard-reference.md",
    "tests/fixtures.json",
    "tests/test_skill_package.py",
}
CASE_IDS = {
    "recommendation_and_possibility",
    "unknown_cause_and_approximation",
    "global_state_not_personal_action",
    "ambiguous_approval_gate",
    "conditions_and_passage_roles",
    "distinct_concepts_and_operations",
    "protected_content_unchanged",
    "saved_not_installed_and_reported_evidence",
    "aim_and_hypothesis_not_fact",
    "strict_source_unavailable",
}


def package_files():
    """Exclude Git metadata and normal Python caches, not publication artifacts."""
    return [
        path for path in ROOT.rglob("*")
        if path.is_file()
        and not {".git", "__pycache__"}.intersection(path.relative_to(ROOT).parts)
    ]


def parse_skill():
    """Validate the deliberately small scalar-only YAML subset used by this skill."""
    prefix, header, body = SKILL.read_text(encoding="utf-8").split("---\n", 2)
    if prefix:
        raise ValueError("Frontmatter must be first")
    fields = {}
    target = fields
    for line in header.splitlines():
        if line == "metadata:":
            if "metadata" in fields:
                raise ValueError("Duplicate metadata")
            target = fields["metadata"] = {}
            continue
        match = re.fullmatch(r'( {2})?([a-z][a-z_-]*): (".*"|[A-Za-z0-9.-]+)', line)
        if not match:
            raise ValueError("Use scalar frontmatter fields and one metadata mapping")
        indent, key, raw = match.groups()
        if bool(indent) != (target is not fields):
            raise ValueError("Unexpected field indentation")
        if key in target:
            raise ValueError("Duplicate field")
        target[key] = json.loads(raw) if raw.startswith('"') else raw
    return fields, body


class SkillPackageTests(unittest.TestCase):
    def test_minimal_package_layout(self):
        paths = {str(path.relative_to(ROOT)) for path in package_files()}
        self.assertEqual(paths, EXPECTED_FILES)
        self.assertFalse(any(path.is_symlink() for path in ROOT.rglob("*")))

    def test_portable_frontmatter(self):
        fields, _ = parse_skill()
        self.assertEqual(
            set(fields), {"name", "description", "license", "compatibility", "metadata"}
        )
        self.assertEqual(fields["name"], "simple-english")
        self.assertEqual(fields["license"], "MIT")
        self.assertEqual(fields["metadata"], {
            "version": "1.3.0",
            "standard": "ASD-STE100 Issue 9 (2025-01-15)",
        })
        self.assertTrue(1 <= len(fields["description"]) <= 1024)
        self.assertIn("Requires", fields["compatibility"])
        self.assertIn("official standard and dictionary", fields["compatibility"])

    def test_skill_body_is_thin(self):
        _, body = parse_skill()
        self.assertTrue(100 <= len(body.splitlines()) <= 160)
        self.assertNotIn("THE RULE CATALOG", body)
        self.assertNotRegex(body, r"\b(?:fork|context|allowed-tools):")

    def test_local_markdown_links_resolve_inside_package(self):
        count = 0
        for path in package_files():
            if path.suffix != ".md":
                continue
            text = path.read_text(encoding="utf-8")
            for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                if link.startswith(("https://", "#")):
                    continue
                with self.subTest(file=path.relative_to(ROOT), link=link):
                    target = (path.parent / link.split("#", 1)[0]).resolve()
                    self.assertTrue(target.is_relative_to(ROOT))
                    self.assertTrue(target.is_file())
                count += 1
        self.assertGreaterEqual(count, 8)

    def test_official_urls_and_lookup_only_boundary(self):
        text = (SKILL.parent / "references/standard-reference.md").read_text(
            encoding="utf-8"
        )
        self.assertEqual(set(re.findall(r"https://[^)\s]+", text)), {
            "https://www.asd-ste100.org/STE_downloads.html",
            "https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf",
        })
        self.assertIn("lookup targets", text)
        self.assertIn("not reproduced rule text", text)
        self.assertIn("Verify each target", text)
        for target in ("1.12", "2.2", "5.2", "5.4", "6.3", "8.5", "8.6", "9.1", "GR-6"):
            with self.subTest(target=target):
                self.assertIn(target, text)

    def test_retired_unsafe_guidance_does_not_return(self):
        patterns = [
            r"a suggestion is stated as fact or deleted",
            r"should \(recommendation\).*delete it, or state it as fact",
            r"approved modals: can, will, must\. banned:",
            r"may / might / could \(possibility\).*can",
            r"ste bans hedges",
            r"every hit.*is a violation",
            r"all structural rules",
            r"config / configuration / settings / options.*pick one",
            r"is designed to, aims to.*say what it does",
            r"simple past only",
            r"\*\*before \(real unedited",
        ]
        docs = [path for path in package_files() if path.suffix == ".md"]
        for path in docs:
            text = path.read_text(encoding="utf-8").lower()
            for pattern in patterns:
                with self.subTest(file=path.relative_to(ROOT), pattern=pattern):
                    self.assertNotRegex(text, pattern)

    def test_publication_hygiene(self):
        private_shapes = [
            r"/(?:Users|home)/[^/\s]+",
            r"/(?:private/)?tmp/[^\s]+",
            r"[A-Za-z]:\\(?:Users|Temp)\\",
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
            r"\b[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}\b",
        ]
        for path in package_files():
            relative = str(path.relative_to(ROOT))
            with self.subTest(file=relative):
                self.assertNotRegex(
                    relative.lower(),
                    r"\.(?:pdf|log|jsonl|docx|zip)$|(?:transcript|private-report|corpus)"
                )
                text = path.read_text(encoding="utf-8")
                for pattern in private_shapes:
                    self.assertNotRegex(text, pattern)

    def test_license_and_validation_boundaries(self):
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("MIT License", license_text)
        self.assertIn("Simple English contributors", license_text)
        self.assertIn("original guidance and code", license_text)
        for name in ("README.md", "AGENTS.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("python3 -B -m unittest discover -s tests -v", text)
            self.assertIn("static guards", text)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("not proof of model behavior", readme)
        self.assertIn("source registration", readme)
        self.assertIn('load_skill(skill_name="simple-english")', readme)
        self.assertIn("skill_directory", readme)
        self.assertIn(
            "git+https://github.com/samueljklee/"
            "amplifier-skill-simple-english@main#subdirectory=skills", readme
        )

    def test_synthetic_fixture_shape_and_coverage(self):
        data = json.loads((ROOT / "tests/fixtures.json").read_text(encoding="utf-8"))
        self.assertEqual(set(data), {"schema_version", "provenance", "purpose", "cases"})
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(data["provenance"], "synthetic")
        self.assertIn("static tests validate shape only", data["purpose"])
        self.assertEqual(len(data["cases"]), 10)
        self.assertEqual({case["id"] for case in data["cases"]}, CASE_IDS)
        for case in data["cases"]:
            with self.subTest(case=case["id"]):
                self.assertEqual(set(case), {
                    "id", "mode", "task", "context", "input",
                    "expected_invariants", "protected_spans",
                })
                self.assertIn(case["mode"], {"pragmatic", "strict"})
                self.assertIn(case["task"], {"rewrite", "review"})
                for key in ("context", "input"):
                    self.assertIsInstance(case[key], str)
                    self.assertTrue(case[key].strip())
                invariants = case["expected_invariants"]
                self.assertIsInstance(invariants, list)
                self.assertTrue(invariants)
                self.assertTrue(all(isinstance(item, str) and item.strip()
                                    for item in invariants))
                spans = case["protected_spans"]
                self.assertIsInstance(spans, list)
                self.assertEqual(len(spans), len(set(spans)))
                for span in spans:
                    self.assertIsInstance(span, str)
                    self.assertTrue(span)
                    self.assertIn(span, case["input"])


if __name__ == "__main__":
    unittest.main()