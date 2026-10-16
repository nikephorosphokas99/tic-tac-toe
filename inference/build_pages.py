"""Builds docs/ for GitHub Pages: the same page + Python files, running in the
browser with Pyodide instead of the local server.

    python inference/build_pages.py
"""
import shutil
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
DOCS = ROOT / "docs"

FILES = {
    HERE / "page.html": "index.html",
    HERE / "transport_pyodide.js": "transport.js",
    ROOT / "api.py": "api.py",
    ROOT / "mcts_agent.py": "mcts_agent.py",
    ROOT / "mcts_agent_xoxo.py": "mcts_agent_xoxo.py",
    HERE / "game.py": "game.py",
}

DOCS.mkdir(exist_ok=True)
for source, target in FILES.items():
    shutil.copyfile(source, DOCS / target)
    print(f"docs/{target}")
