from pathlib import Path
from datetime import datetime
from rich import print

BASE_DIR = Path(__file__).parent.parent / "cases"
BASE_DIR.mkdir(exist_ok=True)

def create_case(name: str):
    case_dir = BASE_DIR / name
    evidence_dir = case_dir / "evidence"
    notes_dir = case_dir / "notes"
    reports_dir = case_dir / "reports"

    for d in [case_dir, evidence_dir, notes_dir, reports_dir]:
        d.mkdir(parents=True, exist_ok=True)

    case_file = case_dir / "case.txt"
    case_file.write_text(f"Case: {name}\nCreated: {datetime.now()}")
    return str(case_dir)

def add_evidence(case_name: str, path: str):
    case_dir = BASE_DIR / case_name
    if not case_dir.exists():
        print(f"[bold red][!][/bold red] Caso '{case_name}' não encontrado.")
        return

    file_path = Path(path)
    if not file_path.exists():
        print(f"[bold red][!][/bold red] Arquivo '{path}' não encontrado.")
        return

    dest = case_dir / "evidence" / file_path.name
    dest.write_bytes(file_path.read_bytes())
    print(f"[bold green][+][/bold green] Evidence added: {dest}")

def add_note(case_name: str, content: str):
    case_dir = BASE_DIR / case_name
    if not case_dir.exists():
        print(f"[bold red][!][/bold red] Caso '{case_name}' não encontrado.")
        return

    note_file = case_dir / "notes" / f"note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    note_file.write_text(content)
    print(f"[bold green][+][/bold green] Note added: {content}")

def generate_report(case_name: str):
    case_dir = BASE_DIR / case_name
    if not case_dir.exists():
        print(f"[bold red][!][/bold red] Caso '{case_name}' não encontrado.")
        return

    report_file = case_dir / "reports" / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    report_content = f"# Report for {case_name}\nGenerated: {datetime.now()}"
    report_file.write_text(report_content)
    print(f"[bold green][+][/bold green] Relatório gerado em: {report_file}")

def list_cases():
    if not BASE_DIR.exists():
        print("Nenhum caso encontrado.")
        return
    cases = [c.name for c in BASE_DIR.iterdir() if c.is_dir()]
    print("Casos existentes:")
    for c in cases:
        print(f" - {c}")
