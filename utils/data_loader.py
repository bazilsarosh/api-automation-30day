import json
from pathlib import Path

def load_json(relative_path: str):
    path = Path(__file__).resolve().parent.parent / relative_path
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
