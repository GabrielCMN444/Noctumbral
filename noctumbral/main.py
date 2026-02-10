import typer
from rich import print
from noctumbral.core.case import create_case, add_evidence, add_note, generate_report, list_cases

app = typer.Typer(help="Noctumbral — Noir Forensic Assistant CLI")

@app.command()
def new(name: str):
    """Create a new investigation case."""
    path = create_case(name)
    print(f"[bold green][+][/bold green] Case criado: {path}")

@app.command()
def add(case_name: str, content: str = typer.Argument(None), note: str = typer.Option(None, "--note")):
    """Add evidence or a note to a case."""
    if note:
        add_note(case_name, note)
    elif content:
        add_evidence(case_name, content)
    else:
        print("[bold red][!][/bold red] Você precisa fornecer um arquivo ou uma nota.")

@app.command()
def report(case_name: str):
    """Generate a report for a case."""
    generate_report(case_name)

@app.command()
def cases():
    """List all cases."""
    list_cases()

@app.command()
def about():
    """Show information about Noctumbral."""
    print("[bold]Noctumbral[/bold] — forensic assistant in the shadows.")
    print("Built for investigation, analysis, and reporting.")

if __name__ == "__main__":
    app()
