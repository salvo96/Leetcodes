from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ["Easy", "Medium", "Hard"]

PROBLEM_DIR_PATTERN = re.compile(r"^\d+_.+")


def is_solved_problem(path: Path) -> bool:
    return (
        path.is_dir()
        and PROBLEM_DIR_PATTERN.match(path.name) is not None
        and (path / "solution.py").exists()
    )


def count_level(level: str) -> int:
    level_path = ROOT / level
    if not level_path.exists():
        return 0

    count = 0
    for path in level_path.rglob("*"):
        if is_solved_problem(path):
            count += 1
    return count


def update_readme(counts: dict[str, int]) -> None:
    readme_path = ROOT / "README.md"
    content = readme_path.read_text(encoding="utf-8")

    start_marker = "<!-- PROGRESS_START -->"
    end_marker = "<!-- PROGRESS_END -->"

    new_block = f"""<!-- PROGRESS_START --> <div align="center">
![Easy](https://img.shields.io/badge/Easy-{counts["Easy"]}-brightgreen) ![Medium](https://img.shields.io/badge/Medium-{counts["Medium"]}-yellow) ![Hard](https://img.shields.io/badge/Hard-{counts["Hard"]}-red) ![Total](https://img.shields.io/badge/Total-{sum(counts.values())}-blue)
</div>
<!-- PROGRESS_END -->"""

    if start_marker in content and end_marker in content:
        pattern = re.compile(
            rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
            re.DOTALL,
        )
        content = pattern.sub(new_block, content)
    else:
        lines = content.splitlines()

        inserted = False
        for i, line in enumerate(lines):
            if line.startswith("# "):
                lines.insert(i + 1, "")
                lines.insert(i + 2, new_block)
                inserted = True
                break

        if not inserted:
            lines.insert(0, new_block)

        content = "\n".join(lines)

    readme_path.write_text(content, encoding="utf-8")


def main():
    counts = {level: count_level(level) for level in LEVELS}
    update_readme(counts)
    print(counts)


if __name__ == "__main__":
    main()
