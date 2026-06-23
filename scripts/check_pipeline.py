from pathlib import Path
import sys

required = [
    "README.md", "START_HERE.md", "BOOTSTRAP_CONTRACT.md", "MANIFEST.md",
    "AGENTS.md", "CLAUDE.md", "GEMINI.md",
    "docs/INDEX.md", "docs/CURRENT.md", "docs/DECISIONS.md",
    "docs/PIPELINE.md", "docs/TOOLING.md", "docs/SKILLS.md",
    "docs/TESTING.md", "docs/RELEASE.md",
    "prompts/start-project-session.md", "prompts/bootstrap-project.md",
]

forbidden_tokens = (
    "-final", "_final", "-latest", "_latest", "-updated", "_updated",
    "-new", "_new", "-v2", "_v2", "-v3", "_v3",
)

missing = [p for p in required if not Path(p).is_file()]
bad_names = []
for path in Path(".").rglob("*.md"):
    lowered = path.stem.lower()
    if any(token in lowered for token in forbidden_tokens):
        bad_names.append(str(path))

skills_doc = Path("docs/SKILLS.md")
required_skill_sources = (
    "phuryn/pm-skills",
    "mattpocock/skills",
    "coreyhaines31/marketingskills",
)
missing_skill_sources = []
if skills_doc.is_file():
    skills_text = skills_doc.read_text(encoding="utf-8")
    missing_skill_sources = [
        source for source in required_skill_sources if source not in skills_text
    ]

if missing:
    print("Missing required pipeline files:")
    for item in missing:
        print(f" - {item}")
if bad_names:
    print("Potential duplicate/versioned document names:")
    for item in bad_names:
        print(f" - {item}")
if missing_skill_sources:
    print("Missing approved skill sources from docs/SKILLS.md:")
    for item in missing_skill_sources:
        print(f" - {item}")
if missing or bad_names or missing_skill_sources:
    sys.exit(1)
print("Universal pipeline checks passed.")
