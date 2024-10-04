import json
import sys
from pathlib import Path

env = sys.argv[1] if len(sys.argv) > 1 else "production"
path = Path(__file__).resolve().parents[1] / "config" / (env + ".json")
if not path.exists():
    path = path.with_name("production.json")
print(path.read_text())
