"""KV-14 CLI - Typer based"""
import typer
from pathlib import Path
from api.client import KV14Client

app = typer.Typer(help="KV-14 Agentic Swarm CLI", add_completion=False)

@app.command()
def analyze(path: str, language: str = "auto", base_url: str = "http://localhost:8000"):
    """Analyze a file"""
    client = KV14Client(base_url=base_url)
    result = client.analyze_file(path)
    typer.echo(f"Risk: {result['risk_score']}/100")
    for b in result.get("bugs", []):
        typer.echo(f"Bug {b['type']} at line {b['line']}: {b['explanation']}")
    if not result.get("bugs"):
        typer.echo("No critical bugs.")

@app.command()
def fix(path: str, language: str = "auto", base_url: str = "http://localhost:8000", apply: bool = False):
    """Generate fix diff"""
    code = Path(path).read_text()
    client = KV14Client(base_url=base_url)
    res = client.fix(code)
    typer.echo(res["diff"])
    if apply:
        Path(path).write_text(res["fixed"])
        typer.echo("Applied fix.")

@app.command()
def swarm(repo: str = ".", goal: str = "fix and review", base_url: str = "http://localhost:8000"):
    """Run full swarm on repo"""
    files = {}
    for p in Path(repo).rglob("*"):
        if p.is_file() and p.suffix in [".py",".js",".ts",".go",".rs",".java"]:
            try:
                files[str(p)] = p.read_text()[:8000]
                if len(files) > 20:
                    break
            except:
                pass
    client = KV14Client(base_url=base_url)
    res = client.swarm(files, goal)
    typer.echo(f"Plan: {res['plan']}")
    typer.echo(f"Consensus: {res['consensus']}")

@app.command()
def health(base_url: str = "http://localhost:8000"):
    client = KV14Client(base_url=base_url)
    typer.echo(client.health())

if __name__ == "__main__":
    app()
# minimalist: typer --help polish
HELP_EXAMPLE="kv14 analyze --file app.py"
QUIET_JSON=True  # --quiet outputs raw JSON only
