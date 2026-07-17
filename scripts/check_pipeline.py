from pathlib import Path
import sys

required = [
    "README.md", "START_HERE.md", "BOOTSTRAP_CONTRACT.md", "MANIFEST.md",
    "AGENTS.md", "CLAUDE.md", "GEMINI.md",
    "docs/INDEX.md", "docs/CURRENT.md", "docs/DECISIONS.md",
    "docs/FOUNDER_AUTOPILOT.md", "docs/CONTEXT_MANAGEMENT.md",
    "docs/PIPELINE.md", "docs/TOOLING.md", "docs/SKILLS.md",
    "docs/TESTING.md", "docs/RELEASE.md",
    "docs/PIPELINE_UPDATE_RECOMMENDATIONS.md",
    "prompts/start-project-session.md", "prompts/bootstrap-project.md",
    "prompts/investigate-change.md", "prompts/implement-change.md",
    "prompts/verify-change.md", "prompts/test-user-flow.md",
    "prompts/audit-change.md",
]

forbidden_tokens = (
    "-final", "_final", "-latest", "_latest", "-updated", "_updated",
    "-new", "_new", "-v2", "_v2", "-v3", "_v3",
)

required_skill_sources = (
    "phuryn/pm-skills",
    "mattpocock/skills",
    "coreyhaines31/marketingskills",
)

required_phrases = {
    "docs/FOUNDER_AUTOPILOT.md": (
        "The founder is not responsible for",
        "The orchestration hub must automatically",
        "Mandatory manual approval gates",
    ),
    "docs/CONTEXT_MANAGEMENT.md": (
        "The repository stores durable truth",
        "One-ticket execution rule",
        "Fresh-context review",
    ),
    "docs/PIPELINE.md": (
        "Founder Autopilot Mode is the default interface",
        "Automatic request routing",
        "Canonical skills-output mapping",
    ),
    "docs/SKILLS.md": (
        "The founder must not be required to",
        "Installation versus activation",
        "Canonical-output rule",
    ),
    "AGENTS.md": (
        "Founder Autopilot",
        "The orchestrator selects skills automatically",
        "Never claim success without evidence",
    ),
    "START_HERE.md": (
        "Access preflight",
        "Recovery confidence",
        "Never require the founder to know or invoke them",
    ),
}

missing = [path for path in required if not Path(path).is_file()]

bad_names = []
for path in Path(".").rglob("*.md"):
    lowered = path.stem.lower()
    if any(token in lowered for token in forbidden_tokens):
        bad_names.append(str(path))

missing_skill_sources = []
skills_doc = Path("docs/SKILLS.md")
if skills_doc.is_file():
    skills_text = skills_doc.read_text(encoding="utf-8")
    missing_skill_sources = [
        source for source in required_skill_sources if source not in skills_text
    ]

missing_phrases = []
for file_path, phrases in required_phrases.items():
    path = Path(file_path)
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            missing_phrases.append(f"{file_path}: {phrase}")

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

if missing_phrases:
    print("Missing required governance language:")
    for item in missing_phrases:
        print(f" - {item}")

if missing or bad_names or missing_skill_sources or missing_phrases:
    sys.exit(1)

print("Universal pipeline checks passed.")
