from pathlib import Path
from lab_helpers import ask, skill, clean_code


def fix_bugs(file):
    path = Path(file)
    code = path.read_text()
    reports = Path(f"reports/{path.stem}.md").read_text()

    result = ask(
        skill("bug-fixer"),
        f"Original code:\n{code}\n\nBug reports:\n{reports}",
        max_new_tokens=1500
    )

    fixed_code = clean_code(result)
    compile(fixed_code, file, "exec")
    path.write_text(fixed_code + "\n")

    print(f"[OK] Fixed code saved in {file}")
    print(fixed_code)
