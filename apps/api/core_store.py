import json, pathlib
BASE = pathlib.Path(__file__).parents[2] / "seed"

with open(BASE / "tools.json") as f:
    TOOLS = {t["id"]: t for t in json.load(f)["tools"]}

with open(BASE / "credits.json") as f:
    CREDITS = {}
    for c in json.load(f)["credits"]:
        CREDITS.setdefault(c["tool_id"], []).append(c)

with open(BASE / "docs.json") as f:
    DOCS = {}
    for d in json.load(f)["docs"]:
        DOCS.setdefault(d["tool_id"], []).append(d)

def list_tools(category=None, region=None):
    items = list(TOOLS.values())
    if category:
        items = [t for t in items if t["category"] == category]
    if region:
        items = [t for t in items if region in t.get("region_tags", [])]
    return items

def tool_by_name(name:str):
    for t in TOOLS.values():
        if t["name"].lower() == name.lower():
            return t
    return None

def credits_for(tool_id):
    return CREDITS.get(tool_id, [])

def docs_for(tool_id):
    return DOCS.get(tool_id, [])
