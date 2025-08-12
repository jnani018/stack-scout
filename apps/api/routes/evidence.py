from fastapi import APIRouter
from core_store import DOCS
router = APIRouter()

@router.get("")
def evidence():
    out = []
    for tool_id, docs in DOCS.items():
        out.append({"tool_id": tool_id, "sources": [{"url": d["src_url"]} for d in docs]})
    return {"items": out}
